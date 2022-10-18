import json
from pathlib import Path

file = open("names.txt", "x")
log = "C:\\Users\\Dan\\Documents\\vpn.log"
text = Path(log).read_text()
text = text.replace('\n', '')


def main():
    for i in range(len(text)):
        if text[i: i + 15] == "openvpn-server,":
            for j in range((i + 15), len(text)):
                if text[j: j + 1] == ",":
                    name = text[(i + 15):j]
                    file.write(name + "\n")
                    break
main()
print("Completed")
