import math
def calcular_densidad(masa_planeta, radio_planeta):
    volumen = (4/3) * math.pi * (radio_planeta**3)
    densidad = masa_planeta / volumen
    return densidad
def main():
    masa_planeta = None
    while masa_planeta is None:
        try:
            masa_planeta = float(input("Ingresa la masa del planeta (en kilogramos): "))
        except ValueError:
            print("¡Error! Debes ingresar un valor numérico para la masa.")
    radio_planeta = None
    while radio_planeta is None:
        try:
            radio_planeta = float(input("Ingresa el radio del planeta (en metros): "))
            if radio_planeta <= 0:
                print("¡Error! El radio debe ser un valor positivo.")
                radio_planeta = None
        except ValueError:
            print("¡Error! Debes ingresar un valor numérico para el radio.")
    densidad = calcular_densidad(masa_planeta, radio_planeta)
    print("La densidad del planeta es:", densidad, "kg/m^3")
if __name__ == "__main__":
    main()
