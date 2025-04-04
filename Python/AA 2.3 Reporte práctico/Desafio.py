def cuadradosLista(arreglo):
    filtro = list(filter(lambda numero: numero > 0 and numero % 1 == 0, arreglo))
    mapeo = list(map(lambda numero: numero**2, filtro))
    return mapeo

cuadrados_enteros = cuadradosLista([-3, 4.8, 5, 3, -3.2])
print(cuadrados_enteros)