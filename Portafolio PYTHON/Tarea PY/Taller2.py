print("Bienvenido al sistema de notas de alumnos")
nombre=input("ingrese el nombre del alumno :")
pparcial=float(input("ingrese la nota del primer parcial :"))
sparcial=float(input("ingrese la nota del segundop parcial :"))
fparcial=float(input("ingrese la nota del examen final :"))
epp=pparcial*35/100
esp=sparcial*35/100
efp=fparcial*30/100
notaf=epp+esp+efp

if notaf >= 3.5:
    print("el alumnoAprovo su nota es de :",notaf)
else :
    print("el alumno No aprovo  su nota es de :",notaf)
