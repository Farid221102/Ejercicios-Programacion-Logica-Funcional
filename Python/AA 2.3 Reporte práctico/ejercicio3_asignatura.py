asignatura_viii = ["Base de datos"]

#asignatura_iv = asignatura_viii + ["Web"]

#print(asignatura_iv)

def agregar_asignatura(lista, asignatura):
    return lista + [asignatura]

print(agregar_asignatura(asignatura_viii, input("Ingrese la nueva asignatura: ")))