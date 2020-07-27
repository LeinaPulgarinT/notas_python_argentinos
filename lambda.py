# lo que estamos haciendo aca, es que queremos que cada uno de los indices que hay dentro de la lista se eleve a la 2, y se me vayan guardando en otra lista lista, eso mismo se puede hacer con funciones lambda de una manera mas elegante:
"""
enteros = [1, 2, 4, 7]
cuadrados = []
for e in enteros:
    cuadrados.append(e ** 2)
     
print(cuadrados)
"""

# Con lambda:
enteros = [1, 2, 4, 7]
cuadrados = list(map(lambda x: x**2, enteros)) # De esta forma es mucho mas elegante
#print(cuadrados)
# Las funciones lambda las podemos utlizar como el ejemplo anterior.

# Supongamos que ahora queremos es que en vez de pasarle una lista de enteros, le pasemos a nuestra función map una lista de funciones y que en cada funcion me evalue una expresion para una lista de enteros, pues se haria de la siguiente forma:
enteros = [1, 2, 4, 7]

def cuadrado(x):
    return x ** 2
def cubo(x):
    return x ** 3
funciones = [cuadrado, cubo]
for e in enteros: # Acá el for me recorre cada uno de los indices de la lista enteros
    resultado = list(map(lambda x: x(e), funciones )) # Acá la funcion lambda lo que me hace es que x, representa a cada uno de los indices que hay en la lista funciones, es decir que representa a 'cubo' y a 'cuadrado', y lo que me hace es que me evalua cudrado(e), y cubo(e), e representan cada una de las iteraciones del ciclo for es decir que primero va ser cuadrado(1), cubo(1), luego cuadrado(2), cubo(2) ... cuadrado(7), cubo(7)
    #print(resultado)

# Otro ejemplo:
squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

# Con lambda y map:
squares_two = list(map(lambda x: x ** 2, range(10)))
print(squares_two)
# El problema de hacerlo con el for es que esa x del for despues de que el for se acaba sigue existiendo en el ultimo valor en el que quedo en este caso 9 si imprimimos la x, nos vamos a dar cuenta de que es asi, encambio con lambda y map eso no sucede.
print(x)

# Esto también saldria bien de la siguiente forma, y quedaría de una forma más organizada:
cuadrados_two = [x ** 2 for x in range(10)]



