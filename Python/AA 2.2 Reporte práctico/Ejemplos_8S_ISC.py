#1) Función de primer orden---------------------------------------------------------------
#Ejemplo 1: Cacular promedio de calificaciones
"""def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

notas = [85, 90, 78, 92, 88]
promedio = calcular_promedio(notas)
print("Tu promedio es:", promedio)

def proyecto_aprobado(calificacion):
    return calificacion >= 70

#Ejemplo 2: Verificar si un proyecto está aprobado
nota_proyecto = 85
if proyecto_aprobado(nota_proyecto):
    print("¡Felicidades, tu proyecto está aprobado!")
else:
    print("Tu proyecto no ha sido aprobado.")"""


#2) Función de primera clase---------------------------------------------------------------
#Ejemplo 1: Asignar una función a una variable
"""def estudiar_materia(materia):
     return f"Estudiando {materia}"

mi_actividad = estudiar_materia
print(mi_actividad("Redes Avanzadas"))

#Ejemplo 2: Pasar una función como argumento
def planificar_semana(actividad, materia):
    return actividad(materia)

print(planificar_semana(estudiar_materia, "Bases de Datos"))"""

#3) Función de orden superior---------------------------------------------------------------
#Ejemplo 1: Seleccionar una operación para procesar notas
"""def operar_notas(operacion, notas):
    return operacion(notas)

def redondear(notas):
    return [round(nota) for nota in notas]

def aumentar_puntos(notas):
    return [nota + 2 for nota in notas]

notas = [85.5, 89.3, 78.7]
print("Notas: ", notas)
print("Notas redondeadas:", operar_notas(redondear, notas))
print("Notas con puntos extra:", operar_notas(aumentar_puntos, notas))

#Ejemplo 2: Crear una función personalizada para estudiar
def crear_metodo_estudio(metodo):
    def estudiar(materia):
        return f"Estudiando {materia} usando el método: {metodo}"
    return estudiar

estudiar_con_pomodoro = crear_metodo_estudio("Técnica Pomodoro")
print(estudiar_con_pomodoro("Inteligencia Artificial"))"""

#4) Función callback---------------------------------------------------------------
#Ejemplo 1: Notificar la finalización de una tarea
"""def realizar_tarea(tarea, callback):
    print(f"Realizando tarea: {tarea}")
    callback(tarea)

def notificar_finalizacion(tarea):
    print(f"¡La tarea '{tarea}' ha sido completada!")

realizar_tarea("Preparar presentación de Redes", notificar_finalizacion)

#Ejemplo 2: Procesar datos después de una operación
def procesar_datos(datos, callback):
    datos_procesados = [dato * 2 for dato in datos]
    callback(datos_procesados)

def mostrar_resultados(resultados):
    print("Resultados procesados:", resultados)

datos = [10, 20, 30]
print("Datos: ", datos)
procesar_datos(datos, mostrar_resultados)"""

#5) Función lambda---------------------------------------------------------------
#Ejemplo 1: Filtrar materias aprobadas
materias = [("Redes", 85), ("Bases de Datos", 68), ("Inteligencia Artificial", 90)]
aprobadas = list(filter(lambda materia: materia[1] >= 70, materias))
print("Materias: ", materias)
print("Materias aprobadas:", aprobadas)

#Ejemplo 2: Calcular el cuadrado de números (útil para algoritmos)
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Números: ", numeros)
print("Cuadrados de los números:", cuadrados)