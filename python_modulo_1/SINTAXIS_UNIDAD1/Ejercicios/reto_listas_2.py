print("\n")
print("=" * 40)
print("LISTAS")
print("=" * 40)
print("\n")

"""
Crea una función llamada filtrar_mayores que reciba dos parámetros: 
una lista de números enteros y un valor umbral. 
La función debe devolver una nueva lista que contenga 
solo los números de la lista original que sean mayores que el valor umbral.

Por ejemplo:

Si llamamos filtrar_mayores([5, 10, 15, 20], 12) debe devolver [15, 20]
Si llamamos filtrar_mayores([1, 2, 3], 5) debe devolver [] (lista vacía)
Puedes empezar creando una función que reciba los dos parámetros 
y luego utilizar un bucle para recorrer la lista original 
y añadir a una nueva lista solo los elementos que cumplan la condición. 
    
"""
def filtrar_mayores(lista, umbral):
    if lista > umbral:
    numero = list[2, 4, 6, 8, 10, 12]
    umbral = [3, 5]
    return [numero for numero in lista if numero > umbral]
        
    
    """
    Filtra los números de una lista que son mayores que un valor umbral dado.
    
    Args:
        lista (list): Lista de números enteros a filtrar.
        umbral (int): Valor umbral para la comparación.
        
    Returns:
        list: Nueva lista con los números mayores que el umbral.
    """
    resultado = []
    
    # TODO: haz aquí el código de la función:
    
    return resultado

# Ejemplos de uso
if __name__ == "__main__":
    print(filtrar_mayores([5, 10, 15, 20], 12))  # Debe devolver [15, 20]
    print(filtrar_mayores([1, 2, 3], 5))         # Debe devolver [] (lista vacía)




