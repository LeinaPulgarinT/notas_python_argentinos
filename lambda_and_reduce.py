# Supongamos que tengo una lista y que quiero sumar todos los elementos de esa lista y que me retorne el resultado, la forma colonial de hacerlo seria la siguiente:
"""
valores = [2, 4, 6, 5, 4]
suma = 0
for valor in valores:
    suma = suma + valor
print(suma)
"""
# Pero con reduce() podemos hacer los mismo que se hizo en el ejemplo anterior de una forma mas elegante:
from functools import reduce
valores = [2, 4, 6, 5, 4]
suma = list(reduce(lambda x, y: x + y, valores))
