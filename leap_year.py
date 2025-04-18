def leap_year():
    year = int(input("Ingrese un año:"))
    type1 = (year%100==0 and year%400==0)
    type2 = (year%100>0 and year%4==0)
    type3 = (year%100>0 and year%4>0)
    if type1==True or type2==True:
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")
