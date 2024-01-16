""""
ACTIVIDAD
1. Crear un sistema de banco online con las siguientes caracteristicas:

a) Usuarios deben tener disponible el inicio de sesion con usuario y contraseña
b) Si el usuario coloca datos erroneos al iniciar sesion, el sistema debe bloquear su acceso al 3er intento fallido
c) El balance inicial en la cuenta de banco es de $2000.
d) El sistema debe permitir al usuario depositar, extraer, ver y transferir dinero.
c) El sistema debe disponer de un menu para realizar las operaciones.
"""



auth_tries = 3
auth = False

while auth_tries > 0 and auth is False: 
    print("Inserte su nombre de usuario")
    username = input()
    print("Inserte su contraseña: ")
    password = input()

    if username == "Carlos" and password == "carlos123":
        auth = True
    else: 
        auth_tries -= 1
        print(f"Datos incorrectos, te quedan {auth_tries} intentos")

if auth_tries == 0:
    print("Acceso bloqueado")



if auth: 
    print("Bienvenido al sistema de banca online")
    balance = 2000
    menu = True
    while menu:

            print("Que quieres realizar?")
            print("1. Depositar")
            print("2. Extraer")
            print("3. Ver saldo")
            print("4. Transferir")
            print("5. Salir")
    
            option = input()
            
            if option == "1":
                print("Cuanto quieres depositar?")
                deposito = int(input())
                balance += deposito
                print(f"Tu balance es {balance}")
            elif option == "2":
                print("Cuanto quieres extraer?")
                extracion = int(input())
                balance -= extracion
                print(f"Tu balance es {balance}")
            elif option == "3":
                print(f"Tu balance es {balance}")
            elif option == "4":
                print("Cuanto quieres transferir?")
                transferencia = int(input())
                balance -= transferencia
                print(f"Tu balance es {balance}")
            elif option == "5":
                print("Adios")
                menu = False
            else:
                print(f"{option} no es una opcion valida")
                
    
