import tkinter as tk
from random import randint

class Dado:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Dice & Dragon")
        self.ventana.geometry("400x500")
        self.ventana.resizable(False, False)

        # Cargar imagen de fondo (debe ser .png o .gif)
        self.fondo_img = tk.PhotoImage(file="img\dragon.png") 

        # Crear un Label para la imagen y colocarlo al fondo
        self.fondo_label = tk.Label(self.ventana, image=self.fondo_img)
        self.fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.portada = tk.Label(self.ventana, text="Dice & Dragons", font=("Arial", 30), bg="black", fg="darkgoldenrod1")
        self.portada.place(x=65, y=15)

        # Crear los demás widgets
        self.etiqueta = tk.Label(self.ventana, text="ReSuLtAdO", font=("Arial", 30), bg="black", fg="darkgoldenrod1")
        self.etiqueta.place(x=165, y=430)

        botones = [
            ("Lanzar Ð4", self.lanzar_d4),
            ("Lanzar Ð6", self.lanzar_d6),
            ("Lanzar Ð10", self.lanzar_d10),
            ("Lanzar Ð20", self.lanzar_d20),
            ("Lanzar Ð100", self.lanzar_d100)
        ]

        for i, (texto, comando) in enumerate(botones):
            b = tk.Button(self.ventana, text=texto, font=("Arial", 18), bg="darkgoldenrod1", fg="black", command=comando)
            b.place(x=10, y=100 + i * 60)

    def lanzar_d4(self):
        resultado = randint(1, 4)
        self.etiqueta["text"] = f"Ð4=> {resultado}  "

    def lanzar_d6(self):
        resultado = randint(1, 6)
        self.etiqueta["text"] = f"Ð6=> {resultado}  "

    def lanzar_d10(self):
        resultado = randint(1, 10)
        self.etiqueta["text"] = f"Ð10=> {resultado} "

    def lanzar_d20(self):
        resultado = randint(1, 20)
        self.etiqueta["text"] = f"Ð20=> {resultado} "

    def lanzar_d100(self):
        resultado = randint(1, 100)
        self.etiqueta["text"] = f"Ð100=> {resultado}"

    def run(self):
        self.ventana.mainloop()


dado = Dado()
dado.run()