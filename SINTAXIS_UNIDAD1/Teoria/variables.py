# VARIABLES <- SON DATOS CON NOMBRE
# UNA VARIABLE ES UN NOMBRE QUE APUNTA A UN DATO
print("\n")
print("=" * 40)
print("VARIABLES")
print("=" * 40)
print("\n")

edad = 25
nombre = "Jacinta Dorotea"
altura = 1.74
es_estudiante = True

x = y = z
print = (f"variables: x={x}, y={y}, z={z}")
      
nombre, edad, altura = """Jacinta Dorotea""", 25, 1.74
print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}")

print("\n")
print("=" * 20)


a = 5
b = 10
a, b = b, a  # Intercambio de valores

a, b = b, a  # Intercambio de valores
print(f"a: {a}, b: {b}")

print("\n")
print("=" * 20)

contador = 0
print(f"Contador: {contador}")

contador -= 2  # Incrementa el contador en 2
print(f"Contador después de restar 2: {contador}")

precio = 100
precio *= 1.21  # Aplica un aumento del 21%
print(f"Precio: {precio}")

precio /= 2
print(f"precio: {precio}")

edad = 10
Edad = 20
EDAD = 30

# Hay que respetar como se escribe la variable, porque la coge como en este caso 3 
# variables diferentes

print("\n")
print("=" * 20)

#__snake_case <- señala a las variables con guion bajo y minúsculas

#__pascal_case <- señala a las variables con mayúsculas en cada palabra
#como se usa en PseInt
#__camelCase <- señala a las variables con mayúsculas en 
# cada palabra excepto la primera palabra


print("\n")
print("=" * 40)
print("AMBITO LOCAL Y GLOBAL")
print("=" * 40)
print("\n")

mensaje = "Hola MUNDO"

print(mensaje)  # Accede a la variable global

contador_global = 100 # Variable global
print(f"Contador global antes de la función: {contador_global}") #imprime 100

# Def <-- define una función

def incrementar():
    global contador_global  # Indica que se usará la variable global
    contador = 0  # Variable local
    print(f"Contador Local + 1: {contador}")
    contador += 1
    print(f"Contador Local después de incrementar: {contador}")
    
    incrementar() # imprime: "contador local: 1"
    
    print(f"Contador global dentro de la función: {contador_global}") #imprime 100
    
# Siempre que queramos usar una variable global dentro de una función, 
# hay que poner global antes de usarla, si no, la función crea una variable local

# incrementar()  # Llama a la función

# def funcion(): #aqui llama a la funcion, ejemplo (1), si no encuntra la variable, se va a la 
    # fucion siguiente. 
    
    def funcion():
        variable: 1
        def funcion_secundaria():
        print(variable)  
    



