import os
import sys
import time
from random import randint, choice
from colorama import Fore, Style
import pyfiglet

os.system('cls')

f = pyfiglet.Figlet(font='slant')
ascii_art = f.renderText('GENPASS')
print(Fore.BLUE + ascii_art + Fore.WHITE + "         [*] Creado por hack4ever " + "\n")

def main():

    print(Fore.GREEN + Style.BRIGHT + "[+] Bienvenido a la aplicación de generacion de contraseñas")
    print(Fore.YELLOW + Style.BRIGHT + "1. Generar contraseña aleatoria")
    print(Fore.YELLOW + Style.BRIGHT + "2. Generar contraseña por numero de telefono")
    print(Fore.YELLOW + Style.BRIGHT + "3. generar contraseñas personlizadas")
    print(Fore.YELLOW + Style.BRIGHT + "4. Salir")
    contraseña = int(input(Fore.BLUE + Style.BRIGHT + "[+] Ingrese una opción: "))
    select(contraseña)

def select(contraseña):
    if contraseña == 1:
        aleatoria()
    elif contraseña == 2:
        telefono()
    elif contraseña == 3:
        personalizada()
    elif contraseña == 4:
        exit()
    else:
        print(Fore.RED + Style.BRIGHT + "[+] Opción no valida")
        main()

