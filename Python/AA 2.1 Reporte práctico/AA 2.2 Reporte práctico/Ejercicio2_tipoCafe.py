def preparar_cafeAme():
    return "Café americano"

def preparar_cafeOlla():
    return "Café de Olla"

def ordenar_cafe(num_tazas, preparar):
    tazas_cafe = [preparar() for _ in range(num_tazas)]
    return tazas_cafe

print("GRUPO A")
cafe_GA = ordenar_cafe(int(input('Ingresa tu orden: ')), preparar_cafeAme)
print(cafe_GA)

print("\nGRUPO B")
cafe_GB = ordenar_cafe(int(input('Ingresa tu orden: ')), preparar_cafeOlla)
print(cafe_GB)