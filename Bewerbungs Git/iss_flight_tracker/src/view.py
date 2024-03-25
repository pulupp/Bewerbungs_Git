import tkinter as tk
from PIL import Image, ImageTk

class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flight Path Tracker - International Space Station")
        self.root.geometry("720x360")

        # Load and display the image
        image_path = "src/resources/world.png"
        image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(image)

        self.label = tk.Label(self.root, image=self.photo)
        self.label.pack()

    def run(self) -> None:
        self.root.mainloop()

if __name__ == "__main__":
    UserInterface().run()
