import os
import re

files = os.listdir("tmdb-data")

count = 0
for textfile in files:
    try:
        with open(f"tmdb-data\\{textfile}","r",encoding="utf-8") as f:
            text = f.read()

        find = re.search(r'"overview":".+"',text)
        if find:
            count = count + 1
    except:
        print("Error at :",textfile)

    
l = len(files)
print(count)
print(l)
print((count/l)*100)