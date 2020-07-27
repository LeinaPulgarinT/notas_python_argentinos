# lo que me hace el siguiente codigo es que me va filtrar en la lista valores solo los numeros que sean pares:
"""
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
print(pares)
"""

# Lo anterior se puede hacer de una forma mas elegante utilizando lambda y filter():
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x: x % 2 == 0, valores))
print(pares)
