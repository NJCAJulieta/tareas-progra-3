codigos = []
nombres = []
seccion = []
curso_Asignado = []
nota = []

for x in range(16):
    codigo = input("\nCodigo del Alumno "+str(x) + "  : ")
    codigos.append(codigo)
    nombre = input("\nNombre del Alumno "+str(x) + "  : ")
    nombres.append(nombre)
    secciones = input("\nseccion del Alumno "+str(x) + "  : ")
    seccion.append(secciones)
    cursos_Asignados = input("\nCurso de Asigno del Alumno "+str(x) + "  : ")
    curso_Asignado.append(cursos_Asignados)
    notas = input("\nnota del Alumno "+str(x) + "  : ")
    nota.append(notas)

print('{:<30} {:<22} {:<23} {:<25} {:<15}'.format("\n\nCodigo", "Nombre", "Sección", "Curso Asignado", "Nota"))
for x in range(16):
    print('{:<25} {:<26} {:<20} {:<30} {:<5}'.format(codigos[x], nombres[x], seccion[x], curso_Asignado[x], nota[x]))