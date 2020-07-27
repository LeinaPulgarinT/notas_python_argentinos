"""
def my_function(mensaje, greeting = 'Hola', age = 22, confirm = True):
    print(f'{greeting}, tengo {age} y mi respuesta es {confirm}' )
# Si por ejemplo yo quiero pasarle a mi funcion los argumentos de los parametros en desorden:
my_function('holis', confirm = False)
my_function(confirm = False, greeting = 'Holisss') # no necesite pasar el argumento de la edad ya que le puse uno por defecto, entonces ese argumento es opcional solo si quiero cambiar el por default que le di.
my_function(confirm = False, greeting = 'Holisss', 'hola mami') # Esto es un error garrafal pues, los parametros que son oligatorios no se pueden pasar despues de los opcionales
"""
"""
def my_function(greeting = 'Hola', age = 22, confirm = True, mensaje):
    print(f'{greeting}, tengo {age} y mi respuesta es {confirm}' )
my_function('Holisss',56 ,False, 'hola mami') # esto no se puede hacer por que los argumentos que no estan predeterminados deben de ir primero y luego los que si tienen valores por default, si lo hago asi me va salir el siguiente error:
# SyntaxError: non-default argument follows default argument
"""
# Palabras claves como argumentos en  los diccionarios:
"""
def venta_de_queso(tipo, *argumentos, **palabras_claves):
    print('__¿Tiene', tipo, '?')
    print('__Lo siento, nos quedamos sin', tipo)
    for arg in argumentos:
        print(arg)
    print('_ ' * 40)
        #claves = sorted(palabras_claves.keys())
    claves = sorted(palabras_claves.items())
    for c in claves:
        print(c, ':', palabras_claves[c])

venta_de_queso('Limburger', 'Es muy liquido, sr.', 
                'Realmente es muy muy liquido, sr.',
                puesto = 'venta de queso colombiano',
                cliente = 'Leina Pulgarin', 
                vendedor = 'camila alvarez')
"""

#Desempaquetando argumentos:
def loro(tension, estado='rostizado', accion='explotar'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.", end=' ')
    print("Está", estado, "!")
d = {"tension": "cinco mil", "estado": "demacrado", "accion": "VOLAR"}
#loro(**d)

def person(name, lastname = 'Pulgarin', age = 22, likes = 'Python'):
    print(f"Miss {name} {lastname}, loves to program in {likes}, to her's {age} years ")
parameters = {'name': 'Leina', 'lastname': 'Tamayo', 'likes': 'Django'}
person(**parameters)