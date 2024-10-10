import tkinter as tk
from tkinter import messagebox
from CSV_Handler import CSV_Handler as CSV
from PIL import Image, ImageTk 

class GUI:

    #Syling Elements       #We made them class variables to have consistency in UI
    header_font = ("Helvetica", 30, "bold")
    button_font = ("Helvetica", 14)
    button_font2 = ("Helvetica", 10)
    text_font = ("Helvetica", 12)
    label_font=("Helvetica", 14)
    input_font=("Helvetica", 14)
    content_font=("Helvetica",10)


    def __init__(self,root,books):
        
        self.root=root
        self.bookObj=books 

    def welcome_page(self):

        for child in self.root.winfo_children(): 
            child.destroy()

        def studentClicked():
            self.student_login_page()
        
        def adminClicked():
            self.admin_login_page()

        self.root.minsize(500,420)




        # image = Image.open("bg.png")  
        # bg_image = ImageTk.PhotoImage(image)

        # frame = tk.Frame(self.root, width=600, height=400)
        # frame.pack()

        # bg_label = tk.Label(frame, image=bg_image)
        # bg_label.place(x=0, y=0, relwidth=0, relheight=0) 




        header_label = tk.Label(self.root, text="Welcome to LMS!", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label.pack(pady=10)

        sub_label = tk.Label(self.root, text="Library Management System \n \n \n\n Login As:", font=GUI.text_font, bg="#f5f5f5", fg="#555555")
        sub_label.pack()

        button_frame = tk.Frame(self.root, bg="#f5f5f5")
        button_frame.pack(pady=10)

        continue_button = tk.Button(button_frame, text="Student", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", padx=20, pady=10, bd=0,
                                    command=studentClicked)
        continue_button.pack(pady=5,padx=10,side="left")
        continue_button = tk.Button(button_frame, text="Admin", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", padx=20, pady=10, bd=0,
                                    command=adminClicked)
        continue_button.pack(side="right",padx=10,pady=5)


        footer_label = tk.Label(self.root, text="Developed by Team'Something' © 2024", font=("Helvetica", 10), bg="#f5f5f5", fg="#888888")
        footer_label.pack(side="bottom",pady=10)



    def student_login_page(self):
        root=self.root
        for child in root.winfo_children(): 
            child.destroy()
        self.root.minsize(500,420)    

        def backClicked():
            self.welcome_page()

        def loginClicked():
            roll=entry_rollnumber.get()   
            paswd=entry_password.get()
            if not(roll) or not (paswd):
                messagebox.showerror("Empty", "Fields Can Not Be Empty!")

            elif roll=="000" and paswd=="000":
                self.sudent_dashboard_page()
            
            else:
                messagebox.showerror("Login Error", "Invalid Username Or Password!")

        header_label = tk.Label(root, text="Student Login", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label.pack(pady=10)

        label_rollnumber = tk.Label(root, text="Roll Number:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_rollnumber.pack(pady=10)
        entry_rollnumber = tk.Entry(root, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_rollnumber.pack(pady=5)

        label_password = tk.Label(root, text="Password:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_password.pack(pady=10)
        entry_password = tk.Entry(root, font=GUI.input_font, width=30, bd=1, relief="solid", show="*")
        entry_password.pack(pady=5)

        login_button = tk.Button(root, text="Login", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                activebackground="#45a049", activeforeground="white", padx=20, pady=10, bd=0, 
                                command=loginClicked)
        login_button.pack(pady=10)

        back_button = tk.Button(root, text="Back", font=GUI.button_font2, bg="#4CAF50", fg="white", 
                                activebackground="#45a049", activeforeground="white", padx=10, pady=2, bd=0, 
                                command=backClicked)
        back_button.pack(pady=15)

        footer_label = tk.Label(root, text="Developed by Team'Something' © 2024", font=("Helvetica", 10), bg="#f5f5f5", fg="#888888")
        footer_label.pack(side="bottom", pady=10)    



    def admin_login_page(self):
        root=self.root
        for child in root.winfo_children(): 
            child.destroy()
        self.root.minsize(500,420)    
        self.root.maxsize(500,420) 

        def backClicked():
            self.welcome_page()   

        header_label = tk.Label(root, text="Admin Login", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label.pack(pady=10)

        label_username = tk.Label(root, text="Username:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_username.pack(pady=10)
        entry_username = tk.Entry(root, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_username.pack(pady=5)

        label_password = tk.Label(root, text="Password:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_password.pack(pady=10)
        entry_password = tk.Entry(root, font=GUI.input_font, width=30, bd=1, relief="solid", show="*")
        entry_password.pack(pady=5)

        login_button = tk.Button(root, text="Login", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                activebackground="#45a049", activeforeground="white", padx=20, pady=10, bd=0, 
                                )
        login_button.pack(pady=10)

        back_button = tk.Button(root, text="Back", font=GUI.button_font2, bg="#4CAF50", fg="white", 
                                activebackground="#45a049", activeforeground="white", padx=10, pady=2, bd=0, 
                                command=backClicked)
        back_button.pack(pady=15)

        footer_label = tk.Label(root, text="Developed by Team'Something' © 2024", font=("Helvetica", 10), bg="#f5f5f5", fg="#888888")
        footer_label.pack(side="bottom", pady=10)



    def student_dashboard_page(self):
        root=self.root
        root=self.root
        for child in root.winfo_children(): 
            child.destroy()
        self.root.minsize(900,500)    
        # self.root.maxsize(00,420) 

        
        side_panel = tk.Frame(root, bg="#333333", width=200, height=500)
        side_panel.pack(side="left", fill="y")
        main_content = tk.Frame(root, bg="#f5f5f5")
        main_content.pack(side="right", expand=True, fill="both")

        # Side panel TAB BUTTONS
        viewBooks_button = tk.Button(side_panel, text="View Books", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(viewBooks), bd=0)
        viewBooks_button.pack(fill="both", pady=10)

        myBooks_button = tk.Button(side_panel, text="My Books", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(myBooks_frame), bd=0)
        myBooks_button.pack(fill="x", pady=10)

        profile_button = tk.Button(side_panel, text="Profile", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(profile_frame), bd=0)
        profile_button.pack(fill="x", pady=10)



        #TABS CONTENT
        viewBooks= tk.Frame(main_content, bg="#f5f5f5")
        profile_frame = tk.Frame(main_content, bg="#f5f5f5")
        myBooks_frame = tk.Frame(main_content, bg="#f5f5f5")
        for frame in (profile_frame, myBooks_frame, viewBooks):
            frame.pack(fill="both", expand=True)


        # ViewBooks Frame
                
        viewBooks_canvas = tk.Canvas(viewBooks)
        viewBooks_canvas.pack(fill="both", expand=True, side="left")

        # Attach the scrollbar to the main window (viewBooks)
        viewBooks_scrollBar = tk.Scrollbar(viewBooks, orient="vertical", command=viewBooks_canvas.yview)
        viewBooks_scrollBar.pack(side="right", fill="y")

        # Configure the canvas to work with the scrollbar
        viewBooks_canvas.configure(yscrollcommand=viewBooks_scrollBar.set)

        # Create a frame inside the canvas
        viewBooks_frame = tk.Frame(viewBooks_canvas)
        viewBooks_canvas.create_window((0, 0), anchor="nw", window=viewBooks_frame)

        # Update the scroll region of the canvas when the frame changes size
        def on_frame_configure(event):
            viewBooks_canvas.configure(scrollregion=viewBooks_canvas.bbox("all"))

        viewBooks_frame.bind("<Configure>", on_frame_configure)

        # Dynamically resize the canvas window to fit the frame's width
        def on_canvas_configure(event):
            viewBooks_canvas.itemconfig(viewBooks_canvas.create_window((0, 0), anchor='nw', window=viewBooks_frame), width=event.width)

        viewBooks_canvas.bind("<Configure>", on_canvas_configure)

        



        books_dict=CSV.loadBooks()
        for bookID in books_dict.keys():
            print(books_dict[bookID])
            self.book_component(viewBooks_frame,books_dict[bookID])
        

        






        #Profile frame
        profile_label = tk.Label(profile_frame, text="Profile Information", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        profile_label.pack()









        #MyBooks frame
        settings_label = tk.Label(myBooks_frame, text="Settings", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        settings_label.pack()





        

        

        def switch_frame(frame):
            viewBooks.pack_forget()
            profile_frame.pack_forget()
            myBooks_frame.pack_forget()
            frame.pack(fill="both", expand=True)
            print(frame)

        switch_frame(viewBooks)


    def admin_book_component(self,frame,bookdict):
        mainbox=tk.Frame(frame,border=1,relief='solid')
        mainbox.pack(fill='x',pady=5)
        title=tk.Label(mainbox,text=bookdict['name'],font=GUI.label_font)
        title.pack(anchor="w")
        author=tk.Label(mainbox,text="by "+bookdict['author'],font=GUI.content_font)
        author.pack(anchor='w')
        total=tk.Label(mainbox,text="\nTotal: "+bookdict['total'] +"\tAvailable: "+bookdict['available'].strip(),font=GUI.content_font)
        total.pack(anchor='w')
        bin=tk.Label(mainbox,text="Bin: "+bookdict['bin'] ,font=GUI.content_font)
        bin.pack(anchor='w')
        brs=""
        for b in bookdict['borrowers']:
            if(b!=""):
                brs+=" , "+b
            
        borrowers=tk.Label(mainbox,text="Borrowers: "+brs ,font=GUI.content_font)
        borrowers.pack(anchor='w')
        





    def admin_dashboard_page(self):
        root=self.root
        root=self.root
        for child in root.winfo_children(): 
            child.destroy()
        self.root.minsize(900,500)    
        # self.root.maxsize(00,420) 

        
        side_panel = tk.Frame(root, bg="#333333", width=200, height=500)
        side_panel.pack(side="left", fill="y")
        main_content = tk.Frame(root, bg="#f5f5f5")
        main_content.pack(side="right", expand=True, fill="both")


#==============================================================================================================================

        # Side panel TAB BUTTONS
        viewBooks_button = tk.Button(side_panel, text="View Books", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(viewBooks,"viewBooks"), bd=0)
        viewBooks_button.pack(fill="both", pady=10)

        addBooks_button = tk.Button(side_panel, text="Add Books", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(addBooks,"addBooks"), bd=0)
        addBooks_button.pack(fill="x", pady=10)
        
        delBooks_button = tk.Button(side_panel, text="Remove Books", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(delBooks,"delBooks"), bd=0)
        delBooks_button.pack(fill="x", pady=10)

        addMembers_button = tk.Button(side_panel, text="Add Member", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(addMembers,"addMembers"), bd=0)
        addMembers_button.pack(fill="x", pady=10)
        
        delMembers_button = tk.Button(side_panel, text="Remove Member", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(delMembers,'delMembers'), bd=0)
        delMembers_button.pack(fill="x", pady=10)



#==============================================================================================================================

        #TABS CONTENT
        viewBooks= tk.Frame(main_content, bg="#f5f5f5")
        addBooks = tk.Frame(main_content, bg="#f5f5f5")
        delBooks = tk.Frame(main_content, bg="#f5f5f5")
        addMembers = tk.Frame(main_content, bg="#f5f5f5")
        delMembers = tk.Frame(main_content, bg="#f5f5f5")
        
        for frame in (viewBooks,addBooks,addMembers,delBooks,delMembers):
            frame.pack(fill="both", expand=True)


#==============================================================================================================================

        # ViewBooks Frame
                
        viewBooks_canvas = tk.Canvas(viewBooks)
        viewBooks_canvas.pack(fill="both", expand=True, side="left")

        viewBooks_scrollBar = tk.Scrollbar(viewBooks, orient="vertical", command=viewBooks_canvas.yview)
        viewBooks_scrollBar.pack(side="right", fill="y")

        viewBooks_canvas.configure(yscrollcommand=viewBooks_scrollBar.set)

        viewBooks_frame = tk.Frame(viewBooks_canvas)
        viewBooks_canvas.create_window((0, 0), anchor="nw", window=viewBooks_frame)

        def on_frame_configure(event):
            viewBooks_canvas.configure(scrollregion=viewBooks_canvas.bbox("all"))

        viewBooks_frame.bind("<Configure>", on_frame_configure)

        def on_canvas_configure(event):
            viewBooks_canvas.itemconfig(viewBooks_canvas.create_window((0, 0), anchor='nw', window=viewBooks_frame), width=event.width)

        viewBooks_canvas.bind("<Configure>", on_canvas_configure)




        def display_books_function(dict):
            for i in viewBooks_frame.winfo_children():
                i.destroy()
            for bookID in dict.keys():
                self.admin_book_component(viewBooks_frame,dict[bookID])

        
        display_books_function(self.bookObj.bookDetails)

        
        

        



#==============================================================================================================================



        #addBooks Frame
        addBooks_canvas = tk.Canvas(addBooks)
        addBooks_canvas.pack(fill="both", expand=True, side="left")

        addBooks_scrollBar = tk.Scrollbar(addBooks, orient="vertical", command=addBooks_canvas.yview)
        addBooks_scrollBar.pack(side="right", fill="y")

        addBooks_canvas.configure(yscrollcommand=addBooks_scrollBar.set)

        addBooks_frame = tk.Frame(addBooks_canvas)
        addBooks_canvas.create_window((0, 0), anchor="nw", window=addBooks_frame)

        def on_frame_configure(event):
            addBooks_canvas.configure(scrollregion=addBooks_canvas.bbox("all"))

        addBooks_frame.bind("<Configure>", on_frame_configure)

        def on_canvas_configure(event):
            addBooks_canvas.itemconfig(addBooks_canvas.create_window((0, 0), anchor='nw', window=addBooks_frame), width=event.width)

        addBooks_canvas.bind("<Configure>", on_canvas_configure)

        #now you can use addBooks_frame as your main screen. 

        def submit_form():
            book_id = entry_book_id.get()
            name = entry_name.get()
            author = entry_author.get()
            total = entry_total.get()
            available = entry_available.get()
            binNO = entry_bin.get()

            if not (book_id and name and author and total.isdigit() and available.isdigit()):
                messagebox.showerror("Input Error", "Please enter valid details in all fields!")
                return

            self.bookObj.addBook({book_id:{'name':name,'author':author,'total':total,'available':available,'bin':binNO,'borrowers':[]}})    


        header_label = tk.Label(addBooks_frame, text="Add Books", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label.pack(pady=10)

        label_book_id = tk.Label(addBooks_frame, text="Book ID:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_book_id.pack(pady=5)
        entry_book_id = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_book_id.pack(pady=5)

        label_name = tk.Label(addBooks_frame, text="Name:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_name.pack(pady=5)
        entry_name = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_name.pack(pady=5)

        label_author = tk.Label(addBooks_frame, text="Author:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_author.pack(pady=5)
        entry_author = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_author.pack(pady=5)

        label_total = tk.Label(addBooks_frame, text="Total Copies:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_total.pack(pady=5)
        entry_total = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_total.pack(pady=5)

        label_available = tk.Label(addBooks_frame, text="Available Copies:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_available.pack(pady=5)
        entry_available = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_available.pack(pady=5)
      
        label_bin = tk.Label(addBooks_frame, text="Bin Number:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_bin.pack(pady=5)
        entry_bin = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_bin.pack(pady=5)

        # Submit button with the theme applied
        submit_button = tk.Button(addBooks_frame, text="Submit", font=GUI.button_font, bg="#4CAF50", fg="white",
                                activebackground="#45a049", activeforeground="white", padx=20, pady=10, bd=0, 
                                command=submit_form)
        submit_button.pack(pady=20)



        




#==============================================================================================================================



        #delBooks Frame
        delBooks_canvas = tk.Canvas(delBooks)
        delBooks_canvas.pack(fill="both", expand=True, side="left")

        delBooks_scrollBar = tk.Scrollbar(delBooks, orient="vertical", command=delBooks_canvas.yview)
        delBooks_scrollBar.pack(side="right", fill="y")

        delBooks_canvas.configure(yscrollcommand=delBooks_scrollBar.set)

        delBooks_frame = tk.Frame(delBooks_canvas)
        delBooks_canvas.create_window((0, 0), anchor="nw", window=delBooks_frame)

        def on_frame_configure(event):
            delBooks_canvas.configure(scrollregion=delBooks_canvas.bbox("all"))

        delBooks_frame.bind("<Configure>", on_frame_configure)

        def on_canvas_configure(event):
            delBooks_canvas.itemconfig(delBooks_canvas.create_window((0, 0), anchor='nw', window=delBooks_frame), width=event.width)

        delBooks_canvas.bind("<Configure>", on_canvas_configure)

        #now you can use delBooks_frame as your main screen. 



#==============================================================================================================================



    #addMembers Frame
        addMembers_canvas = tk.Canvas(addMembers)
        addMembers_canvas.pack(fill="both", expand=True, side="left")

        addMembers_scrollBar = tk.Scrollbar(addMembers, orient="vertical", command=addMembers_canvas.yview)
        addMembers_scrollBar.pack(side="right", fill="y")

        addMembers_canvas.configure(yscrollcommand=addMembers_scrollBar.set)

        addMembers_frame = tk.Frame(addMembers_canvas)
        addMembers_canvas.create_window((0, 0), anchor="nw", window=addMembers_frame)

        def on_frame_configure(event):
            addMembers_canvas.configure(scrollregion=addMembers_canvas.bbox("all"))

        addMembers_frame.bind("<Configure>", on_frame_configure)

        def on_canvas_configure(event):
            addMembers_canvas.itemconfig(addMembers_canvas.create_window((0, 0), anchor='nw', window=addMembers_frame), width=event.width)

        addMembers_canvas.bind("<Configure>", on_canvas_configure)


        #now you can use addBooks_frame as your main screen. 




#==============================================================================================================================




        #delMembers Frame
        delMembers_canvas = tk.Canvas(delMembers)
        delMembers_canvas.pack(fill="both", expand=True, side="left")

        delMembers_scrollBar = tk.Scrollbar(delMembers, orient="vertical", command=delMembers_canvas.yview)
        delMembers_scrollBar.pack(side="right", fill="y")

        delMembers_canvas.configure(yscrollcommand=delMembers_scrollBar.set)

        delMembers_frame = tk.Frame(delMembers_canvas)
        delMembers_canvas.create_window((0, 0), anchor="nw", window=delMembers_frame)

        def on_frame_configure(event):
            delMembers_canvas.configure(scrollregion=delMembers_canvas.bbox("all"))

        delMembers_frame.bind("<Configure>", on_frame_configure)

        def on_canvas_configure(event):
            delMembers_canvas.itemconfig(delMembers_canvas.create_window((0, 0), anchor='nw', window=delMembers_frame), width=event.width)

        delMembers_canvas.bind("<Configure>", on_canvas_configure)
        

        #now you can use delBooks_frame as your main screen. 






#==============================================================================================================================
        

        

        def switch_frame(frame,button):
            viewBooks.pack_forget()
            addBooks.pack_forget()
            delBooks.pack_forget()
            addMembers.pack_forget()
            delMembers.pack_forget()
            viewBooks_button.configure(bg='#45a049')
            addBooks_button.configure(bg='#45a049')
            delBooks_button.configure(bg='#45a049')
            addMembers_button.configure(bg='#45a049')
            delMembers_button.configure(bg='#45a049')
            
            if button=="viewBooks":
                display_books_function(self.bookObj.bookDetails)

            frame.pack(fill="both", expand=True)
            exec( f"{button}_button.configure(bg='#215c52')")
            print(frame)

        switch_frame(viewBooks,'viewBooks')




    @staticmethod
    def alert(title,message):    
        messagebox.showerror(title, message)

    @staticmethod
    def success(title,message):
        messagebox.showinfo(title,message)

    
