# Datos estáticos
# Arreglo
tamArreglo = 5
valNums = [True]*tamArreglo
print(valNums)
pos = 0
print(valNums[pos]," TIPO: ",type(valNums[pos]))
print(valNums," TIPO: ",type(valNums))

valNums.append('False')
pos = 5
print(valNums[pos]," TIPO: ",type(valNums[pos]))

# Ejercicio Construir una función que determine si la lista es homogenea o heterogeneas