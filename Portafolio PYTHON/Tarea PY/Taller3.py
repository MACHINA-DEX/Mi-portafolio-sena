print ("Ventas")
opcion=1
acum=0
while True:
    if opcion==1:
        venta=int(input("Digite el valor de compra :"))
        acum=acum+venta
        opcion=int(input("¿Desea agregar mas compras? 1. SI 2. NO "))
    if opcion==2:
        break

print(f"El total de las ventas fue $",acum)
ganancias=acum*25/100
print("la ganancia de las ventas fue de :",ganancias)
