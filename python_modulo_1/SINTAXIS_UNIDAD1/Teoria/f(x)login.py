print("\n")
print("=" * 40)
print("F(X)s LOGIN")
print("=" * 40)
print("\n")

def login(email, password):
    email_valido = "admin@gmail.com"
    password_valida = "1234"
    
# Verificar si el mail y el password coinciden

if email == email_valido:
    return True
else:
    return False


login("admin@gmail.com", "abcd1234") # False

login("admin@gmail.com", "1234") # True

login("usuario@gmail.com", "1234") # False

# Un ejemplo

if login("admin@gmail.com", "1234"):
    pass


# LOGIN CON NÚMERO MÁXIMO DE INTENTOS

# Aquí podemos crear una aplicación de consola
# que pida al usuario email y password,
# si falla tres veces detiene el programa y no deja continuar
# si acierta le deja usar la aplicación

valid_email = "Anna@gmail.com"
valid_password = "A_12"
max_intentos = 3

def login1(valid_email, valid_password):
# bucle for para máximo 3 intentos fallidos para verificar mail y contraseña
# leer por input el email y password
    for intento in range (1, max_intentos + 1) # 1, 2, 3,
    email = input("introduce email: "). strip()
    password = input("Introduce password: "). strip()
    
    if email == valid_email and password == valid_password
        return True
    
    intentos_restantes = max_intentos - intento # 3 - 1 = 2, 3 - 2 = 1, 3 - 3 = 0
    if intentos_restantes > 0:
        print(f"Credenciales incorrectas, te quedan {intentos_restantes} intentos")
    else:
        print("Has agotado todos los intentos, adiós.")
        sys.exit(1) # corta de forma definitiva el programa


if login():
    opcion = elegir_opcion()
    
    
def login_2():
    pass

def elegir_opcion():
    print("")
opcion = input()
return opcion
    
if login_1():
        opcion = elegir_opcion()
        print(f"Has elegido la opcion {opcion}")
        
# hacer algo en base a la opcion elegida por el usuario:    

# if...
# elif...
# elif...
# else


if login_1():
    while True:
        print("Bienvenido/a a la aplicación. Opciones disponibles: 1 - ver productos, 2 - crear producto, 3 - terminar el programa.")
opcion = input("Introduce una opción: ")
print(f"Has elegido la opcion {opcion}")

if opcion == "1":
    print("1")
elif opcion == "2":
    print("2")
elif opcion == "3" or opcion == "salir":
    print("saliendo...")
    break
else:
    print("opción incorrecta.")
    


