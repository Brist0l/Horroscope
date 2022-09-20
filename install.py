#!/usr/bin/python3

import os

print()

if not os.path.exists(f"{os.path.expanduser('~')}/.local/bin/"):
    os.system("mkdir ~/.local/bin")
os.system("cp -r src/* ~/.local/bin")
os.chdir(f"{os.path.expanduser('~')}/.local/bin/")
os.system('mv main.py hscope')
os.system('sudo chmod +x hscope')