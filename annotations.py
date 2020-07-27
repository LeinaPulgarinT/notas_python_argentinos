# Anotaciones en las funciones sirven para especificar el tipo de dato de los parametros, y tambien el tipo de dato que debe retornar la funcion, se especifica después de la flechita
def f(jamon: str, huevos: str = 'huevos') -> str:
    print('Anotaciones:', f.__annotations__)
    print('Argumentos:', jamon, huevos)
    return jamon + ' y ' + huevos
  
f('carne')