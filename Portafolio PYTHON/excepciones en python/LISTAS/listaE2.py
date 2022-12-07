sueldos=[3000000,1200000,1000000,1300000,900000]
empleados=["Ivan","Jaramillo","Robert","Samuel","Miguel"]

for i in zip(empleados,sueldos):
    print(i[0]," : ",i[1])