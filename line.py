def line():
    coefA = float(input("Ingrese el coeficiente A:"))
    coefB = float(input("Ingrese el coeficiente B:"))
    coorX1 = float(input("Ingrese el coeficiente X1:"))
    coorX2 = float(input("Ingrese el coeficiente X2:"))
    coory1 = coefA*coorX1+coefB
    coory2 = coefA*coorX2+coefB
    p1 = f"({coorX1}, {coory1})"
    pp1 = (coorX1,coory1)
    p2 = f"({coorX2}, {coory2})"
    pp2 = (coorX2,coory2)

    print(f"El coeficiente A de su ecuación de la recta es: {coefA}")
    print(f"El coeficiente B de su ecuación de la recta es: {coefB}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coorX1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coorX2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {coefA}X + {coefB}")
    print("")

    print("Dados los siguientes puntos:")
    print("\t"+f"P1 {p1}")
    print("\t"+f"P2 {p2}")
    print("")

    import math
    from math import dist
    print (f"La distancia entre ellos es: {math.dist(pp1,pp2)}")
