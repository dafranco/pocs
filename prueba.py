import tkinter as tk
import random
import string
from tkinter import font


class ReactionPracticeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Práctica de Reacción")
        self.grid_size = 4  # Tamaño de la cuadrícula (4x4)
        self.buttons = {}  # Diccionario para guardar botones
        self.target_keys = []  # Lista de teclas objetivo
        self.timer_label = None  # Etiqueta para el temporizador
        self.remaining_time = 5  # Tiempo límite en segundos
        self.setup_ui()
        self.new_targets()

    def setup_ui(self):
        """Crea la cuadrícula de botones y el temporizador."""
        # Configura la cuadrícula de botones
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                button = tk.Button(
                    self.root,
                    text="",
                    width=8,
                    height=4,
                    font=font.Font(size=26, weight="bold"),
                    bg="white",
                    fg="red",
                    state="normal",
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[(i, j)] = button

        # Etiqueta para el temporizador
        self.timer_label = tk.Label(
            self.root,
            text=f"Tiempo restante: {self.remaining_time}s",
            font=font.Font(size=14),
        )
        self.timer_label.grid(row=self.grid_size, column=0, columnspan=self.grid_size)

        # Vincula las teclas del teclado al evento de pulsación
        self.root.bind("<KeyPress>", self.key_pressed)

    def new_targets(self):
        """Genera nuevas teclas objetivo y las muestra en la cuadrícula."""
        self.remaining_time = 5  # Reinicia el temporizador
        self.update_timer()

        # Limpia los colores y textos anteriores
        for button in self.buttons.values():
            button.config(bg="white", text="")

        # Genera hasta 3 teclas objetivo
        self.target_keys = random.sample(string.ascii_uppercase, k=3)

        # Coloca las teclas en posiciones aleatorias de la cuadrícula
        positions = random.sample(list(self.buttons.keys()), k=len(self.target_keys))
        for key, position in zip(self.target_keys, positions):
            self.buttons[position].config(text=key, bg="orange")

    def update_timer(self):
        """Actualiza el temporizador visual."""
        self.timer_label.config(text=f"Tiempo restante: {self.remaining_time}s")
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.new_targets()  # Si el tiempo se acaba, genera nuevas teclas

    def key_pressed(self, event):
        """Maneja la pulsación de teclas."""
        pressed_key = event.char.upper()
        if pressed_key in self.target_keys:
            # Encuentra el botón correspondiente y colorea de verde
            for button_pos, button in self.buttons.items():
                if button["text"] == pressed_key:
                    button.config(bg="green")
                    break
            # Elimina la tecla de la lista de objetivos
            self.target_keys.remove(pressed_key)

            # Si ya no quedan teclas objetivo, genera nuevas
            if not self.target_keys:
                self.root.after(1000, self.new_targets)


# Inicializa la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ReactionPracticeApp(root)
    root.mainloop()
