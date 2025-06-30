import tkinter as tk
from random import randint
import pygame

class Dado:
    def __init__(self):

        pygame.mixer.init()
        pygame.mixer.music.load("sound/dragon_breath.mp3")
        pygame.mixer.music.play(1)  # - - - - Elementos para agregar musica o sonidos mp3 o wav

        self.sonido_click = pygame.mixer.Sound("sound/clic/D4.mp3",)
        self.sonido_click1 = pygame.mixer.Sound("sound/clic/D6.mp3",)
        self.sonido_click2 = pygame.mixer.Sound("sound/clic/D10.mp3",)
        self.sonido_click3 = pygame.mixer.Sound("sound/clic/D20.mp3",)
        self.sonido_click4 = pygame.mixer.Sound("sound/clic/D100.mp3",)
        

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
        self.etiqueta.place(x=175, y=430)

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
        self.sonido_click.play()
        resultado = randint(1, 4)
        self.etiqueta["text"] = f"Ð 4 = {resultado}"

    def lanzar_d6(self):
        self.sonido_click1.play()
        resultado = randint(1, 6)
        self.etiqueta["text"] = f"Ð 6 = {resultado}"

    def lanzar_d10(self):
        self.sonido_click2.play()
        resultado = randint(1, 10)
        self.etiqueta["text"] = f"Ð10 = {resultado}"

    def lanzar_d20(self):
        self.sonido_click3.play()
        resultado = randint(1, 20)
        self.etiqueta["text"] = f"Ð20 = {resultado}"

    def lanzar_d100(self):
        self.sonido_click4.play()
        resultado = randint(1, 100)
        self.etiqueta["text"] = f"Ð100 = {resultado}"

    def run(self):
        self.ventana.mainloop()


dado = Dado()
dado.run()