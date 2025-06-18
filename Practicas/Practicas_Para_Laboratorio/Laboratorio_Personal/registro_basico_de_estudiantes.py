estudiante1 = ("Matias", 19,"Ingenieria civil informatica")

estudiantes = [
    estudiante1,
    ("Ana", 48,"Ingenieria civil informatica"),
    ("Ian",23,"Ingenieria civil informatica")
]

print("\nEstudiantes",estudiantes)

print("\nSegundo estudiante: ",estudiantes[1])

cursos = ("Matematicas","Matematicas","Fisica","Algebra")

print("\nCursos: ",set(cursos))

notas = {
    "Matematicas": 5.6,
    "Algebra": 4.2,
    "Fisica": 6.7
}

print("\nCursos y notas:",notas)

print("\nNota de algrebra: ",notas["Algebra"])

notas["Ingles"] = 6.9

print("\nCursos y notas con asignatura, ingles, agrgrada: ",notas)