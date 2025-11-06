print("\n")
print("=" * 40)
print("FUNCIONES_PRACTICAS")
print("=" * 40)
print("\n")

# Funciones que devuelven números

# Funciones que devuelven un precio con IVA
"""
def calcular_iva(precio):
    
        calcula el IVA a partir de un precio. 
        devuelve el 21% de ese precio
   
    
    
    return precio * 0.21

"""
# Calcula el promedio de una lista de números.
# strip = permite borrar espacios extras 
# Suma todos los números de la lista y divide el resultado
# entre la cantidad de elementos.

# Args:
# numeros: Una lista de valores numéricos

# Returns:
# El promedio como valor flotante

# Ejemplo:
# >>> calcular_promedio([1, 2, 3, 4])
# 2.5

def calcular_iva(precio):
    return precio * 0.21

product_price = 100
calcular_iva(product_price)

# --- explicacion Alan ---

# funciones que devuelven números

# función que devuelve un precio con IVA

def calcular_iva(precio):
    """
    Calcula el IVA de un precio dado.

    Obtiene el 21 % de un precio.

    Args:
    precio: precio mayor que cero

    Returns:
    El IVA en punto flotante (float)

    Ejemplo:
    >>> calcular_iva(100)
    21

    """
    return precio * 0.21


microfono_precio = 100
microfono_precio_iva = calcular_iva(microfono_precio)
print(f"precio original: {microfono_precio}")
print(f"precio con IVA: {microfono_precio_iva}")

# OTRA FORMA

microfono_precio = 100
microfono_iva = calcular_iva(microfono_precio)
print(f"precio original: {microfono_precio}")
print(f"IVA del producto: {microfono_iva}")

print(f"Precio final: {microfono_precio + microfono_iva}")

# crear una f(x) que reciba un numero de inicio y un numero de fin
# Y devuelva una lista con numeros: [inicio, 2, 3, 4, 5, 6 ... fin]
# Lista: usar range()

def crear_lista_numeros(inicio, fin):
    return list(range(inicio, fin))

    
    
lista1 = crear_lista_numeros(1, 5)
print(lista1) # [1, 2, 3, 4, 5]

lista2 = crear_lista_numeros(1, 10)
print(lista2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista3 = crear_lista_numeros(5, 20)
print(lista3) # [5, hasta el 20]







            






















