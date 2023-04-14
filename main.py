import tkinter as tk
import pyautogui

class MouseTracker(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Mouse Tracker")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.coords_label = tk.Label(self, font=("Arial", 18))
        self.coords_label.pack(padx=50, pady=50)
        self.update_coords()

    def update_coords(self):
        x, y = pyautogui.position()
        self.coords_label.config(text=f"X: {x}, Y: {y}")
        self.after(100, self.update_coords)

root = tk.Tk()
app = MouseTracker(master=root)
app.mainloop()
