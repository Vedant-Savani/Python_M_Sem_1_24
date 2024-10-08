from UI import*
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Library Management System")
root.geometry("500x300")
root.config(bg="#f5f5f5") 

GuiObj=GUI(root)
GuiObj.welcome_page()


root.mainloop()

