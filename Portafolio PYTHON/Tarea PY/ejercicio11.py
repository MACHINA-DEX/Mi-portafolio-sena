print("ingresa la fecha para determinar si es navidad o no")


dia=int(input("ingrese el dia :"))
while 0<dia>30:
    print("esta fecha no es valida ingresa otra fecha")
    dia=int(input("ingrese el dia :"))
print("el dia es valido")

mes=int(input("ingrese el mes :"))
while 0<mes>12:
    print("El mes no es valido")
    mes=int(input("ingrese el mes :"))
print("El mes es valido")

if dia==25 and mes ==12:
    print("la fecha es en navidad ")
else:
    print("la fecha no es en navidad")