estudiantes = {
    "SMSS12345": {
        "nombre": "Juan Pérez",
        "materias": [("Programacion III",9), ("Ingles",8), ("Redes",10)],
        "edad": 20,
    },
    "SMSS889977": {
            "nombre": "Marta Hernandez",
            "materias": [("Leyes",9), ("Psicologia",7), ("Oratoria",9)],
            "edad": 21,
        },
}

print(estudiantes["SMSS889977"]["nombre"])
print(estudiantes["SMSS889977"]["materias"][2][1])