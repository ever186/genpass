import os
from random import randint, choice
from colorama import Fore, Style
import pyfiglet

os.system('cls' if os.name == 'nt' else 'clear')

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
    os.system('cls' if os.name == 'nt' else 'clear')

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

    generadas = set()  # conjunto para evitar repeticiones

    with open("aleatoria.txt", "w") as f:
        while len(generadas) < cantidad:  # hasta llegar a la cantidad pedida
            nombre = choice(nombres)
            apellido = choice(apellidos)
            palabra = choice(palabras)
            signo = choice(signos)

            posibles = [
                nombre + apellido + str(randint(1000, 9999)),
                nombre + signo + str(randint(1000, 9999)),
                palabra + str(randint(1000, 9999)),
                palabra + signo + str(randint(1000, 9999))
            ]

            for p in posibles:
                if len(generadas) >= cantidad:
                    break
                if p not in generadas:
                    f.write(p + "\n")
                    generadas.add(p)
                    print(f"Contraseña {len(generadas)} generada", end="\r")

    print(Fore.GREEN + Style.BRIGHT + f"\n[+] Contraseñas guardadas en aleatoria.txt")
    print(Fore.CYAN + f"[+] Total de contraseñas generadas: {len(generadas)}")
    main()

def telefono():
    os.system('cls' if os.name == 'nt' else 'clear')

    f = pyfiglet.Figlet(font='slant')
    ascii_art = f.renderText('GENPASS')
    print(Fore.BLUE + ascii_art)

    cantidad = int(input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la cantidad de contraseñas: "))
    print(Fore.YELLOW + Style.BRIGHT + "[+] Generando contraseñas por número de teléfono...\n")

    generadas = set()

    with open("telefono.txt", "w") as f:
        while len(generadas) < cantidad:
            prefijos = ["300", "301", "302", "303", "304", "305",
                        "310", "311", "312", "313", "314", "315",
                        "316", "317", "318", "319", "320", "321",
                        "322", "323", "324"]
            numero = choice(prefijos) + str(randint(2000000, 9999999))

            if numero not in generadas:
                f.write(numero + "\n")
                generadas.add(numero)
                print(f"Número {len(generadas)} generado", end="\r")

    print(Fore.GREEN + Style.BRIGHT + f"\n[+] Contraseñas guardadas en telefono.txt")
    print(Fore.CYAN + f"[+] Total de contraseñas generadas: {len(generadas)}")
    main()

def personalizada():
    os.system('cls' if os.name == 'nt' else 'clear')

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

    if input(Fore.GREEN + Style.BRIGHT + "[+] ¿Tiene pareja [s/n]?: ") == "s":
        pareja = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el nombre de la pareja: ")
        lastname_par = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el apellido de la pareja: ")
        num_par = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese el número de teléfono de la pareja: ")
        fecha_par = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese la fecha de nacimiento de la pareja [ddmmaa]: ")
        nombres.append(pareja)
        apellidos.append(lastname_par)
        numeros.append(num_par)
        fechas.append(fecha_par)

    if input(Fore.GREEN + Style.BRIGHT + "[+] ¿Tiene hermanos [s/n]?: ") == "s":
        hermano_1 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese nombre de hermano: ")
        lastname_her_1 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese apellido de hermano: ")
        hermano_2 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese nombre de hermano: ")
        lastname_her_2 = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese apellido de hermano: ")
        nombres.extend([hermano_1, hermano_2])
        apellidos.extend([lastname_her_1, lastname_her_2])

    if input(Fore.GREEN + Style.BRIGHT + "[+] ¿Tiene hijos [s/n]?: ") == "s":
        user_child = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese nombre de hijo: ")
        lastname_child = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese apellido de hijo: ")
        fecha_child = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese fecha de nacimiento de hijo [ddmmaa]: ")
        nombres.append(user_child)
        apellidos.append(lastname_child)
        fechas.append(fecha_child)

    if input(Fore.GREEN + Style.BRIGHT + "[+] ¿Tiene mascota [s/n]?: ") == "s":
        mascota = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese nombre de mascota: ")
        fecha_mascota = input(Fore.GREEN + Style.BRIGHT + "[+] Ingrese fecha de adopción de mascota [ddmmaa]: ")
        nombres.append(mascota)
        fechas.append(fecha_mascota)

    signos = ["","+", "-", "*", "%", "!", "&", "@", "#", "$", ".", "_"]

    print(Fore.YELLOW + Style.BRIGHT + "[+] Generando contraseñas personalizadas...\n")
    generadas = set()

    with open("personalizada.txt", "w") as f:
        while len(generadas) < cantidad:
            nombre = choice(nombres)
            apellido = choice(apellidos)
            fecha = choice(fechas)
            signo = choice(signos)
            numeros_sel = choice(numeros)

            posibles = [
                nombre + apellido + fecha,
                apodo + signo + fecha,
                nombre + signo + fecha,
                numeros_sel + signo + apodo,
                numeros_sel + signo + nombre
            ]

            for p in posibles:
                if len(generadas) >= cantidad:
                    break
                if p not in generadas:
                    f.write(p + "\n")
                    generadas.add(p)
                    print(f"Contraseña {len(generadas)} generada", end="\r")

    print(Fore.GREEN + Style.BRIGHT + f"\n[+] Contraseñas guardadas en personalizada.txt")
    print(Fore.CYAN + f"[+] Total de contraseñas generadas: {len(generadas)}")
    main()

main()




