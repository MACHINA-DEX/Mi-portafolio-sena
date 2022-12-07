

def notas():
        mayor=0
        menor=0
        for a in range (0,10):
            a=int(input("ingrese las notas"))
            if a<7:
                menor+=1
            elif a>7:
                mayor+=1 

        print("los notas mayores a 7 son :",mayor)
        print("Los numeros menores a 7 son :",menor)       



notas()        