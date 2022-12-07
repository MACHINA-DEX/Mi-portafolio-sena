
def division(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("No se puede dividir por cero")


division(8,4)
division(5,0)
