import os
import time

#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro

os.system("clear")
os.system("pkg install figlet")
os.system("clear")
print("\033[1;35m")
os.system("figlet F1GH")

#Funções do script.
print("""\033[1;31m
/====================\

l    [1]Sqlmap       l
l    [2]FBI          l
l    [3]DDos-Attack  l
l    [4]DDOS         l
l    [5]XERXES       l
l    [6]LITES-DDOS   l
l    [7]LITESPAM     l
l    [8]Trojans      l
l    [9]instabrute   l
l    [10]Black-Hydra l
l    [11]irssi       l
l    [12]Lazy        l
l    [13]Exit        l
\====================/
""")
op = input(">>>/")

if op == "1":
    os.system("""
    clear
    git clone https://github.com/sqlmapproject/sqlmap
    python3 F1GH.py
    """)
elif op == "2":
    os.system("""
    clear
    git clone https://github.com/xHak9x/fbi.git
    python3 F1GH.py
    """)
elif op == "3":
    os.system("""
    clear
    git clone https://github.com/Ha3MrX/DDos-Attack
    python3 F1GH.py
    """)
elif op == "4":
    os.system("""
    clear
    git clone https://github.com/pembriahmad/DDOS
    python3 F1GH.py
    """)
elif op == "5":
    os.system("""
    clear
    git clone https://github.com/XCHADXFAQ77X/XERXES
    python3 F1GH.py
    """)
elif op =="6":
    os.system("""
    clear
    git clone https://github.com/4L13199/LITEDDOS
    python3 F1GH.py
    """)
elif op == "7":
    os.system("""
    clear
    git clone https://github.com/4L13199/LITESPAM
    python3 F1GH.py
    """)
elif op == "8":
    os.system("""
    clear
    git clone https://github.com/R133F/Trojans
    python3 F1GH.py
    """)
elif op == "9":
    os.system("""
    clear
    git clone https://github.com/Ha3MrX/InstaBrute
    python3 F1GH.py
    """)
elif op == "10":
    os.system("""
    clear
    git clone https://github.com/Gameye98/Black-Hydra
    python3 F1GH.py
    """)
elif op == "11":
    os.system("""
    clear
    pkg install irssi
    python3 F1GH.py
    """)
elif op == "12":
    os.system("""
    clear
    git clone https://github.com/TechnicalMujeeb/Termux-Lazyscrip.git
    python3 F1GH.py
    """)
elif op == "13":
    print("Saindo!...")
    time.sleep(4)
    exit()
else:
    os.system("python3 F1GH.py")
