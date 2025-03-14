def prepPizzas():
    return "🍕"

def prepHamb():
    return "🍔"

def prepHD():
    return "🌭"

def calcular_bonus(numP):
    if numP > 2:
        return "Coca gratis 🥤"
    else:
        return ""

def ordenar(porciones, preparar):
    alimentos = [preparar() for _ in range(porciones)]
    bonus = calcular_bonus(porciones)
    return alimentos, bonus

print("GRUPO A")
pizzas = ordenar(int(input('Ingresa tu orden: ')), prepPizzas)
print(pizzas)

print("\nGRUPO B")
hamb = ordenar(int(input('Ingresa tu orden: ')), prepHamb)
print(hamb)

print("\nGRUPO C")
HD = ordenar(int(input('Ingresa tu orden: ')), prepHD)
print(HD)