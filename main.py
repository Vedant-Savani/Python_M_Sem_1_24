from CSV_Handler import CSV_Handler
from UI import *
from Books import *
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Library Management System")
root.geometry("500x300")
root.config(bg="#f5f5f5") 


BooksObj=Books()
Books.bookDetails=CSV_Handler.loadBooks()
GuiObj=GUI(root,BooksObj)


GuiObj.admin_dashboard_page()


root.mainloop()

