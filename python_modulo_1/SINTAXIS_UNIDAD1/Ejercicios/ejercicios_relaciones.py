print("\n")
print("=" * 20)
print("ONE TO ONE")
print("=" * 20)
print("\n")

print("=== EJERCICIO: RELACIÓN EMPLEADO-TARJETA CORPORATIVA ===\n")

# 1. Crear la clase Empleado con los atributos: id, nombre, cargo, salario
# El atributo 'tarjeta' debe inicializarse como None
class Empleado:
    def __init__(self, id, nombre, cargo, salario):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.tarjeta = None
        
# 2. Crear la clase TarjetaCorporativa con los atributos: id, numero, fecha_emision, empleado_id
class TarjetaCorporativa:
    def __init__(self, id, numero, fecha_emision, empleado_id):
        self.id = id
        self.numero = numero
        self.fecha_emision = fecha_emision
        self.empleado_id = empleado_id # FK (clave foránea) hacia empleado
         

print("=== CREANDO OBJETOS ===")

# 3. Crear un empleado con id: 1, nombre: Alba Motacilla, cargo: Desarrolladora, salario: 45000
empleado1 = Empleado(1, "Alba Motacilla", "Desarrolladora", 45000)

# 4. Crear una tarjeta corporativa con id: 1, número: TC001, fecha de emisión: 2025-01-15, id de empleado: 1
tarjeta1 = TarjetaCorporativa(1, "TC001", "2025-01-15", 1)

print("Los datos de la tarjeta corporativa son: {tarjetacorporativa1}")

# 5. Asignar la tarjeta al empleado (relación one-to-one)
empleado1.tarjeta1 = tarjeta1
print(f"Empleado: {empleado1.nombre}")
print(f"Numero de Tarjeta: {empleado1.tarjeta.numero}")
print(f"Fecha de Emisión: {empleado1.tarjeta.fecha_emision}")
print(f"Fecha de Emisión: {tarjeta1.fecha_emision}")

# 6. Imprimir información del empleado y su tarjeta
# Hay para mostrar:
print(f"El nombre del empleado es: {self.nombre}")
print(f"El numero de tarjeta del empleado es: {tarjetacorporativa1}")

# - Nombre del empleado
# - Número de tarjeta


print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-one
print(f"El empleado {empleado1.tarjetacorporativa1} posee tarjeta corporativa")



print("\n")
print("=" * 20)
print("MANY TO ONE")
print("=" * 20)
print("\n")

print("=== EJERCICIO: RELACIÓN HABITACIONES-HOTEL ===\n")

# 1. Crear la clase Hotel con los atributos: id, nombre, direccion, estrellas

class Hotel:
    def __init__(self, id, nombre, direccion, estrellas):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.estrellas = estrellas
        

# 2. Crear la clase Habitacion con los atributos: id, numero, tipo, precio y hotel
class Habitacion:
    def __init__(self, id, numero, tipo, precio, hotel):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.hotel = hotel

print("=== CREANDO OBJETOS ===")

# 3. Crear un hotel con id: 1, nombre: Hotel Carbonero, dirección: Plaza Parus Mayor 123, estrellas: 4

hotel1 = Hotel(1, "Hotel Carbonero", "Plaza Parus Mayor 123", 4)

# 4. Crear tres habitaciones:
# - id: 1, número: 101, tipo: Individual, precio: 80, hotel: Hotel Carbonero
# - id: 2, número: 102, tipo: Doble, precio: 120, hotel: Hotel Carbonero
# - id: 3, número: 103, tipo: Suite, precio: 200, hotel: Hotel Carbonero
habitacion1 = Habitacion(1, 101, "Individual1", 80, hotel1)
habitacion2 = Habitacion(2, 102, "Doble", 120, hotel1)
habitacion3 = Habitacion(3, 103, "Suite", 200, hotel1)


print("=== ESTABLECIENDO RELACIÓN ===")

# 5. Imprimir información del hotel y sus habitaciones Hay que mostrar:
print(f"nombre{hotel1.nombre}, Estrellas {hotel1.estrellas}")
print(f"nombre{habitacion1.hotel1.nombre}, Estrellas: {habitacion1.hotel.estrellas}")



print("\n=== RESULTADO FINAL ===")
# 6. Mostrar un mensaje confirmando la relación many-to-one

print(f"La habitación {habitacion1.numero} pertenece al hotel {habitacion1.hotel.nombre}")

print("\n")
print("=" * 20)
print("ONE TO MANY")
print("=" * 20)
print("\n")

print("=== EJERCICIO: RELACIÓN CARPETA-ARCHIVOS ===\n")

# 1. Crear la clase Carpeta con los atributos: id, nombre, fecha_creacion
# El atributo 'archivos' debe inicializarse como una lista vacía
class Carpeta:
    def __init__(self, id, nombre, fecha_creacion):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion
        self.archivos = []
        

# 2. Crear la clase Archivo con los atributos: id, nombre, extension, tamaño, carpeta_id
class Archivo:
    def __init__(self, id, nombre, extension, tamaño, carpeta_id):
        self.id = id
        self.nombre = nombre
        self.extension = extension
        self.tamaño = tamaño
        self.carpeta_id = carpeta_id
        
        
print("=== CREANDO OBJETOS ===")

# 3. Crear una carpeta con id: 1, nombre: Proyecto Aviberico, fecha de creación: 2025-01-15
carpeta1 = Carpeta(1, "Proyecto Aviberico", "2025- 01- 15")

# 4. Crear tres archivos:
# - id: 1, nombre: main, extensión: py, tamaño: 1024, id de carpeta: 1
# - id: 2, nombre: config, extensión: json, tamaño: 512, id de carpeta: 1
# - id: 3, nombre: readme, extensión: md, tamaño: 256, id de carpeta: 1

archivo1 = Archivo(1, "Main", "py", 1024, 1)
archivo2 = Archivo(2, "Config", "json", 512, 1)
archivo3 = Archivo(3, "readme", "md", 256, 1)


print("=== ESTABLECIENDO RELACIÓN ===")
# carpeta1, va en minuscula porque es una variable
# 5. Agregar los archivos a la carpeta (relación one-to-many)
carpeta1.archivos.append(archivo1)
carpeta1.archivos.append(archivo2)
carpeta1.archivos.append(archivo3)

print("=== VERIFICANDO RELACIÓN ===")

# 6. Imprimir información de la carpeta y sus archivos
# Hay que mostrar:
# - Nombre de la carpeta
# - Número total de archivos
# - Lista de archivos con sus detalles

print(f"Nombre de la carpeta: {carpeta1.nombre}")
print(f"Numero total de Archivos: {len(carpeta1.archivos)} archivos")
print(f"Fecha de creación: {carpeta1.fecha_creacion}")
print("ARCHIVOS:")
for archivo in carpeta1.archivos:
    print(f"- {archivo.nombre}.{archivo.extension} - {archivo.tamaño} bytes")



print("\n=== RESULTADO FINAL ===")
# 7. Mostrar un mensaje confirmando la relación one-to-many
print(f"La carpeta {carpeta1.nombre} tiene {len(carpeta1.archivos)} archivos")


