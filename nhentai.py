import requests
import time
import re

url = "https://nhentai.net/random/"

num = int(input("How Many? - "))
name = input("Name of output text file? - ")
print("CAUTION: The generation of the codes can be slow if your internet connection is slow.")

tries = 0
start = time.time()
codes = set()

while len(codes) != num:
    tries += 1
    r = requests.get(url).url
    code = re.findall(r"(\d+)", r)
    if len(code):
        codes.add(code[0])

codes = list(codes)

with open(name, "w") as f:
    f.write("\n".join(codes))


end = time.time()
print(str(end - start) + " second/s elapsed.")
print("Found {} with {} tries.".format(len(codes), tries))
input("Press Enter to continue...")
