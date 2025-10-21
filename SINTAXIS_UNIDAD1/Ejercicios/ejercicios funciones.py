"""
1.- Escribe una función que reciba dos números como parámetros y devuelva su suma.

"""
def sumar(a, b):
    return(a+b)

# Ejemplo de uso

resultado = sumar(4+6)
print(f"La suma es: {resultado} ")

"""
2.- Crea una función que determine si un número es par o impar.

"""
def es_par(numero):
    return numero % 2 == 0

# Ejemplo de uso

numero = 10
if es_par(numero):
    print(f"{numero} es par")
    
    
"""
3.- Escribe una función que calcule el factorial de un número dado.  
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Ejemplo uso

n = 5
print(f"El factorial de {n} es: ", factorial(n))

"""
4.- Escribe una función que reciba el radio de un círculo y devuelva su área.
Usa la fórmula: área= pi * r2

"""   
PI = 3.14159

def area_circulo(radio):
    return PI * radio ** 2

# Ejemplo uso:

radio = 4
print(f"El área del círculo con radio {radio} es: ", area_circulo(radio))



    
  
    


