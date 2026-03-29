import shlex


def read_keybinds(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as sway_config:
            swayLines = sway_config.read().split("\n")
            swayKeybinds = []

            for line in swayLines:
                lineArgs = line.strip().split()
                if(lineArgs):
                    if (lineArgs[0] == "bindsym" or lineArgs[0] == "$mod"):
                            if (lineArgs[0] == "bindsym"):
                                lineArgs.remove(lineArgs[0])
                            lineArgs = [lineArgs[0], " ".join(lineArgs[1:])]
                            swayKeybinds.append(lineArgs)                    
            
            return swayKeybinds
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
