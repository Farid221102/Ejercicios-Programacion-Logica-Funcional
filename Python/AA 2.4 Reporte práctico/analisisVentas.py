from functools import reduce

ventas = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

suma = reduce(lambda acumulador, numero:acumulador + numero, ventas, 0)

prom = suma / len(ventas)
print("Promedio en pesos mexicanos:", round(prom))
print("")

dolares = list(map(lambda peso: peso/20.5, ventas))
dolares2 = list(map(lambda peso: round(peso), dolares))
print("Ventas en dolares:", dolares2)
print("")

mayores = list(filter(lambda venta: venta > 150, dolares))
mayores2 = list(map(lambda peso: round(peso), mayores))
print("Ventas en dolares mayores a $150:", mayores2)
print("")

suma2 = reduce(lambda acumulador, numero:acumulador + numero, mayores, 0)
print("Suma total ventas en dolares mayores a $150:", round(suma2))