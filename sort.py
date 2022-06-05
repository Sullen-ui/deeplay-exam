import re
s = []
with open('log.txt', 'r') as file:
    for line in file:
        if '10.1.192.38' in line:
          r = re.findall('sid=/(.*?)/&', line)
          s += r
    s.sort()
    print(*s, sep="\n") 
