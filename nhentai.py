import random
import requests
import time
import os
error = int(0)
wrkng = int(0)
num = int(input("How Many? - "))
name = input("Name of output text file? - ")
print("CAUTION: Sending can be slow if your internet connection is slow.")
start = time.time()
end = time.time()
for i in range(num):
    True
    while True:
        outF = open(name + ".txt", "a")
        seed = random.sample(range(374305), 1)
        if(num == wrkng):
            break
        url = "http://nhentai.to/g/" + str(seed)
        s = url
        c = seed
        fl = url
        s1 = s.replace("[","")
        s2 = s1.replace("]", "")
        r = requests.get(s2)
        if r.status_code == 404:
            error += 1
            errurl = url
        else:
            outF.writelines(str(s2))
            outF.write('\n')
            wrkng += 1
        
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')
        print("Counter:")
        print("Error: " + str(error))
        print("Completed: " + str(wrkng))

 
end = time.time()
print(str(end - start) + " second/s elapsed.")
print("Output: " + name + ".txt")
print("404 = " + str(error))
print("Working = " + str(wrkng))
input("Press Enter to continue...")
