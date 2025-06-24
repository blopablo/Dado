# - - - - D A D O S - - - - #

import tkinter as tk
from random import randint

class Dado:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Dado")
        self.ventana.config(background="black")
        self.ventana.geometry("400x500")
        self.ventana.resizable(False, False)
    

        self.etiqueta = tk.Label(self.ventana, text="ReSuLtAdO", font=("Arial", 30), bg= "black", fg="yellow")
        self.etiqueta.pack(pady=30)

        self.boton = tk.Button(self.ventana, text="Lanzar Ð4", font=("Arial", 18), bg="yellow", fg="black", command= self.lanzar_d4)
        self.boton.pack(pady=10)

        self.boton = tk.Button(self.ventana, text="Lanzar Ð6", font=("Arial", 18), bg="yellow", fg="black", command= self.lanzar_d6)
        self.boton.pack(pady=10)

        self.boton = tk.Button(self.ventana, text="Lanzar Ð10", font=("Arial", 18), bg="yellow", fg="black", command= self.lanzar_d10)
        self.boton.pack(pady=10)

        self.boton = tk.Button(self.ventana, text="Lanzar Ð20", font=("Arial", 18), bg="yellow", fg="black", command= self.lanzar_d20)
        self.boton.pack(pady=10)

        self.boton = tk.Button(self.ventana, text="Lanzar Ð100", font=("Arial", 18), bg="yellow", fg="black", command= self.lanzar_d100)
        self.boton.pack(pady=10)

    def lanzar_d4(self):
        resultado = randint(1, 4)
        self.etiqueta["text"] = f"╪Ð4=> {resultado}"
    
    def lanzar_d6(self):
        resultado = randint(1, 6)
        self.etiqueta["text"] = f"╪Ð6=> {resultado}"
    
    def lanzar_d10(self):
        resultado = randint(1, 10)
        self.etiqueta["text"] = f"Ð10=> {resultado}"

    def lanzar_d20(self):
        resultado = randint(1, 20)
        self.etiqueta["text"] = f"Ð20=> {resultado}"

    def lanzar_d100(self):
        resultado = randint(1, 100)
        self.etiqueta["text"] = f"Ð100: {resultado}"
    
    


    def run(self):
        self.ventana.mainloop()


dado = Dado()
dado.run()
