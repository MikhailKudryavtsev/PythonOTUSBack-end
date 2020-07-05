# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import time


name = os.name
print(f'\nCемейство ОС: {name}')

platform_os_ = sys.platform
print(f'\nВерсия ядра: {platform_os_}')

version_os = sys.version
print(f'\nВерсия ОС: {version_os}')

print(f'\nТекущуя директория {os.getcwd()} и список в файлов в ней: ')
subprocess.call(['ls'])

dir_ = input('\nУкажите директорию: ')
try:
    print(f"\nУказанная директория: {dir_}")
    subprocess.Popen("ls", cwd=dir_)
except FileNotFoundError:
    print('\nУказана неверная директория')
time.sleep(1)   #таймаут, чтобы список файлов успел отобразиться

print('\nСписок всех процессов: ')
subprocess.call(['ps', '-ef'])

print('\nИнформация о процессе "bash": ')
cmd = 'ps -ef | grep bash'
subprocess.call(cmd, shell=True)