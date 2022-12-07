print("Binvenido al cajero paquita por favor registrese")
usuario=str(input("Digite su nombre de usuario:"))
clave=int(input("Digite su clave:"))

print("A Continuacion ingrese sus datos para entrara")

ingreso1 = str(input("Ingresa tu usuario para acceder:"))

while ingreso1 != usuario:
 print ("El usuario no es corecto")
 ingreso1 = str(input("Ingresa tu usuario para acceder:"))

ingreso2 = int(input("Ingresa tu contraseña:"))

while ingreso2 != clave:
 print ("La clave no es correcta")
 ingreso2=int(input("Ingresa tu contraseña:"))

print ("Bienvenido usuario",usuario,"Que deseas hacer el dia de hoy?")

MENU_CAJERO=0

while MENU_CAJERO!=4:
    MENU_CAJERO=int(input("Digite la aopcion que quiera ejecutar:\n 1. ver saldo \n 2.retirar \n 3.consignar \n 4. cerrar sesion :"))
    if MENU_CAJERO ==1: 
        print("su saldo es : ")
    elif MENU_CAJERO ==2:
        input("cuanto desea retirar: ")
        print("gracias por preferirnos")
    elif MENU_CAJERO==3:
        input("¿cuanto desea consignar?")
        print("graciass por preferirnos")
    elif MENU_CAJERO == 4:
        print("vuelva pronto")