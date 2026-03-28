
import shlex

file_path = '/home/veli/.config/sway/config'

try:
    with open(file_path, 'r', encoding='utf-8') as sway_config:
        swayLines = sway_config.read().split("\n")
        swayKeybinds = []

        for line in swayLines:
            lineArgs = line.strip().split()
            if(lineArgs):
                if (lineArgs[0] == "bindsym"):
                        lineArgs.remove(lineArgs[0])
                        lineArgs = [lineArgs[0], " ".join(lineArgs[1:])]
                        swayKeybinds.append(lineArgs)                    

        
        for keybind in swayKeybinds:
            for i, arg in enumerate(keybind):
                if (arg == "-d"):
                    keybind = [keybind[0], keybind[i+1]]
            print(keybind)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")

