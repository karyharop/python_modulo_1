print("\n")
print("=" * 40)
print("LISTAS")
print("=" * 40)
print("\n")

def filtrar_mayores(lista, umbral):
    """
    Filtra los números de una lista que son mayores que un valor umbral dado.
    
    Args:
        lista (list): Lista de números enteros a filtrar.
        umbral (int): Valor umbral para la comparación.
        
    Returns:
        list: Nueva lista con los números mayores que el umbral.
    * Se inicia una lista vacia para guardar los numeros que cumplan la condición.
    
    """
    
    resultado = []
    
    # TODO: haz aquí el código de la función:
    # Recorremos cada numero de la lista
    # Una forma de hacerlo, la más simple:
    for n in lista: 
        # Comprobamos si el mumero es mayor al umbral
        if n > umbral:
            # Si se cumple el if, se añade a la lista de resultados
            resultado.append(n)
    
    return resultado

# Otra forma de hacerlo con comprension de listas

def filtrar_mayores(lista, umbral):
    return [n for n in lista if n > umbral]   
    
# Ejemplos de uso
if __name__ == "__main__":
    print(filtrar_mayores([5, 10, 15, 20], 12))  # Debe devolver [15, 20]
    print(filtrar_mayores([1, 2, 3], 5))         # Debe devolver [] (lista vacía)

