# RONDA 1 CORREGIDA
# Ejercicio: calcular el promedio de tres notas.

print("CALCULO DE PROMEDIO")

try:
    nombre = input("Nombre del estudiante: ").strip()
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
        raise ValueError("Las notas deben estar entre 0 y 10.")

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 6:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    print(f"Estudiante: {nombre}")
    print(f"Promedio: {promedio:.2f}")
    print(f"Estado: {estado}")

except ValueError as error:
    print(f"Error en los datos: {error}")
finally:
    print("Proceso finalizado.")
