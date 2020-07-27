# Listas por comprension:
# Las listas por comprension nos ahorra tener que utlizar mas lineas de código y nos proporcionan una forma de hacer las cosas mucho mas sencillas, por ejemplo quiero hacer dos for que me recorran cada uno de a lista doferente y si los elementos de la lista son diferentes me los va a juntar en cada iteracion:
tuplitas = [(x, y) for x in range(1, 4) for y in [3, 1, 4] if x != y]
print(tuplitas)

# Otra forma de hacer el ejemplo anterior pero con ciclos for:
tuplas = []
for x in range(1, 4): # ese range(1, 4) == [1, 2, 3]
    for y in [3, 1, 4]:
        if x != y:
            tupla = (x, y)
            tuplas.append(tupla)
print(tuplas)

# CONCLUSION:
# Se puede notar si queremos hacer lo del segundo ejemplo como el primero debemos hacer poner los ciclos y el if en el mismo orden para que nos de los mismos resultados.


#------Ejercicios que se pueden hacer con comprensiones de listas: --------------

# Duplicar los elementos de una lista:
vec = [-4, -2, 0, 2, 4]
duplicados = [x * 2 for x in vec] # Así yo no lo guarde en una variable esto lo que me retorna es una nueva lista, no es que me sobrescriba la que ya existe, si no que me genera una nueva direccion de memoria.

# Filtrar la lista para excluir números negativos:
positivos = [x for x in vec if x >= 0] # esto me genera una nueva lista solo con los numeros positivos.


