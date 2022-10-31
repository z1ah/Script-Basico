import os, time
from sys import stdout 

# Color Rojo
def red():
    RED = "\033[1;31m"
    stdout.write(RED)

# color azul
def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

# Banner con mi Logo
banner = """
     _____      _        _     
 ___|___ /  ___| |___  _| |__  
|_  / |_ \ / _ \ __\ \/ / '_ \ 
 / / ___) |  __/ |_ >  <| | | |
/___|____/ \___|\__/_/\_\_| |_| (Ahora Soy Piloto)
                               
"""   
# Menu Principal
def menuSystem():
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("Seleccione su Sistema operativo")
    print("\n1 -> Linux")
    time.sleep(1)
    print("\n2 -> MacOs")
    time.sleep(1)
    print("\n3 -> Windows")
    time.sleep(1)
    print("\n4 -> Salir")

    option = input("\n-->> ")

    if option == "1":
        menuLinux()
    if option == "2":
        menuMac()
    if option == "3":
        menuWin()
    if option == "4":
        exit()


# Menu para Procesos de Linux
def menuLinux():
    os.system("clear")
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("1 -> Actualizar Sistema")
    time.sleep(1)
    print("\n2 -> Apagar Computador")
    time.sleep(1)
    print("\n3 -> Mostra Interfaz de Red y IP")
    time.sleep(1)
    print("\n4 -> Salir")
    time.sleep(1)
    
    # Entrada de datos
    option = input("\n-->> ")

    if option == "1":
        os.system("clear")
        red()
        print(banner)
        print("\nEl Sistema se comenzara actualizar en 5 seg....")
        time.sleep(5)
        os.system("sudo apt update")
        
    if option == "2":
        os.system("clear")
        print(banner)
        print("\nApagando Computador")
        time.sleep(2)
        os.system("shutdown -h now")

    if option == "3":
        os.system("clear")
        print(banner)
        os.system("ifconfig")
        menuSystem()

    if option == "4":
        exit()



# Menu para Procesos de MacOs
def menuMac():
    os.system("clear")
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("1 -> Abrir Navegador")
    time.sleep(1)
    print("\n2 -> Apagar Computador")
    time.sleep(1)
    print("\n3 -> Mostra Interfaz de Red y IP")
    time.sleep(1)
    print("\n4 -> Salir")
    time.sleep(1)
    
    # Entrada de datos
    option = input("\n-->> ")

    if option == "1":
        os.system("clear")
        red()
        print(banner)
        print("\nSu navegador es safari :)")
        time.sleep(1)
        os.system("open -a safari https://www.youtube.com/watch?v=S2PVsv2K1Bg&ab_channel=SteveLacy-Topic")
        
    if option == "2":
        os.system("clear")
        print(banner)
        print("\nApagando Computador")
        time.sleep(2)
        os.system("sudo shutdown -h now")

    if option == "3":
        os.system("clear")
        print(banner)
        os.system("networksetup -getinfo Wi-Fi")
        menuSystem()

    if option == "4":
        exit()



# Menu para Procesos de Windows
def menuWin():
    os.system("clear")
    red()
    print(banner)
    blue()
    time.sleep(1)
    print("1 -> Abrir Navegador")
    time.sleep(1)
    print("\n2 -> Apagar Computador")
    time.sleep(1)
    print("\n3 -> Mostra Interfaz de Red y IP")
    time.sleep(1)
    print("\n4 -> Salir")
    time.sleep(1)
    
    # Entrada de datos
    option = input("\n-->> ")

    if option == "1":
        os.system("clear")
        red()
        print(banner)
        print("\nSu navegador es Chrome :)")
        time.sleep(1)
        os.system("Start chrome /incognito https://github.com/z3etxh")
        
    if option == "2":
        os.system("clear")
        print(banner)
        print("\nApagando Computador")
        time.sleep(2)
        os.system("shutdown /s")

    if option == "3":
        os.system("clear")
        print(banner)
        os.system("ipconfig /all")
        menuSystem()

    if option == "4":
        exit()

menuSystem()
