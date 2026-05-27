# Función para calcular horas y clasificación
def calcular_horas(nombre, horas):
    total_horas = sum(horas)

    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total_horas, clasificacion


# Lista para guardar los recursos
recursos = []

# Días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Ingresar datos de 4 recursos
for i in range(4):
    print(f"\nIngrese los datos del recurso {i + 1}")

    nombre = input("Nombre del recurso: ")

    horas = []

    # Pedir horas de cada día
    for dia in dias:
        hora = float(input(f"Horas trabajadas el {dia}: "))
        horas.append(hora)

    # Guardar datos en la matriz
    recursos.append([nombre] + horas)

# Mostrar resultados
print("\n===== REPORTE SEMANAL =====")

for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_horas(nombre, horas)

    print("\nRecurso:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)