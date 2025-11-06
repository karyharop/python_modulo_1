
print("\n")
print("=" * 40)
print("IF ELIF ELSE")
print("=" * 40)
print("\n")

#Crea un programa que solicite al usuario su edad mediante input() y 
# determine en qué categoría se encuentra según los siguientes criterios:

#Si la edad es menor que 13 años: "Eres un niño"
#Si la edad está entre 13 y 17 años (inclusive): "Eres un adolescente"
#Si la edad está entre 18 y 64 años (inclusive): "Eres un adulto"
#Si la edad es 65 años o mayor: "Eres un adulto mayor"
#El programa debe mostrar el mensaje correspondiente usando print(). 
# Recuerda que input() devuelve una cadena de texto, 
# por lo que necesitarás convertir la entrada a número entero usando int().

print("=" * 40)

print("BASE_DATOS_USUARIOS")

print("=" * 40)

#Estructura tu código de la siguiente manera:

#Solicita la edad al usuario
#Convierte la entrada a entero
#Usa una estructura if-elif-else para evaluar la edad
#Muestra el mensaje correspondiente
#Ejemplo de ejecución:

#Si el usuario introduce 15, debe mostrar: "Eres un adolescente"
#Si el usuario introduce 25, debe mostrar: "Eres un adulto"


# Solicitar la edad al usuario


#forma concisa
# edad = int(int(input""inrtroduce tu edad: "))


# Convertir la entrada a entero
edad = int(edad_input)
# Evaluar la edad usando if-elif-else
if edad < 13:
    print("Eres un niño.")
elif edad <= 17:
# elif edad >= 13 and <= 17
    print("Eres un adolescente.")
elif edad <= 64:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor")

# Mostrar el mensaje correspondiente

print(edad)



# De esta forma lo ha hecho Reyes...

edad_usuario = input("Dame la edad del usuario: ")

try:
# Convertir la entrada a entero
edad = int(edad_usuario)

# Evaluar la edad usando if-elif-else
if edad >= 65:
mensaje = "adulto mayor"
elif edad >= 18:
mensaje = "adulto"
elif edad >= 13:
mensaje = "adolescente"
elif edad > 0:
mensaje = "niño"
else:
mensaje = "error. Por favor, escriba un número positivo"

# Mostrar el mensaje correspondiente
print(f"Eres un {mensaje}" if edad>0 else f"Es un {mensaje}")

except ValueError:
print("Por favor, introduce un número para la edad.")

