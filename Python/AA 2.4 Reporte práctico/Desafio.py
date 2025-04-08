import tkinter as tk
from tkinter import messagebox, Toplevel
from functools import reduce

# --- Datos de entrada ---
estudiantes = ["Alumno 1", "Alumno 2", "Alumno 3", "Alumno 4"]
materias = ["Redes", "Programación funcional", "Bases de datos"]
aspectos = ["Contenido", "Complejidad", "Herramientas", "Prácticas"]

evaluacion = {
    "Contenido": "¿Qué tan claro fue el contenido de la materia?",
    "Complejidad": "¿Qué tan compleja te pareció la materia?",
    "Herramientas": "¿Qué tan útiles fueron las herramientas utilizadas?",
    "Prácticas": "¿Qué tan efectivas fueron las prácticas realizadas?"
}

respuestas = {materia: [] for materia in materias} #Guarda las respuestas por materia
registro_actual = 0 #Para saber en que número de registro se encuentra

# --- Funciones funcionales ---
#Función para calcular el promedio de una lista, redondea a dos decimales
def calcularPromedio(lista):
    return round(reduce(lambda acu, x: acu + x, lista) / len(lista), 2) if len(lista) > 0 else 0

#Calcula el promedio general por materia
def promedioGeneralMateria(respuestas):
    return dict(map(lambda materia: (materia,calcularPromedio(list(map(lambda alumno: calcularPromedio(alumno), respuestas.get(materia, []))))), respuestas.keys()))

#Función para calcular el promedio global de todas las mateiras
def promedioGeneral(respuestas):
    return calcularPromedio(list(map(lambda materia: calcularPromedio(list(map(lambda alumno: calcularPromedio(alumno), respuestas[materia]))), respuestas)))

#Calcula la suma de todas las calificaiones de una materia
def totalMateria(respuestas):
    return dict(map(lambda materia: (materia,reduce(lambda acu, alumno: acu + sum(alumno), respuestas[materia], 0)), respuestas))

#Calcula la suma de todas las calificaiones generales, es decir, de todas las materias
def totalGeneral(respuestas):
    return reduce(lambda acu, materia: acu + reduce(lambda acu2, alumno: acu2 + sum(alumno), respuestas[materia], 0),respuestas,0)

#Función para obtener el mayor y menor promedio por materia
def promedioMaxMin(respuestas):
    promedios = list(map(lambda materia:calcularPromedio(list(map(lambda alumno: calcularPromedio(alumno), respuestas[materia]))), respuestas))
    return max(promedios), min(promedios)

# --- Interfaz gráfica ---
class EncuestaApp:
    #Constructor para iniciarlizar la ventana principal
    def __init__(self, root):
        self.root = root
        self.root.title("Encuesta de Evaluación de Asignaturas")
        self.vars = {} #Diccionario vacío para almacenar las variables de entrada
        self.crear_formulario()

    def crear_formulario(self):
        tk.Label(self.root, text="Encuesta de Evaluación", font=("Arial", 16)).pack(pady=10)

        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(pady=10)

        #Estructura anidada para guardar las entradas del usuario
        self.vars = dict(map(lambda materia: (materia,dict(map(lambda asp: (asp, tk.StringVar()), aspectos))), materias))

        #Crea los formularios de entrada para cada materia
        list(map(lambda materia: self.crear_bloque_materia(materia), materias))

        tk.Button(self.root, text="Guardar", command=self.guardar_respuestas).pack(pady=10)

    #Genera los labels con el nombre de la materia y sus campos de evaluación
    def crear_bloque_materia(self, materia):
        tk.Label(self.form_frame, text=materia, font=("Arial", 14, "bold"), fg="blue").pack(anchor="w")

        #Se coloca el label con la pregunta
        def crear_linea(aspecto):
            frame = tk.Frame(self.form_frame)
            frame.pack(anchor="w", pady=2)
            tk.Label(frame, text=aspecto + ":", width=40, anchor="w").pack(side="left")
            tk.Label(frame, text=evaluacion[aspecto], width=50, anchor="w").pack(side="left")
            #Se crea la caja de texto
            tk.Entry(frame, width=5, textvariable=self.vars[materia][aspecto]).pack(side="left")

        list(map(crear_linea, aspectos))

    #Borra el contenido de los campos para poder hacer otro registro
    def limpiar_campos(self):
        list(map(lambda materia: list(map(lambda asp: self.vars[materia][asp].set(""), aspectos)), materias))

    #Evento que se ejecuta al dar click al botón
    def guardar_respuestas(self):
        global registro_actual #Para saber cuantos alumnos han respondido

        if registro_actual >= 4:
            messagebox.showinfo("Límite alcanzado", "Ya se registraron los 4 alumnos.")
            return

        #Extrae las respuestas, las convierte en int
        def obtener_valores(materia):
            return list(map(lambda asp: int(self.vars[materia][asp].get()), aspectos))

        #Crea el diccionario con las respuestas por materia
        respuestas_actual = dict(map(lambda materia: (materia, obtener_valores(materia)), materias))
        #Agrega el diccionario de respuestas por materia, al diccionario global
        list(map(lambda materia: respuestas[materia].append(respuestas_actual[materia]), materias))

        registro_actual += 1
        self.limpiar_campos()

        if registro_actual == 4:
            self.mostrar_resultados()
        else:
            messagebox.showinfo("Registro guardado", f"Respuestas del estudiante {registro_actual} guardadas.")

    #Crea una nueva ventana para mostrar los resultados
    def mostrar_resultados(self):
        ventana = Toplevel(self.root)
        ventana.title("Resultados de la Encuesta")
        
        #Se llamda a todas las funciones creadas previamente para obtener los resultados deseados
        prom_materia = promedioGeneralMateria(respuestas)
        total_materia = totalMateria(respuestas)
        prom_gen = promedioGeneral(respuestas)
        total_gen = totalGeneral(respuestas)
        max_val, min_val = promedioMaxMin(respuestas)

        mensaje = "Resultados de la Encuesta:\n\n"
        #Usa reduce para construi el resumen que se tiene por materia
        mensaje += reduce(lambda acu, m: acu + f"{m}: Promedio = {prom_materia[m]}, Total = {total_materia[m]}\n", materias, "")
        mensaje += f"\nPromedio general: {prom_gen}\nTotal general: {total_gen}\nValor máximo de promedios: {max_val}\nValor mínimo de promedios: {min_val}"

        #Muestra todos los resultados en la ventana nueva
        tk.Label(ventana, text=mensaje, justify="left", font=("Arial", 12)).pack(padx=10, pady=10)

# --- Ejecutar ---
if __name__ == '__main__':
    root = tk.Tk()
    app = EncuestaApp(root)
    root.mainloop()