import os
import re

INLINE_MATH_PATTERN = re.compile(r"(?<!\\)\$(.+?)(?<!\\)\$")
SINGLE_CHAR_SUBSCRIPT_PATTERN = re.compile(r"(?<!\\)_([A-Za-z0-9])(?![A-Za-z0-9])")
LITERAL_HASH_PATTERN = re.compile(r"(?<!\\)#")

def sanitize_math_text(text):
    text = SINGLE_CHAR_SUBSCRIPT_PATTERN.sub(r"_{\g<1>}", text)
    return LITERAL_HASH_PATTERN.sub(r"\\#", text)

def sanitize_inline_math(line):
    return INLINE_MATH_PATTERN.sub(
        lambda match: f"${sanitize_math_text(match.group(1))}$",
        line,
    )

def update_notes():
    input = os.path.expanduser("~") + "/Obsidian/brainTwo/"
    output = os.path.expanduser("~") + "/Github/notes/"
    dirs = {}

    # loop through folders inside obsidian
    for dir in os.listdir(input):
        ignore = ["Templates", "Brain.base"]
        if not dir.startswith(".") and dir not in ignore:
            folder_name = dir
            folder_path = os.path.join(input, folder_name)
            dirs[folder_name] = {}

            # loop through files inside obsidian folder
            for file in os.listdir(folder_path):
                if file.endswith(".md"):
                    file_path = os.path.join(folder_path, file)
                    file_name = os.path.basename(file)[:-3] # remove suffix ".md"
                    dirs[folder_name][file_name] = file_path

                    # read from obsidian files
                    with open(file_path, "r") as obs:
                        data = obs.read()
                        os.makedirs(os.path.join(output, folder_name), exist_ok=True)

                        # write to github files
                        out_file = os.path.join(output, folder_name, file_name + ".md")
                        with open(out_file, "w") as git:
                            git.write(data)

                        # read from github files
                        with open(out_file, "r") as git:
                            lines = git.readlines()

                            in_math_block = False

                            # loop through lines inside file
                            for i in range(len(lines)):
                                next_line = lines[i + 1] if i + 1 < len(lines) else ""
                                line_after_next = lines[i + 2] if i + 2 < len(lines) else ""

                                pattern0 = not lines[i].startswith("- ") and next_line.startswith("- ")
                                pattern1 = next_line.startswith("$$") and not line_after_next.startswith("---")
                                pattern2 = next_line.startswith("---")
                                pattern3 = lines[i].startswith("\\")
                                pattern4 = "![[" in lines[i]

                                # add hashtags and newlines
                                if pattern0 or pattern1:
                                    lines[i] = "### " + lines[i].rstrip("\n") + "\n"

                                # add newlines
                                if pattern2:
                                    lines[i] = lines[i].rstrip("\n") + "\n\n"

                                # replace alignment
                                if pattern3:
                                    lines[i] = lines[i].replace("align*", "aligned")

                                # remove images
                                if pattern4:
                                    lines[i] = lines[i].split("![[")[0]

                                stripped_line = lines[i].strip()
                                if stripped_line == "$$":
                                    in_math_block = not in_math_block
                                    continue

                                if in_math_block:
                                    lines[i] = sanitize_math_text(lines[i])
                                else:
                                    lines[i] = sanitize_inline_math(lines[i])
                            
                            # write to github files
                            with open(out_file, "w") as git:
                                git.writelines(lines)

    # remove renamed/deleted files
    for folder_name in os.listdir(output):
        out_folder = os.path.join(output, folder_name)
        in_folder = os.path.join(input, folder_name)
        if os.path.isdir(out_folder) and os.path.isdir(in_folder):
            obsidian_files = set(f for f in os.listdir(in_folder) if f.endswith('.md'))
            github_files = set(f for f in os.listdir(out_folder) if f.endswith('.md'))
            for file in github_files:
                if file not in obsidian_files:
                    os.remove(os.path.join(out_folder, file))

def main():
    update_notes()

if __name__ == "__main__":
    main()