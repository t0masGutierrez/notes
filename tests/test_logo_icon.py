import contextlib
import http.server
import pathlib
import socketserver
import sys
import threading
import unittest
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


EXPECTED_LOGO = "obsidian.png"
EXPECTED_CACHE_TOKEN = "v=2"


@contextlib.contextmanager
def static_server(root):
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=str(root), **kwargs)

        def log_message(self, format, *args):
            pass

    class QuietTCPServer(socketserver.TCPServer):
        allow_reuse_address = True

        def handle_error(self, request, client_address):
            exc_type, _, _ = sys.exc_info()
            if exc_type is BrokenPipeError:
                return
            super().handle_error(request, client_address)

    with QuietTCPServer(("127.0.0.1", 0), Handler) as httpd:
        thread = threading.Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{httpd.server_address[1]}"
        finally:
            httpd.shutdown()
            thread.join()


class LogoIconTest(unittest.TestCase):
    def test_page_uses_dedicated_uncached_obsidian_logo_for_icons_and_previews(self):
        repo_root = pathlib.Path(__file__).resolve().parents[1]
        expected_asset = repo_root / EXPECTED_LOGO
        favicon_asset = repo_root / "favicon.ico"
        manifest_asset = repo_root / "site.webmanifest"

        self.assertTrue(expected_asset.exists())
        self.assertTrue(favicon_asset.exists())
        self.assertTrue(manifest_asset.exists())
        self.assertGreater(expected_asset.stat().st_size, 1000)
        self.assertGreater(favicon_asset.stat().st_size, 1000)

        with static_server(repo_root) as base_url, sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(f"{base_url}/index.html", wait_until="domcontentloaded")

            icon_hrefs = page.evaluate(
                """
                () => Array.from(document.querySelectorAll('link[rel~="icon"], link[rel="shortcut icon"], link[rel="apple-touch-icon"]'))
                    .map((link) => link.href)
                """
            )
            self.assertGreaterEqual(len(icon_hrefs), 3)
            for href in icon_hrefs:
                parsed = urlparse(href)
                self.assertIn(parsed.path, [f"/{EXPECTED_LOGO}", "/favicon.ico"])
                self.assertEqual(parsed.query, EXPECTED_CACHE_TOKEN)
                self.assertNotIn("githubusercontent", href.lower())
                self.assertNotIn("avatars", href.lower())
                self.assertNotIn("/logo.png?", href.lower())

            for selector in ['meta[property="og:image"]', 'meta[property="og:image:secure_url"]', 'meta[name="twitter:image"]']:
                content = page.locator(selector).get_attribute("content")
                self.assertTrue(content.endswith(f"/{EXPECTED_LOGO}?{EXPECTED_CACHE_TOKEN}"))
                self.assertNotIn("githubusercontent", content.lower())
                self.assertNotIn("avatars", content.lower())

            manifest_href = page.locator('link[rel="manifest"]').get_attribute("href")
            self.assertEqual(manifest_href, f"site.webmanifest?{EXPECTED_CACHE_TOKEN}")
            manifest = page.request.get(f"{base_url}/site.webmanifest?{EXPECTED_CACHE_TOKEN}").json()
            manifest_icons = [icon["src"] for icon in manifest["icons"]]
            self.assertIn(f"{EXPECTED_LOGO}?{EXPECTED_CACHE_TOKEN}", manifest_icons)

            response = page.request.get(f"{base_url}/{EXPECTED_LOGO}?{EXPECTED_CACHE_TOKEN}")
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers.get("content-type"), "image/png")
            self.assertGreater(len(response.body()), 1000)
            browser.close()


if __name__ == "__main__":
    unittest.main()
