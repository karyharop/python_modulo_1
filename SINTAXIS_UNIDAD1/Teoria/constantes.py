print("\n")
print("=" * 40)
print("CONSTANTES")
print("=" * 40)
print("\n")


#LISTA, ESTRUCTURA DE DATOS MODIFICABLES, PUEDES TENER VALORES DUPLICADOS
#mi_lista = [1, 2, 3, 4, 5]
#TUPLAS, ESTRUCTURA DE DATOS NO MODIFICABLES
#mi_tupla = (1, 2, 3, 4, 5)
#CONJUNTOS, ESTRUCTURA DE DATOS NO MODIFICABLES, NO PERMITE VALORES DUPLICADOS
#mi_conjunto = {1, 2, 3, 4, 5}
#ARRAYS, ESTRUCTURA DE DATOS MODIFICABLES, PERMITE VALORES DUPLICADOS, DEBEN SER DATOS DEL MISMO TIPO
# LOS ARRAYS SE USAN MUCHO EN CIENCIA DE DATOS
#mi_array = array.array('i', [1, 2, 3, 4, 5]) # 'i' indica que son enteros
#DICCIONARIOS, ESTRUCTURA DE DATOS MODIFICABLES, PERMITE VALORES DUPLICADOS, SE USAN PARA ALMACENAR PARES DE VALOR-CLAVE
#mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2'}, TAMBIEN LLAMADOS SETS DE DATOS
#LOS DICCIONARIOS SON MUY USADOS EN PROGRAMACION WEB, PARA ALMACENAR DATOS DE USUARIOS

print("\n")
print("=" * 40)

PI = 3.14159  # Constante matemática
VELOCIDAD_LUZ = 299792458  # en metros por segundo
GRAVEDAD_TIERRA = 9.81  # en m/s^2
DIAS_SEMANA = 7  # Días en una semana
USER_DEFAULT = "Usuario"

# Si qiueres mantener las constantes, debes añadirlas en un archivo aparte
# y llamarlas desde ahí, para que no se modifiquen

print("\n")
print("=" * 40)
print("OPERADORES ARITMÉTICOS")
print("=" * 40)
print("\n")

precio_manzanas = 3
precio_naranjas = 4
total_frutas = precio_manzanas + precio_naranjas
print(f"Total de la compra: {total_frutas} euros")

dinero_entregado = 20
dinero_producto = 13
cambio = dinero_entregado - dinero_producto
print(f"Su cambio es: {cambio} euros")

precio_unitario = 5
cantidad = 3
precio_total = precio_unitario * cantidad
print(f"Precio por {cantidad} unidades: {precio_total} euros")
precio_total /= 2  # Aplica un descuento del 50%

pizza = 8 / 2
print(f"8 / 2 = {pizza}")

horas_totales = 90
horas_por_dia = 24
dias_completos = horas_totales // horas_por_dia
print(f"Días completos en 90 horas: {dias_completos} días")

horas_restantes = horas_totales % horas_por_dia
print(f"Horas restantes después de días completos: {horas_restantes} horas")
print("\n")
print("=" * 40)

lado = 4
area_cuadrado = lado ** 2
print(f"Área del cuadrado es: {area_cuadrado} unidades cuadradas")

numero = 27
raiz_cubica = numero ** (1/3)
print(f"La raíz cúbica de {numero} es: {raiz_cubica}")

print("=" * 40)

resultado = 0.2 + 0.1
it  (f"El resultado de 0.2 + 0.1 es: {resultado}")
#me falta escribir print(resultado)

print("\n")
print("=" * 40)
print("OPERADORES EN COMPARACION")
print("=" * 40)
print("\n")


precio_producto_a = 15
precio_producto_b = 10

es_mas_barato_ = precio_producto_b < precio_producto_a
print(f"¿El producto B es más barato que el A? {es_mas_barato}")

print("\n")
print("=" * 40)
print("OPERADORES LÓGICOS")# SON PARA EVALUAR OPERACIONES BOOLEANAS
print("=" * 40)
print("\n")

NOT # NEGACION
AND # Y
OR  # O, es más permisivo que el AND
XOR # O EXCLUSIVO

print("\n")
print("=" * 40)

ingresos_suficientes = True
buen_historial_crediticio = True

aprobacion_prestamo = ingresos_suficientes and buen_historial_crediticio
print(f"¿El préstamo fue aprobado? {aprobacion_prestamo}")

es_socio = False
tiene_invitacion = True

puedo_entrar_evento = es_socio or tiene_invitacion
print(f"¿Puedo entrar al evento? {puedo_entrar_evento}")

disponible = False
no_disponible = not disponible


