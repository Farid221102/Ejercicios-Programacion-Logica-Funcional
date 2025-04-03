def agregar_asignatura(lista):
    res = input("Ingrese una asignatura nueva: ")
    if(res == "no"):
        return lista
    return agregar_asignatura(lista + [res])

asignaturas = ["Graficación","Automatas","Investigación"]
print(agregar_asignatura(asignaturas))