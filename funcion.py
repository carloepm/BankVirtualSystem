""""
ACTIVIDAD
1. Crear un sistema de banco online con las siguientes caracteristicas:

a) Usuarios deben tener disponible el inicio de sesion con usuario y contraseña
b) Si el usuario coloca datos erroneos al iniciar sesion, el sistema debe bloquear su acceso al 3er intento fallido
c) El balance inicial en la cuenta de banco es de $2000.
d) El sistema debe permitir al usuario depositar, extraer, ver y transferir dinero.
c) El sistema debe disponer de un menu para realizar las operaciones.
"""

def autenticacion(username: str, password: str,) -> bool:
    """esta funcion autentica al usuario.
    
    argumentos:
            username (str): nombre de usuario
            password (str): contraseña
    retorno: 
            bool: True si el usuario es correcto, Falso si es invalido"""
    if username == "Carlos" or password == "carlos123":
        return True
    return False

def print_menu() -> None:
    """Esta funcion printea el menu principal"""
    print(
        """"
        Que operacion deseas realizar?
            1. Deposito
            2. Extraccion
            3. Ver saldo
            4. Transferir
            5. Salir
            """
    )

def deposito(balance: int) -> int:
    """ Esta funcion es para depositar dinero en la cuenta
    """   
    print("Cuanto quieres depositar?")
    depositar = int(input())
    balance += depositar
    print(f"Tu balance es {balance}")
    return balance

def extraccion(balance: int) -> int:
    """Esta funcion consiste en la extraccion de dinero de la cuenta
    """
    print("Cuanto dinero quieres extraer?")
    extraccion = int(input())
    balance -= extraccion
    print(f"tu balance es {balance}")
    return balance

def saldo(balance: int) -> int:
    """ Esta funcion simplemente expresa el saldo actual de la cuenta"""
    print(f"Tu balance es {balance}")
    return balance

def transferencia(balance: int) -> int:
    """Esta funcion es para realizar transferencias de una cuenta a otra
    """
    print("Cuanto quieres transferir?")
    transferencia = int(input())
    balance -= transferencia
    print(f"Tu balance es {balance}")
    return balance

def main():
    "aqui esta la funcion principal del programa."
auth_tries = 3
auth = False

while auth_tries > 0 and auth is False: 
    print("Inserte su nombre de usuario")
    username = input()
    print("Inserte su contraseña: ")
    password = input()

    auth = autenticacion(username, password)
    if auth is False:
       auth_tries -= 1
       print(f"Credenciales incorrectas, tienes {auth_tries} intentos mas")

if auth_tries == 0:
    print("Acceso bloqueado")
else:
    print("Bienvenido al sistema de banca online")
    

    balance = 2000
    menu = True
    while menu:
        print_menu()
        
        option = input()
        ops_menu = {
            "1": deposito,
            "2": extraccion,
            "3": saldo,
            "4": transferencia,
            "5": None,
            }
        
        if option in ops_menu:
            if option == "5":
                print("Adios")
                menu = False
            else: 
                balance = ops_menu[option](balance)
        else: 
            print(f"{option} es una opcion invalida")

if __name__ == "__main__":
    main()
