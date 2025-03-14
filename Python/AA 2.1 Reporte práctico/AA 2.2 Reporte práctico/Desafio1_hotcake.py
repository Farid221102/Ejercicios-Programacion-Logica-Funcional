def preparar_hotcakes():
    return "🥞"

def ordenar(num_piezas):
    piezas_hc = [preparar_hotcakes() for _ in range(num_piezas)]
    return piezas_hc

hc_fam = ordenar(int(input('Ingresa el número de integrantes de tu familia: ')))
print(hc_fam)