import json
from pathlib import Path

file = "C:\\Users\\Dan\\Documents\\vpn.log"
text = Path(file).read_text()
text = text.replace('\n', '')
for i in range(len(text)):
    if text[i: i + 1] == ",":
        print(text[i - i: i])
        break
