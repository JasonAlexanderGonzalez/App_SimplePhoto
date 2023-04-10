import tkinter as tk
import pyautogui
from tkinter import filedialog
from PIL import ImageTk

class ScreenshotApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Screenshot App")

        # Configurar el tamaño de los botones
        button_width = 15
        button_height = 2

        # Crear botón de "play"
        self.play_button = tk.Button(self.root, text="Play", width=button_width, height=button_height, command=self.take_screenshot, bg="green")
        self.play_button.pack(side="left")  # Modificado

        # Crear botón de "guardar"
        self.save_button = tk.Button(self.root, text="Guardar", width=button_width, height=button_height, command=self.save_screenshot, bg="blue")
        self.save_button.pack(side="left")  # Modificado

        # Crear botón de "salir"
        self.quit_button = tk.Button(self.root, text="Salir", width=button_width, height=button_height, command=self.root.destroy, bg="red")
        self.quit_button.pack(side="left")  # Modificado

        # Crear label para mostrar la imagen
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.image = None
        self.filename = ""

        self.root.mainloop()

    def take_screenshot(self):
        # Tomar captura de pantalla
        self.image = pyautogui.screenshot()

        # Mostrar imagen en la interfaz gráfica
        img_tk = ImageTk.PhotoImage(self.image)
        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk  # Para prevenir que la imagen sea borrada por el recolector de basura

    def save_screenshot(self):
        # Pedir la ubicación donde se desea guardar la imagen
        self.filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])

        # Guardar la imagen en la ubicación especificada
        if self.filename:
            self.image.save(self.filename)

if __name__ == '__main__':
    app = ScreenshotApp()
