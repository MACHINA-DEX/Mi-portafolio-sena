menuser=0
print("Bienvenidos a TOLISALUD E.P.S")
print("Realice el registro por favor")
N1=str(input("Ingrese su primer nombre :"))
N2=str(input("Ingrese su segundo nombre :"))
A1=str(input("Ingrese su primer apellido :"))
A2=str(input("Ingrese su segundo apellido :"))
CC=int(input("Ingrese su numero de cedula :"))
T=str(input("Ingrese su telefono :"))
C=str(input("Ingrese su correo electronico :"))



while menuser !=3:
    print("""
    Bienvenido que desea hacer

    1-Actulizar
    2-mostrar los datos
    3-salir""")
    menuser=int(input())
    if menuser==1:
        print("ingrese los nuevos datos")
        N1=str(input("Ingrese su primer nombre :"))
        N2=str(input("Ingrese su segundo nombre :"))
        A1=str(input("Ingrese su primer apellido :"))
        A2=str(input("Ingrese su segundo apellido :"))
        CC=int(input("Ingrese su numero de cedula :"))
        T=str(input("Ingrese su telefono :"))
        C=str(input("Ingrese su correo electronico :"))
    if   menuser ==2:
        print("sus datos de usuario son :")
        print("Nombre completo",N1,N2,A1,A2)
        print("Cedula :",CC)
        print("Telefono :",T)
        print("Correo electronico :",C)
    if menuser ==3:
        print("Gracias por su visita")

