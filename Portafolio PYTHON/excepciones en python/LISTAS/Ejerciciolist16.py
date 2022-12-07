
a=input("Ingrese el nombre del primer empleado :")
print("")
a1=int(input("Ingrese el primer sueldo del primer empleado :"))
print("")
a2=int(input("Ingrese el segundo sueldo del primer empleado :"))
print("")
a3=int(input("Ingrese el tercero sueldo del primer empleado :"))
print("")
b=input("Ingrese el nombre del segundo empleado :")
print("")
b1=int(input("Ingrese el primer sueldo del segundo empleado :"))
print("")
b2=int(input("Ingrese el segundo sueldo del segundo empleado :"))
print("")
b3=int(input("Ingrese el tercer sueldo del segundo empleado :"))
print("")
c=input("Ingrese el nombre del tercer empleado :")
print("")
c1=int(input("Ingrese el primero sueldo del tercer empleado :"))
print("")
c2=int(input("Ingrese el segundo sueldo del tercer empleado :"))
print("")
c3=int(input("Ingrese el tercer sueldo tercer empleado :"))
print("")

e1=(a1,a2,a3)

e2=(b1,b2,b3)

e3=(c1,c2,c3)

print("El empleado ",a,"resivio los siguientes sueldos :")
print(e1)
print("El empleado ",b,"resivio los siguientes sueldos :")
print(e2)
print("El empleado ",c,"resivio los siguientes sueldos :")
print(e3)

st1=a1+a2+a3

st2=b1+b2+b3

st3=c1+c2+c3

print("El empleado ",a,"cobro en total  :",st1)
print("El empleado ",b,"cobro en total  :",st2)
print("El empleado ",c,"cobro en total  :",st3)


if st1 >=500000:
    print("El empleado ",a,"Cobro mas de 500.000cop en este ultimo trimestre")
elif st1<500000:
    print("El empleado",a,"no gana mas de 500.000cop en el ultimo trimestre")


if st2>=500000:
    print("El empleado ",b,"Cobro mas de 500.000cop en este ultimo trimestre")
elif st2<500000:
    print("El empleado",b,"no gana mas de 500.000cop en el ultimo trimestre")


if st3 >=500000:
    print("El empleado ",c,"Cobro mas de 500.000cop en este ultimo trimestre")
elif st3<500000:
    print("El empleado",c,"no gana mas de 500.000cop en el ultimo trimestre")









