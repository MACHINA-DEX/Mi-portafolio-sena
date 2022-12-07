from tkinter import messagebox
def numero_mayor():
    if B.get() < A.get() > C.get() :
        message = "El mayor es el primero"+str(A.get())
        messagebox.showinfo(message=message)
    elif A.get() < B.get() > C.get() :
         message = "El mayor es el segundo"+str(B.get())
         messagebox.showinfo(message=message)
    elif A.get() < C.get() > B.get() :
         message = "El mayor es el tercero"+str(C.get())
         messagebox.showinfo(message=message)   
from tkinter import*

interfaz = Tk()
interfaz.geometry("400x250+750+400")
interfaz.title("¿Cual es el nuemro mayor")

lblA = Label(text="ingrese el primer valor :").grid(row=0,column=0)
A = DoubleVar()
txtA = Entry(textvariable=A).grid(row=0,column=1)

lblB = Label(text="ingrese el segundo valor :").grid(row=1,column=0)
B = DoubleVar()
txtB = Entry(textvariable=B).grid(row=1,column=1)

lblC = Label(text="ingrese el tercer valor :").grid(row=2,column=0)
C = DoubleVar()
txtC = Entry(textvariable=C).grid(row=2,column=1)

btncalculo = Button(text="¿cual es el numero mayor?",command = numero_mayor).place(x=100,y=70)

interfaz.mainloop()