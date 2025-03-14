#EJERCICIO 1: Ordenar café para el grupo ISC

'''1. Crear una función que no tome ningún argumento y devuelva la 
cadena de texto café para simular la preparación de una taza de café'''

'''2. Crear función para tomar la orden del café que toma un argumento
numero_tazas, que indica cuántas tazas de café se desean.
    Dentro de la función:
    - Almacena los resultados en una lista llamada tazas_cafe.
    - Utiliza una lista por comprensión para llamar a la función preparar_cafe 
      según el numero_tazas propocionado. Ir archivo compresionListas.py
    - Finalmente, devuelve numero_tazas'''

'''3. Llama a la 2da función con el número de tazas que
requiere y almacenarla en lista'''

def preparar_cafe():
    return "Café"

def ordenar_cafe(num_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(num_tazas)]
    return tazas_cafe

cafe_grupo_a = ordenar_cafe(int(input('Ingresa tu orden: ')))
print(cafe_grupo_a)