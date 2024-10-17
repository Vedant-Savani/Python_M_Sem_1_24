from CSV_Handler import CSV_Handler
from UI import *
from books import *
import tkinter as tk
from tkinter import ttk
from members import Members



root = tk.Tk()
root.title("Library Management System")
root.geometry("500x300")
root.config(bg="#f5f5f5") 


BooksObj=Books()
Books.bookDetails=CSV_Handler.loadBooks()
Books.bookHistory=CSV_Handler.loadHistory()

MembersObj=Members()


GuiObj=GUI(root,BooksObj,MembersObj)


GuiObj.welcome_page()


root.mainloop()

