import math


def calcular_semieje_mayor(distancia_media):
    semieje_mayor = distancia_media / 2
    return semieje_mayor


def calcular_periodo(semieje_mayor):
    G = 6.67430e-11 
    M = 1.989e30  # Masa del Sol en kg
    periodo = 2 * math.pi * math.sqrt((semieje_mayor**3) / (G * M))
    return periodo


def main():
    distancia_media = None
    while distancia_media is None:
        try:
            distancia_media = float(input("Ingresa la distancia media al sol (en unidades astronómicas): "))
            if distancia_media <= 0:
                print("¡Error! La distancia media debe ser un valor positivo.")
                distancia_media = None
        except ValueError:
            print("¡Error! Debes ingresar un valor numérico para la distancia media.")


    semieje_mayor = calcular_semieje_mayor(distancia_media)
    periodo = calcular_periodo(semieje_mayor)


    print("El semieje mayor es:", semieje_mayor, "unidades astronómicas")
    print("El período orbital es:", periodo, "años")


if __name__ == "__main__":
    main()
