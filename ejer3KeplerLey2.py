import math


def calcular_tasa_cambio_area(L, M):
    tasa_cambio_area = L / (2 * M)
    return tasa_cambio_area


def main():
    L = None
    while L is None:
        try:
            L = float(input("Ingresa el momento angular (L): "))
        except ValueError:
            print("¡Error! Debes ingresar un valor numérico para el momento angular.")


    M = None
    while M is None:
        try:
            M = float(input("Ingresa la masa del cuerpo central (M): "))
        except ValueError:
            print("¡Error! Debes ingresar un valor numérico para la masa.")


    tasa_cambio_area = calcular_tasa_cambio_area(L, M)
    print("La tasa de cambio del área es:", tasa_cambio_area)


if __name__ == "__main__":
    main()



