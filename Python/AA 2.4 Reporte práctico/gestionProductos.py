productos = ["Frijoles Refritos","Coca Cola","Zumo de naranja", "Café de Olla","Gorditas de Chicharrón","Huevos Motuleños"]

productos2 = sorted(productos)

productos3 = ", ".join(productos2)

print(productos3)
print("")

productos4 = list(map(lambda pro: pro.replace(" ","-"), productos2))

productos5 = list(map(lambda pro: pro.replace(" ","-"), productos4))

productos6 = list(map(lambda pro: pro.lower(), productos5))

print(productos6)