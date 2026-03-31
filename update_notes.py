import os

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

                            # loop through lines inside file
                            for i in range(len(lines)-1):
                                pattern0 = not lines[i].startswith("- ") and lines[i+1].startswith("- ") 
                                pattern1 = lines[i+1].startswith("$$") and not lines[i+2].startswith("---")
                                pattern2 = lines[i+1].startswith("---") 
                                pattern3 = lines[i].startswith("\\")
                                pattern4 = "![[" in lines[i]

                                # add hashtags and newlines
                                if pattern0 or pattern1:
                                    lines[i] = "### " + lines[i] + "\n"

                                # add newlines
                                if pattern2:
                                    lines[i] += "\n"
                                
                                # replace alignment
                                if pattern3:
                                    lines[i] = lines[i].replace("align*", "aligned")

                                # remove images
                                if pattern4:
                                    lines[i] = lines[i].split("![[")[0]
                            
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