def aleatoria():
    os.system('cls')

    f = pyfiglet.Figlet(font='slant')
    ascii_art = f.renderText('GENPASS')
    print( Fore.BLUE + ascii_art)

    cantidad = int(input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la cantidad de contraseñas: "))
    print(Fore.GREEN + Style.BRIGHT + "[+] Generando contraseña aleatoria", end="\n")

    nombres = ["Alejandro", "Carlos", "Diego", "Fernando", "Guillermo", "Hugo", "Luis", "Manuel", 
               "Pedro", "Rafael", "Santiago", "Tomas", "Victor", "javier", "Maria", "Juan", 
               "Miguel", "Valery", "Maira"]

    apellidos = ["Alvarez", "Arias", "Benitez", "Castro", "Diaz", "Espinosa", "Garcia", 
                 "Hernandez", "Lopez", "Martinez", "Perez", "Reyes", "Rodriguez", "Sanchez", "Torres"]

    palabras = ["colombia", "familia", "Familia", "casa", "quinta", "carro", 
                "realmadrid", "RealMadrid", "Barcelona", "futbol"]

    signos = ["+", "-", "*", "/", "%", "!", "?", "&", "@", "#", "$", "|", ";", ".", ",", "_", "="]

    with open("aleatoria.txt", "w") as f:
        for i in range(cantidad):
            i = i + 1
            nombre = choice(nombres)
            apellido = choice(apellidos)
            palabra = choice(palabras)
            signo = choice(signos)

            f.write(nombre + apellido + str(randint(1000, 9999)) + "\n")
            f.write(nombre + signo + str(randint(1000, 9999)) + "\n")
            f.write(palabra + str(randint(1000, 9999)) + "\n")
            f.write(palabra + signo + str(randint(1000, 9999)) + "\n")

            print(f"palabra {i} generada", end="\r")

        print(Fore.GREEN + Style.BRIGHT + "[+] Contraseñas guardadas en aleatoria.txt")
        main()
def telefono():
    os.system('cls')

    f = pyfiglet.Figlet(font='slant')
    ascii_art = f.renderText('GENPASS')
    print( Fore.BLUE + ascii_art)

    cantidad = int(input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la cantidad de contraseñas: "))
    print(Fore.YELLOW + Style.BRIGHT + "[+] Generando contraseña por numero de telefono", end="\n")
    with open("telefono.txt", "w") as f:
        for i in range(10):
            i = i + 1
            f.write("300" +str(randint(2000000, 9399999)) + "\n")
            f.write("301" +str(randint(2000000, 7999999)) + "\n")
            f.write("302" +str(randint(2000000, 4699999)) + "\n")
            f.write("303" +str(randint(2000000, 6849999)) + "\n")
            f.write("304" +str(randint(2000000, 3899999)) + "\n")
            f.write("305" +str(randint(2000000, 9599999)) + "\n")
            f.write("310" +str(randint(2000000, 9999999)) + "\n")
            f.write("311" +str(randint(2000000, 9999999)) + "\n")
            f.write("312" +str(randint(2000000, 9999999)) + "\n")
            f.write("313" +str(randint(2000000, 9999999)) + "\n")
            f.write("314" +str(randint(2000000, 9999999)) + "\n")
            f.write("315" +str(randint(2000000, 9999999)) + "\n")
            f.write("316" +str(randint(2000000, 9999999)) + "\n")
            f.write("317" +str(randint(2000000, 9999999)) + "\n")
            f.write("318" +str(randint(2000000, 9999999)) + "\n")
            f.write("319" +str(randint(2000000, 9999999)) + "\n")
            f.write("320" +str(randint(2000000, 9999999)) + "\n")
            f.write("321" +str(randint(2000000, 9999999)) + "\n")
            f.write("322" +str(randint(2000000, 9999999)) + "\n")
            f.write("323" +str(randint(2000000, 9999999)) + "\n")
            f.write("324" +str(randint(1000000, 9999999)) + "\n")

            print(f"numero {i} generada", end="\r")
        print(Fore.GREEN + Style.BRIGHT + "[+] Contraseñas guardadas en telefono.txt")
    main()


def personalizada():
    os.system('cls')

    f = pyfiglet.Figlet(font='slant')
    ascii_art = f.renderText('GENPASS')
    print( Fore.BLUE + ascii_art)

    cantidad = int(input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la cantidad de contraseñas: "))

    user = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el nombre de la persona: ")
    lastname = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el apellido: ")
    fecha = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la fecha de nacimiento[ddmmaa]: ")
    user_num = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el numero de telefono: ")
    apodo = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el apodo: ")


    user_mon = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el nombre de la madre: ")
    lastname_mon = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el apellido de la madre: ")
    fecha_mon = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la fecha de nacimiento de la madre [ddmmaa]: ")
    user_father = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el nombre del padre: ")
    lastname_father = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el apellido del padre: ")
    fecha_father = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la fecha de nacimiento del padre [ddmmaa]: ")

    nombres = [user, user_mon, user_father]
    apellidos = [lastname, lastname_mon, lastname_father]
    fechas = [fecha, fecha_mon, fecha_father, ""]
    numeros = [user_num]

    par = input(Fore.GREEN + Style.BRIGHT + "[+] tiene pareja[s/n]: ")
    if par == "s":
        pareja = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el nombre de la pareja: ")
        lastname_par = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el apellido de la pareja: ")
        num_par = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el numero de telefono de la pareja: ")
        fecha_par = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la fecha de nacimiento de la pareja [ddmmaa]: ")
        nombres.append(pareja)
        apellidos.append(lastname_par)
        numeros.append(num_par)
        fechas.append(fecha_par)
    else:
        pass

    herm = input(Fore.GREEN + Style.BRIGHT + "[+] tiene hermanos[s/n]: ")
    if herm == "s":
        hermano_1 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingresa nombre de hermano: ")
        lastname_her_1 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingresa apellido de hermano: ")
        hermano_2 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingresa nombre de hermano: ")
        lastname_her_2 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingresa apellido de hermano: ")
        nombres.append(hermano_1)
        apellidos.append(lastname_her_1)
        nombres.append(hermano_2)
        apellidos.append(lastname_her_2)
    else:
        pass

    hijo = input(Fore.GREEN + Style.BRIGHT + "[+] tiene hijos[s/n]: ")
    if hijo == "s":
        user_child = input(Fore.GREEN + Style.BRIGHT + "[+] Ingresa nombre de hijo: ")
        lastname_child = input(Fore.GREEN + Style.BRIGHT + "[+] Ingresa apellido de hijo: ")
        fecha_child = input(Fore.GREEN + Style.BRIGHT + "[+] Ingresa fecha de nacimiento de hijo [ddmmaa]: ")
        nombres.append(user_child)
        apellidos.append(lastname_child)
        fechas.append(fecha_child)
    else:
        pass
    mascota = input(Fore.GREEN + Style.BRIGHT + "[+] tiene mascota[s/n]: ")
    if mascota == "s":
        mascota = input(Fore.GREEN + Style.BRIGHT + "[+] Ingresa nombre de mascota: ")
        fecha_mascota = input(Fore.GREEN + Style.BRIGHT + "[+] Ingresa fecha de adoptacion de mascota [ddmmaa]: ")
        nombres.append(mascota)
        fechas.append(fecha_mascota)
    else:    
        pass

    signos = ["","+", "-", "*", "%", "!", "&", "@", "#", "$", ".", "_"]

    print(Fore.YELLOW + Style.BRIGHT + "[+] Generando contraseña personalizada", end="\n")
    with open("personalizada.txt", "w") as f:
        for i in range(cantidad):
            nombre = choice(nombres)
            apellido = choice(apellidos)
            fecha = choice(fechas)
            signo = choice(signos)
            numeros = choice(numeros)

            i = i + 1

            f.write(nombre + apellido + fecha + "\n")
            f.write(apodo + signo + fecha +"\n")
            f.write(nombre + signo + fecha + "\n")
            f.write(numeros + signo + apodo + "\n")
            f.write(numeros + signo + nombre + "\n")
    
        print(Fore.GREEN + Style.BRIGHT + "[+] Contraseñas guardadas en personalizada.txt")
        main()

main()
