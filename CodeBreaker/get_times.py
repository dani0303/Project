import json
from pathlib import Path


log = "C:\\Users\\Dan\\Documents\\vpn.log"
text = Path(log).read_text()
text = text.replace('\n', '')

for i in range(len(text)):
    if text[i: i + 4] == "EDT,":
        for j in range((i + 5), len(text)):
            if text[j: j + 1] == ",":
                time = text[i + 4: j]
                if time == ",VPN":
                    file = open("names.txt")
                    file.write("nothing")
                    file.close()
                else:
                    file = open("names.txt")
                    file.write(str(time))
                    file.close()
                break
print("completed")
