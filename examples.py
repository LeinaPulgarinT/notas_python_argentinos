# a = ['Maria', 'tenia', 'un' 'corderito']
# for i in range(len(a)):
  #  print(i, a[i])
"""
for n in range(2, 10):
  #print(n)
  for x in range(2, n):
    if n % x == 0:
      print(n)
      break
    else:
      print()
  print()
"""
# Este ciclo se comporta de esta forma: para poder que se me ejecute el else, de mi for necesito que en las subiteraciones, es decir en cada una de las iteraciones de mi ciclo anidado en ningun momento entre al condicional, por que si entra al condicional entonces se me ejecuta el break, entonces con un solo brak que se me ejecute entonces eso no me va permitir que se ejecute el else, entonces no me entra al else, para que ese else se ejecute tiene que ser que el break en esa iteracion no se de, es decir no se cumpla el condicional.

# declaracion continue:
"""
for num in range(2, 10):
  if num % 2 == 0:
    print('Encontré un número par', num)
    continue
  print('Encontré un número', num)
  """
# En el ejemplo anterior lo que hace el continue es que si se me cumple la condicion, quiere decir que ya encontre lo que estaba buscando, entonces el continue le dice al ciclo que como ya encontro lo que queria continue con la siguiente iteracion, que se me salte a la siguiente interacion

# Valores por omision:
"""
def f(a, L = []):
  L.append(a)
  return L 
print(f(1))
print(f(2))
print(f(3))

def f(a, L = None):
  if L is None:
    L = []
  L.append(a)
  return L
print(f(1))
print(f(2))
print(f(3))
"""
# Diferentes llamados a funciones:
"""
def loro(tension, estado = 'muerto', accion = 'explotar', tipo = 'Azul Nordico'):
  print("-- Este loro no va a", accion, end=' ')
  print("si le aplicás", tension, "voltios.")
  print("-- Gran plumaje tiene el", tipo)
  print("-- Está", estado, "!")
#loro(1000)
#loro('un millon', 'depojado de la vida', 'saltar')
#loro('un millon', estado = 'depojado de la vida')

# tipos de llamadas que son invalidas: 
#loro(tension = 5.0, estado = 'muerto')
#loro(100, tension = 200)
loro(actor = 'Juan Garau')
"""
# Pasar argumentos con tuplas, solo podria pasar los argumentos de la siguiente forma:
"""
def muchos_items(archivo, separador, *args):
  print(archivo)
  print(separador)
  #a= args
  print(args)
# Asi: es decir pasando solo los parametros que estan definidos:
muchos_items(separador = 'o', archivo = 'holis') # ó
# Asi:
muchos_items(1, 2, 3, 4)
# si por ejemplo quisiera hacer un llamado asi me va salir un error:
muchos_items(separador = 'o', archivo = 'holis', greeting = 'good morning') # me va salir un error, esto funcionaria de maravilla si fuera con diccionarios, pero con tuplas no funciona.
# Esto tambien me lanzaria un error:
muchos_items(1, 2, 3, 4, num = 4)"""

# Formas de concatenar, con sep & .join: 
"""
def concatenar(*args, sep = '/'): # Acá sep='/', esto es para separar
  return sep.join(args) # Entonces cuando hago sep.join, le estoy diciendo que me los va se parar por lo que le dije arriba 
print(concatenar('hola', 'leina', sep='.'))
# También si quiero puedo volver a asignar lo que quiero que me separe mi concatenación
print(concatenar('hola', 'leina', sep='@'))
print(concatenar('hola', 'leina', sep='&'))


Lo anterior tambien podria hacerse de las dos siguientes maneras:
def concatenar(*args): 
  sep = ', ' aca le estaria definiendo por que simbolo los voy a separar.
  return sep.join(args)

Tambien podria hacerse de la siguiente forma:
def concatenar(*args): 
  return ';'.join(args) Esto quiere decir que los voy a separar por ; 
"""
nombreString = '''Fulano
Mengano
Sutano '''
#print(nombreString)
nameList = nombreString.split(sep='/n')
print(nameList)