<h2>Задание №1</h2>
Имеется лог файл log.txt.<br>
Необходимо при помощи любых локальных инструментов (bash,python ...) <br>
получить отсортированный список всех значений sid в строках с IP=10.1.192.38<br>
Значения sid должны быть без ограничивающих символов '/',<br>
кроме тех, что находятся внутри значения.<br>
<br>
<h3>Реализация:</h3>
<h4>Вариант 1(Скучный, питоновый) - [sort.py](../blob/main/sort.py)</h4>

    #Импорт модуля re для работы с регулярками
    import re
    # Список под конечный результат
    s = []
    # Открываю лог-файл
    with open('log.txt', 'r') as file:
        # Перебор строк 
        for line in file:
            # Условие на вхождение IP в строку
            if '10.1.192.38' in line:
                # Беру нужный отрезок
                r = re.findall('sid=/(.*?)/&', line)
                # Добавляю в список
                s += r
        # Сортирую список      
        s.sort()
        # Вывожу на экран
    print(*s, sep="\n")
    # Закрываю файл
    file.close()

Вариант 2(Весёлый, питоновый. Мне нравиться больше. Просьба запустить) - sort2.py
$python sort2.py

Вариант 3(Баш) - sort.sh
Обрезал нужную часть слева и справа затем сортировка
#!/bin/bash
grep '10.1.192.38' log.txt | sed 's/^.*sid=\///;s/\/&type.*//' | sort


Задание 2
Имеется app.jar файл.
Для его запуска используется команда java -jar app.jar some_out_file "Service is working!"
Напишите простой демон для systemd (Linux), который будет поддерживать работу приложения и перезапускать его в случае
выхода из строя процесса.
Необходимо сделать защиту от зацикливания перезапусков, когда процесс постоянно выходит из строя.

Реализация:

[Unit]
Description=JavaApp

[Service]
Type=forking
ExecStart=sudo java -jar /var/www/java-app/app.jar /var/log/java-app/log.txt
Restart=on-failure
RestartSec=5
StartLimitInterval=5

[Install]
WantedBy=multi-user.target

![image](https://user-images.githubusercontent.com/82956250/172077163-4006646d-4fb3-4bda-b702-af6a8a08f9e3.png)



