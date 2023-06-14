import math
def calcular_gravedad(masa_planeta, radio_planeta):
    G = 6.67430e-11  # Constante de gravitación universal
    gravedad = G * masa_planeta / (radio_planeta ** 2)
    return gravedad
def obtener_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print("¡Error! Debes ingresar un valor positivo.")
            else:
                return valor
        except ValueError:
            print("¡Error! Debes ingresar un valor numérico.")
masa_planeta = obtener_numero_positivo("Ingresa la masa del planeta (en kilogramos): ")
radio_planeta = obtener_numero_positivo("Ingresa el radio del planeta (en metros): ")
gravedad = calcular_gravedad(masa_planeta, radio_planeta)
print("La gravedad en la superficie del planeta es:", gravedad, "m/s^2")