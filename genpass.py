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
    print(Fore.GREEN + Style.BRIGHT + "[+] Bienvenido a la aplicación de generación de contraseñas")
    print(Fore.YELLOW + Style.BRIGHT + "1. Generar contraseña aleatoria")
    print(Fore.YELLOW + Style.BRIGHT + "2. Generar contraseña por número de teléfono")
    print(Fore.YELLOW + Style.BRIGHT + "3. Generar contraseñas personalizadas")
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
        print(Fore.RED + Style.BRIGHT + "[+] Opción no válida")
        main()

def aleatoria():
    os.system('cls')

    f = pyfiglet.Figlet(font='slant')
    ascii_art = f.renderText('GENPASS')
    print(Fore.BLUE + ascii_art)

    cantidad = int(input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la cantidad de contraseñas: "))
    print(Fore.GREEN + Style.BRIGHT + "[+] Generando contraseñas aleatorias...\n")

    nombres = ["Alejandro", "Carlos", "Diego", "Fernando", "Guillermo", "Hugo", "Luis", "Manuel", 
               "Pedro", "Rafael", "Santiago", "Tomas", "Victor", "Javier", "Maria", "Juan", 
               "Miguel", "Valery", "Maira"]

    apellidos = ["Alvarez", "Arias", "Benitez", "Castro", "Diaz", "Espinosa", "Garcia", 
                 "Hernandez", "Lopez", "Martinez", "Perez", "Reyes", "Rodriguez", "Sanchez", "Torres"]

    palabras = ["colombia", "familia", "Familia", "casa", "quinta", "carro", 
                "realmadrid", "RealMadrid", "Barcelona", "futbol"]

    signos = ["+", "-", "*", "/", "%", "!", "?", "&", "@", "#", "$", "|", ";", ".", ",", "_", "="]

    total_generadas = 0

    with open("aleatoria.txt", "w") as f:
        for i in range(cantidad):
            nombre = choice(nombres)
            apellido = choice(apellidos)
            palabra = choice(palabras)
            signo = choice(signos)

            f.write(nombre + apellido + str(randint(1000, 9999)) + "\n")
            f.write(nombre + signo + str(randint(1000, 9999)) + "\n")
            f.write(palabra + str(randint(1000, 9999)) + "\n")
            f.write(palabra + signo + str(randint(1000, 9999)) + "\n")

            total_generadas += 4
            print(f"Palabra {total_generadas} generada")

    print(Fore.GREEN + Style.BRIGHT + f"\n[+] Contraseñas guardadas en aleatoria.txt")
    print(Fore.CYAN + f"[+] Total de contraseñas generadas: {total_generadas}")
    main()

def telefono():
    os.system('cls')

    f = pyfiglet.Figlet(font='slant')
    ascii_art = f.renderText('GENPASS')
    print(Fore.BLUE + ascii_art)

    cantidad = int(input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la cantidad de contraseñas: "))
    print(Fore.YELLOW + Style.BRIGHT + "[+] Generando contraseña por número de teléfono", end="\n")
    with open("telefono.txt", "w") as f:
        for i in range(cantidad):
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

            print(f"Número {i+1} generado")

    print(Fore.GREEN + Style.BRIGHT + "[+] Contraseñas guardadas en telefono.txt")
    main()

def personalizada():
    os.system('cls')

    f = pyfiglet.Figlet(font='slant')
    ascii_art = f.renderText('GENPASS')
    print(Fore.BLUE + ascii_art)

    cantidad = int(input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la cantidad de contraseñas: "))

    user = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el nombre de la persona: ")
    lastname = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el apellido: ")
    fecha = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la fecha de nacimiento[ddmmaa]: ")
    user_num = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el número de teléfono: ")
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

    par = input(Fore.GREEN + Style.BRIGHT + "[+] ¿Tiene pareja [s/n]?: ")
    if par == "s":
        pareja = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el nombre de la pareja: ")
        lastname_par = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el apellido de la pareja: ")
        num_par = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el número de teléfono de la pareja: ")
        fecha_par = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la fecha de nacimiento de la pareja [ddmmaa]: ")
        nombres.append(pareja)
        apellidos.append(lastname_par)
        numeros.append(num_par)
        fechas.append(fecha_par)

    herm = input(Fore.GREEN + Style.BRIGHT + "[+] ¿Tiene hermanos [s/n]?: ")
    if herm == "s":
        hermano_1 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese nombre de hermano: ")
        lastname_her_1 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese apellido de hermano: ")
        hermano_2 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese nombre de hermano: ")
        lastname_her_2 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese apellido de hermano: ")
        nombres.extend([hermano_1, hermano_2])
        apellidos.extend([lastname_her_1, lastname_her_2])

    hijo = input(Fore.GREEN + Style.BRIGHT + "[+] ¿Tiene hijos [s/n]?: ")
    if hijo == "s":
        user_child = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese nombre de hijo: ")
        lastname_child = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese apellido de hijo: ")
        fecha_child = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese fecha de nacimiento de hijo [ddmmaa]: ")
        nombres.append(user_child)
        apellidos.append(lastname_child)
        fechas.append(fecha_child)

    mascota = input(Fore.GREEN + Style.BRIGHT + "[+] ¿Tiene mascota [s/n]?: ")
    if mascota == "s":
        mascota = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese nombre de mascota: ")
        fecha_mascota = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese fecha de adopción de mascota [ddmmaa]: ")
        nombres.append(mascota)
        fechas.append(fecha_mascota)

    signos = ["","+", "-", "*", "%", "!", "&", "@", "#", "$", ".", "_"]

    print(Fore.YELLOW + Style.BRIGHT + "[+] Generando contraseña personalizada...\n")
    total_generadas = 0
    with open("personalizada.txt", "w") as f:
        for i in range(cantidad):
            nombre = choice(nombres)
            apellido = choice(apellidos)
            fecha = choice(fechas)
            signo = choice(signos)
            numeros_sel = choice(numeros)

            f.write(nombre + apellido + fecha + "\n")
            f.write(apodo + signo + fecha +"\n")
            f.write(nombre + signo + fecha + "\n")
            f.write(numeros_sel + signo + apodo + "\n")
            f.write(numeros_sel + signo + nombre + "\n")

            total_generadas += 5
            print(f"Contraseña {total_generadas} generada")

    print(Fore.GREEN + Style.BRIGHT + f"\n[+] Contraseñas guardadas en personalizada.txt")
    print(Fore.CYAN + f"[+] Total de contraseñas generadas: {total_generadas}")
    main()

main()


