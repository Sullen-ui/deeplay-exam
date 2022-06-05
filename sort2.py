import time, sys, re

with open('logo.txt', 'r') as file:
    for line in file:
        sys.stdout.write('\33[35m'+line + '\x1b[0m')
        sys.stdout.flush()
        time.sleep(0.1) 
sys.stdout.write('\n')
file.close()

ip = input('Введите IP-адрес: ')
s = []
with open('log.txt', 'r') as file:
    for line in file:
        if ip in line:
          r = re.findall('sid=/(.*?)/&', line)
          s += r 
    s.sort()
    print(*s, sep="\n") 
    file.close()
    if input('Cохранить в файл? (Y/n): ') == 'Y':
        f= open('out '+ ip +'.txt', 'w')
        for i in s:
            f.write(ip + ': sid = ' + i + '\n')
        print('Сохранено в файл', f.name)
        f.close()

