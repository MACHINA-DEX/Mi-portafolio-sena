MENU_ESTUDIANTE=0
while MENU_ESTUDIANTE!=5:
    MENU_ESTUDIANTE=int(input("MENU PRINCIPAL:\n 1.Ingrese alumno \n 2.Ingrese materias \n 3.Ingrese notas \n 4.Estado \n 5.Salir :"))
    if MENU_ESTUDIANTE ==1: 
        E=str(input("Ingrese el nombre del estudiante :"))
    elif MENU_ESTUDIANTE ==2:
        M=str(input("Ingrese el nombre de la materia :"))
    elif MENU_ESTUDIANTE==3:
        N=int(input("¿Cuantas notas desea ingresa? :"))
        for i in range(0,N):
            nota=int(input("ingresa la nota :"))
            nota +=nota
            prom=nota/N  
    elif MENU_ESTUDIANTE == 4:
        print("Nombre :",E)
        print("Materia :",M)
        print("El promedio",prom)
    elif MENU_ESTUDIANTE==5:
        print("Vuelva pronto")





        