import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from view_principal import RobotUI  # Importa la clase RobotUI del archivo view_principal

class Ventana:
    def __init__(self, root, title, ventana_type=None):
        self.root = root
        self.title = title
        self.ventana_type = ventana_type
    
    def abrir(self):
        if self.ventana_type == "control":
            control_ui = RobotUI()
            control_ui.pack()
            control_ui.mainloop()

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

def main():
    root = tk.Tk()
    root.title("Vista")

    # Centrar la ventana en la pantalla
    window_width = 900
    window_height = 850
    center_window(root, window_width, window_height)

    root.configure(bg='#b3cde0')  # Fondo azul medio

    # Construir la ruta al archivo de imagen de manera portátil
    logo_path = os.path.join('src', 'resources-python', 'view', 'assets', 'images', 'Stem.png')
    logo_image = Image.open(logo_path)
    logo_photo = ImageTk.PhotoImage(logo_image)

    # Colocar la imagen en la ventana
    logo_label = tk.Label(root, image=logo_photo, bg='#b3cde0')
    logo_label.place(relx=0.5, rely=0.3, anchor='n')

    style = ttk.Style()
    style.configure(
        'TButton',
        font=('arial', 12, 'bold'),
        foreground='black',
        background='#424242',
        borderwidth=4,
        focusthickness=3,
        focuscolor='none',
        padding=10
    )
    style.map(
        'TButton',
        foreground=[('active', 'black')],
        background=[('active', '#005f99')]
    )

    button_frame = tk.Frame(root, bg='#b3cde0', bd=5)
    button_frame.place(relx=0.5, rely=0.75, anchor='center')

    ventana_control = Ventana(root, "Control Dobot", ventana_type="control")

    button1 = ttk.Button(button_frame, text="Control Dobot", width=20, command=ventana_control.abrir)
    button1.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
