
"""
  Una clase es una plantilla o plano que define:

- Características (atributos): color, precio, raza, altura, id
- Comportamientos (métodos): arrancar, ladrar, iniciar sesión

  
    """

class Coche:
    # definimos atributos y métodos
    pass

mi_coche = coche()
coche_de_amigo = Coche()


"""
constructor: método especial que se ejecuta automáticamente
cuando creamos un nuevo objeto.

El método __init__ se ejecuta automáticamente al crear
el objeto y sirve para dejar el objeto con datos
iniciales.

self -> hace referencia a la variable principal, en el caso del ejemplo 
self, hace referencia a Persona.

    
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        

personal = Persona("Carla", 50) 



class Libro:
    # atributos: titulo, autor, numero páginas
    # métodos: abrir, leer, cerrar, subrayar
    pass
    def __init__(self, titulo, autor, isbn, numero_paginas, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.isbn = isbn
        self.abierto = False # si quieres abrir el libro
        self.pagina_actual = 0 # iniciamos en la pagina 0 (cerrado)
   
# libro_python = Libro()
book = Libro("shag", "Alanna", 1500) 

def abrir(self):
    self.abierto = True
    print(f"Se ha abierto {self.titulo}")

def cerrar(self):
    self.abierto = False
    print(f"Se ha cerrado {self.titulo}")

class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        

# Crear libros
libro1 = Libro("Marianela", "Benito Pérez Galdos", 200, "677854564556544")
libro2 = Libro("El Principito", "Antoine de Saint Exuperi", 180, "57756546456565656", False)

# verificar si está disponibles

print(f"{libro1.titulo} (libro1) está {'Disponible' if libro1.disponible else 'Prestado'}")
print(f"{libro2.titulo} (libro2) está {'Disponible' if libro2.disponible else 'Prestado'}")
   

# Crear objetos Producto
laptop = Producto("Portatil baratucho", 350) # El stock, será 0
# esto debido al valor por defecto que se ha colocado
teclado = Producto("Teclado mecánico", 80, 15)
# ahora es 15, porque se ha especificado

class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = (ancho + alto) * 2
        
# Crear objeto rectángulo
rectangulo = Rectangulo(5,3)
print(rectangulo.perimetro)

"""
Al definir valores predeterminados para los parámetros del 
constructor los convertimos en opcionales.

"""       
print("\n")
print("VALIDACION_ATRIBUTOS")
print("\n")


class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        
        # Validacion para que el saldo inicial sea como 
        # minimo 0 (no tenga valor -)
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        
        self.saldo = saldo_inicial
        
# Crear objetos cuenta
cuenta_ana = Cuenta("Ana", 1000)

# Esto lanzará un ValueError , el try/except es para controlar un error
try:
    cuenta_problemática = Cuenta("Juan", -500)
except ValueError as e:
    print(f"ERROR: {e}")
    
        
# crear la clase Producto
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
# Crear objetos Producto
laptop = Producto("Portátil baratucho", 350)
teckado = Producto("Teclado mecánico", 80, 15)
            
"""
===== CLASES Y OBJETOS, RELACIONES DE COMPOSICION==== 

* Uno a Uno (one to one):
    Un ciudadano español tiene un DNI. Ese DNI, 
    pertenece sólo a ese ciudadano.
    
"""
# Cuando estamos hablando de clases se coloca la clase, 
# que en este caso es ciudadano la primera letra con mayúscula
class Ciudadano:
    def __init__(self, id, nombre, apellido, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = None
        
class DNI:
    def __init__(self, id, numero):
        self.id = id
        self.numero = numero
        
# CREAR LOS OBJETOS

ciudadano1 = Ciudadano(7, Alanna, García, 42) 
dni1 = DNI(1, 346587935)   
    
# Asignar la referencia

ciudadano1.dni = dni1        

"""   
* Uno a Muchos (one to many):
    Una categoría puede tener muchos productos
    y un producto sólo puede perteneeer a esa categoría.
    
"""
class Categoria:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = productos[] # lista de productos

class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = Categoria # agregamos referencia
        
# Crear los objetos

categoria1 = Categoria(1, "Lacteos", "Productos derivados de la leche")
categoria2 = Categoria(2, "frutas", "Productos Frutales")
producto1 = Producto(1, "leche", 1.0)
producto2 = Producto(2, "Queso", 4.5)
producto3 = Producto(3, "yogurt",1.5)
producto4 = Producto(4, "Naranjas", 0.75)

"""    
* Muchos a Uno (Many to one):
    Muchos profesores trabajan en 1 departamento y ese dpto.
    puede tener muchos profesores.
"""
class Departamento:
    def __init__(self, id, nombre, ubicacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion

class Profesor:
    def __init__(self, id, nombre, especialidad, departamento):
        self.id = id
        self.nombre = nombre
        self.especialidad = especialidad
        self.departamento = departamento
        
# Crear objeto

depto1 = Departamento(1, "matemáticas", "Edificio 1A")
profesor1 = Profesor(1, "Tornasol", "Topología", depto1)
profesor2 = Profesor(1, "Andrade", "Biología", depto1)        

"""    
*Muchos a Muchos (many to many):
    Muchos estudiantes pueden tener muchas asignaturas
    cada asignatura puede tener muchos estudiantes
        
"""
class Estudiante:
    def __init__(self, id, nombre, edad):
        self.id = id
        self. nombre = nombre
        self.edad = edad
        self.asignaturas = [] # Lista de asignaturas
        
class Asignatura:
    def __init__(self, id, nombre, creditos):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.estudiantes = [] # Lista de estudiantes
        
class EstudianteAsignatura:
    def __init__(self, estudiante_id, asignatura_id, nota):
        self.estudiante_id = estudiante_id
        self.asignatura_id = asignatura_id
        self.nota = nota
        
# Crear objeto

estudiante1 = Estudiante(1, "Anna", 20)  
estudiante2 = Estudiante(2, "Pépe", 22)
asignatura1 = Asignatura(1, "matemáticas", 6)
asignatura2 = Asignatura(2, "Criptografía", 3)

# Relaciones

estudiante1.asignaturas = [asignatura1, asignatura2]
estudiante2.asignaturas = [asignatura1]

asignatura1.estudiantes = [estudiante1, estudiante2]
asignatura2.estudiantes = [estudiante1]    
        
relaciones = [
EstudianteAsignatura(1, 1, 8.5),
EstudianteAsignatura(1, 2, 6.0),
EstudianteAsignatura(2, 1, 7.5)
]









































