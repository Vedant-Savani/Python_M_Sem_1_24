import tkinter as tk
from tkinter import messagebox
from CSV_Handler import CSV_Handler as CSV
from members import Members

class GUI:

    #Syling Elements       #We made them class variables to have consistency in UI
    header_font = ("Helvetica", 30, "bold")
    button_font = ("Helvetica", 14)
    button_font2 = ("Helvetica", 10)
    text_font = ("Helvetica", 12)
    label_font=("Helvetica", 14)
    input_font=("Helvetica", 14)
    content_font=("Helvetica",10)


#===============================================================================================================================================

    def __init__(self,root,books,memebrs):
        
        self.root=root
        self.bookObj=books 
        self.membersObj=memebrs

#===============================================================================================================================================


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

        # image = Image.open("bg1.jpg")
        # photo1 = ImageTk.PhotoImage(image)

        # background_label = tk.Label(self.root, image=photo1)
        # background_label.place(x=0, y=1)

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

#===============================================================================================================================================


    def student_login_page(self):
        root=self.root
        for child in root.winfo_children(): 
            child.destroy()
        self.root.minsize(500,420)    

        def backClicked():
            self.welcome_page()

        def loginClicked():
            roll=entry_rollnumber.get().upper()   
            paswd=entry_password.get()   
            if not(roll) or not (paswd):
                messagebox.showerror("Empty", "Fields Can Not Be Empty!")

            else:
                try:
                    if self.membersObj.memberDetails[roll]['password']==paswd:
                        self.student_dashboard_page(roll)
                    else:
                        self.alert("Error","INVALID CREDENTIALS !!")
                except:
                    self.alert("Error","INVALID CREDENTIALS !!")

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

#===============================================================================================================================================


    def admin_login_page(self):
        root=self.root
        for child in root.winfo_children(): 
            child.destroy()
        self.root.minsize(500,420)    

        def backClicked():
            self.welcome_page()   


        def adminlogin():
            username=entry_username.get()
            passwd=entry_password.get()
            if(username=="admin" and passwd=="123"):
                self.admin_dashboard_page()
            else:
                self.alert("Error","Wrong Credentials!")    

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
                                command=adminlogin)
        login_button.pack(pady=10)

        back_button = tk.Button(root, text="Back", font=GUI.button_font2, bg="#4CAF50", fg="white", 
                                activebackground="#45a049", activeforeground="white", padx=10, pady=2, bd=0, 
                                command=backClicked)
        back_button.pack(pady=15)

        footer_label = tk.Label(root, text="Developed by Team'Something' © 2024", font=("Helvetica", 10), bg="#f5f5f5", fg="#888888")
        footer_label.pack(side="bottom", pady=10)

#===============================================================================================================================================


    def student_dashboard_page(self,rollnumber):
        root=self.root
        root=self.root
        for child in root.winfo_children(): 
            child.destroy()
        self.root.minsize(900,500)    

        
        
        def switch_frame(frame,button):

            viewBooks.pack_forget()
            myBooks.pack_forget()
            profile.pack_forget()
            viewBooks_button.configure(bg='#45a049')
            myBooks_button.configure(bg='#45a049')
            profile_button.configure(bg='#45a049')
            
            if button=="viewBooks":
                display_books_function(self.bookObj.bookDetails)

            frame.pack(fill="both", expand=True)
            exec( f"{button}_button.configure(bg='#215c52')")
            update_mybooks_frame()
            display_books_function(self.bookObj.bookDetails)


        side_panel = tk.Frame(root, bg="#333333", width=200, height=500)
        side_panel.pack(side="left", fill="y")
        main_content = tk.Frame(root, bg="#f5f5f5")
        main_content.pack(side="right", expand=True, fill="both")

        def logout():
            self.welcome_page()
            


        # Side panel TAB BUTTONS
        viewBooks_button = tk.Button(side_panel, text="View Books", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(viewBooks,'viewBooks'), bd=0)
        viewBooks_button.pack(fill="both", pady=10)

        myBooks_button = tk.Button(side_panel, text="My Books", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(myBooks,'myBooks'), bd=0)
        myBooks_button.pack(fill="x", pady=10)

        profile_button = tk.Button(side_panel, text="Profile", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(profile,'profile'), bd=0)
        profile_button.pack(fill="x", pady=10)
        

        def logout():
            self.welcome_page()
            

        logout_button = tk.Button(side_panel, text="Log Out", font=GUI.button_font,bg="#bd2d2d", fg="white",
                                activebackground="#f12d2d", activeforeground="white", command=logout, bd=0)
        logout_button.pack(fill="x", pady=10)



        #TABS CONTENT
        viewBooks= tk.Frame(main_content, bg="#f5f5f5")
        profile = tk.Frame(main_content, bg="#f5f5f5")
        myBooks = tk.Frame(main_content, bg="#f5f5f5")
        for frame in (profile, myBooks, viewBooks):
            frame.pack(fill="both", expand=True)


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

        



        def search():

            search_type=dropdown_var.get()
            required_items=[]
            if(search_type=="Author"):
               
                aut=entry.get().strip()
                
                if not aut :
                    GUI.alert("Error","Seach field is empty!")
                    return
                for i in self.bookObj.bookDetails.keys():
                    if aut.strip().lower() in self.bookObj.bookDetails[i]['author'].lower():
                        required_items.append((i,self.bookObj.bookDetails[i]))
                
                c=0
                for i in viewBooks_frame.winfo_children():
                    if c==0:
                        c=1
                        continue
                    i.destroy()
                if len(required_items)==0:
                    GUI.alert("...","No Results Found!")
                else:
                    for items in required_items:        
                        self.student_book_component_view(viewBooks_frame,items[1],items[0],rollnumber,display_books_function)


            elif(search_type=="Title"):
               
                aut=entry.get().strip()
                
                if not aut :
                    GUI.alert("Error","Seach field is empty!")
                    return
                for i in self.bookObj.bookDetails.keys():
                    if aut.strip().lower() in self.bookObj.bookDetails[i]['name'].lower():
                        required_items.append((i,self.bookObj.bookDetails[i]))
                
                c=0
                for i in viewBooks_frame.winfo_children():
                    if c==0:
                        c=1
                        continue
                    i.destroy()
                
                if len(required_items)==0:
                    GUI.alert("...","No Results Found!")               
                else:
                    for items in required_items:        
                        self.student_book_component_view(viewBooks_frame,items[1],items[0],rollnumber,display_books_function)
                
            
            else:
                GUI.alert("ERROR","Something Went Wrong!")
                return


        viewBooks_search_frame = tk.Frame(viewBooks_frame)
        viewBooks_search_frame.pack(pady=20) 

        label = tk.Label(viewBooks_search_frame, text="Search by ", font=GUI.label_font)
        label.pack(side=tk.LEFT, padx=5)

        dropdown_var = tk.StringVar(viewBooks_search_frame)
        dropdown_var.set("Title") 
        
        options = ["Title" , "Author"]
        dropdown_menu = tk.OptionMenu(viewBooks_search_frame, dropdown_var, *options)
        dropdown_menu.pack(side=tk.LEFT,pady=10)
        dropdown_menu.config(font=GUI.button_font,
                                 padx=2, bd=1)

        entry = tk.Entry(viewBooks_search_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry.pack(side=tk.LEFT, padx=5)

        search_button = tk.Button(viewBooks_search_frame, text="Search", command=search,font=GUI.button_font, bg="#4CAF50", fg="white",
                                activebackground="#45a049", activeforeground="white", padx=2, bd=0)
        search_button.pack(side=tk.LEFT, padx=5)

        def display_books_function(dict=self.bookObj.bookDetails):
            c=0
            for i in viewBooks_frame.winfo_children():
                if c==0:
                    c=1
                    continue
                i.destroy()
            for bookID in dict.keys():
                self.student_book_component_view(viewBooks_frame,dict[bookID],bookID,rollnumber,display_books_function)

            
        display_books_function(self.bookObj.bookDetails)

        






        #Profile frame
        profile_canvas = tk.Canvas(profile)
        profile_canvas.pack(fill="both", expand=True, side="left")

        profile_scrollBar = tk.Scrollbar(profile, orient="vertical", command=profile_canvas.yview)
        profile_scrollBar.pack(side="right", fill="y")

        profile_canvas.configure(yscrollcommand=profile_scrollBar.set)

        profile_frame = tk.Frame(profile_canvas)
        profile_canvas.create_window((0, 0), anchor="nw", window=profile_frame)

        def on_frame_configure(event):
            profile_canvas.configure(scrollregion=profile_canvas.bbox("all"))

        profile_frame.bind("<Configure>", on_frame_configure)

        def on_canvas_configure(event):
            profile_canvas.itemconfig(profile_canvas.create_window((0, 0), anchor='nw', window=profile_frame), width=event.width)

        profile_canvas.bind("<Configure>", on_canvas_configure)

        #now you can use profile_frame as your main frame


        header_label = tk.Label(profile_frame, text="Change Your Password", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label.pack(pady=10)

        label_current = tk.Label(profile_frame, text="Enter Current Password:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_current.pack(pady=10)
        entry_current = tk.Entry(profile_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_current.pack(pady=5)

        
        label_new = tk.Label(profile_frame, text="Enter New Password:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_new.pack(pady=10)
        entry_new = tk.Entry(profile_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_new.pack(pady=5)


        label_renew = tk.Label(profile_frame, text="Re-enter New Password:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_renew.pack(pady=10)
        entry_renew = tk.Entry(profile_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_renew.pack(pady=5)

        def resetpass():
            current=entry_current.get()
            new=entry_new.get()
            renew=entry_renew.get()
            if(current==self.membersObj.memberDetails[rollnumber]['password']):
                if(new==renew):
                    self.membersObj.updateMember(rollnumber,new)
            else:
                return
            entry_current.delete(0,tk.END)        
            entry_new.delete(0,tk.END)        
            entry_renew.delete(0,tk.END)        



        search_button = tk.Button(profile_frame, text="Reset", command=resetpass,font=GUI.button_font,bg="#bd2d2d", fg="white",
                                activebackground="#f12d2d", activeforeground="white", padx=10,pady=5, bd=0)
        search_button.pack( pady=10)







        #MyBooks frame
        
        myBooks_canvas = tk.Canvas(myBooks)
        myBooks_canvas.pack(fill="both", expand=True, side="left")

        myBooks_scrollBar = tk.Scrollbar(myBooks, orient="vertical", command=myBooks_canvas.yview)
        myBooks_scrollBar.pack(side="right", fill="y")

        myBooks_canvas.configure(yscrollcommand=myBooks_scrollBar.set)

        myBooks_frame = tk.Frame(myBooks_canvas)
        myBooks_canvas.create_window((0, 0), anchor="nw", window=myBooks_frame)

        def on_frame_configure(event):
            myBooks_canvas.configure(scrollregion=myBooks_canvas.bbox("all"))

        myBooks_frame.bind("<Configure>", on_frame_configure)

        def on_canvas_configure(event):
            myBooks_canvas.itemconfig(myBooks_canvas.create_window((0, 0), anchor='nw', window=myBooks_frame), width=event.width)

        myBooks_canvas.bind("<Configure>", on_canvas_configure)

        #now you can use myBooks_frame as your main frame

             

        def update_mybooks_frame():
            for child in myBooks_frame.winfo_children():
                child.destroy()

            header_label = tk.Label(myBooks_frame, text="Books Issued To: "+str(rollnumber).upper(), font=("Helvetica",20,'bold'), fg="#333333")
            header_label.pack(pady=10)   
            for i in self.bookObj.bookDetails.keys():
                if rollnumber in self.bookObj.bookDetails[i]['borrowers']:
                    self.student_book_component_return(myBooks_frame,self.bookObj.bookDetails[i],i,rollnumber.strip(),update_mybooks_frame)
        
        update_mybooks_frame()

       
        

        

            

        switch_frame(viewBooks,'viewBooks')

#===============================================================================================================================================


    def admin_book_component(self,frame,bookdict,BookID):
        mainbox=tk.Frame(frame,border=1,relief='solid')
        mainbox.pack(fill='x',pady=5,padx=10)
        title=tk.Label(mainbox,text=bookdict['name'],font=GUI.label_font)
        title.pack(anchor="w")
        author=tk.Label(mainbox,text="by "+bookdict['author'],font=GUI.content_font)
        author.pack(anchor='w')
        total1=tk.Label(mainbox,text="Book ID: "+BookID,font=GUI.content_font)
        total=tk.Label(mainbox,text="\nTotal: "+str(bookdict['total']) +"\tAvailable: "+str(bookdict['available']),font=GUI.content_font)
        total1.pack(anchor='w')
        total.pack(anchor='w')
        bin=tk.Label(mainbox,text="Bin: "+bookdict['bin'] ,font=GUI.content_font)
        bin.pack(anchor='w')
        brs=""
        for b in bookdict['borrowers']:
            if(b!=""):
                brs+=" , "+b
            
        borrowers=tk.Label(mainbox,text="Borrowers: "+brs ,font=GUI.content_font)
        borrowers.pack(anchor='w')
  
  
    def student_book_component_return(self,frame,bookdict,BookID,roll,func):
        mainbox=tk.Frame(frame,border=1,relief='solid')
        mainbox.pack(fill='x',pady=5,padx=10)
        
       
        def returnBookFunction(bookId,roll):
            self.bookObj.returnBook(bookId,roll)
            func()

        button12 = tk.Button(mainbox, text="Return",font=GUI.button_font,bg="#bd2d2d", fg="white",
                                activebackground="#f12d2d", activeforeground="white", padx=10,pady=5, bd=0
                                ,command=lambda: returnBookFunction(BookID,roll))
        button12.pack( pady=10,side='right',padx=30)

        title=tk.Label(mainbox,text=bookdict['name'],font=GUI.label_font)
        title.pack(anchor="w")    


        author=tk.Label(mainbox,text="by "+bookdict['author'],font=GUI.content_font)
        author.pack(anchor='w')

        total1=tk.Label(mainbox,text="Book ID: "+BookID,font=GUI.content_font)
        total=tk.Label(mainbox,text="\nTotal: "+bookdict['total'] +"\tAvailable: "+str(bookdict['available']),font=GUI.content_font)
        total1.pack(anchor='w')
        total.pack(anchor='w')
        bin=tk.Label(mainbox,text="Bin: "+bookdict['bin'] ,font=GUI.content_font)
        bin.pack(anchor='w')

        

  
    def student_book_component_view(self,frame,bookdict,BookID,roll,display_books_function):
        mainbox=tk.Frame(frame,border=1,relief='solid')
        mainbox.pack(fill='x',pady=5,padx=10)
        
        def borrowBookFunction(bookId,roll):
            self.bookObj.borrowBook(bookId,roll)
            display_books_function()   
            

        button112 = tk.Button(mainbox, text="Borrow",font=GUI.button_font,bg="#4CAF50", fg="white",
                                activebackground="#f12d2d", activeforeground="white", padx=10,pady=5, bd=0
                                ,command=lambda: borrowBookFunction(BookID,roll))
        button112.pack( pady=10,side='right',padx=30)

        title=tk.Label(mainbox,text=bookdict['name'],font=GUI.label_font)
        title.pack(anchor="w")

        author=tk.Label(mainbox,text="by "+bookdict['author'],font=GUI.content_font)
        author.pack(anchor='w')
       

        total1=tk.Label(mainbox,text="Book ID: "+BookID,font=GUI.content_font)
        total=tk.Label(mainbox,text="\nTotal: "+bookdict['total'] +"\tAvailable: "+str(bookdict['available']),font=GUI.content_font)
        total1.pack(anchor='w')
        total.pack(anchor='w')
        bin=tk.Label(mainbox,text="Bin: "+bookdict['bin'] ,font=GUI.content_font)
        bin.pack(anchor='w')
        
#===============================================================================================================================================


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
        
        bookHistory_button = tk.Button(side_panel, text="Book History", font=GUI.button_font, bg="#4CAF50", fg="white", 
                                    activebackground="#45a049", activeforeground="white", command=lambda: switch_frame(bookHistory,'bookHistory'), bd=0)
        bookHistory_button.pack(fill="x", pady=10)

        def logout():
            self.welcome_page()
            

        logout_button = tk.Button(side_panel, text="Log Out", font=GUI.button_font,bg="#bd2d2d", fg="white",
                                activebackground="#f12d2d", activeforeground="white", command=logout, bd=0)
        logout_button.pack(fill="x", pady=10)





#==============================================================================================================================

        #TABS CONTENT
        viewBooks= tk.Frame(main_content, bg="#f5f5f5")
        addBooks = tk.Frame(main_content, bg="#f5f5f5")
        delBooks = tk.Frame(main_content, bg="#f5f5f5")
        addMembers = tk.Frame(main_content, bg="#f5f5f5")
        delMembers = tk.Frame(main_content, bg="#f5f5f5")
        bookHistory = tk.Frame(main_content, bg="#f5f5f5")
        
        for frame in (viewBooks,addBooks,addMembers,delBooks,delMembers,bookHistory):
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


        def search():

            search_type=dropdown_var.get()
            required_items=[]
            if(search_type=="Author"):
               
                aut=entry.get().strip()
                
                if not aut :
                    GUI.alert("Error","Seach field is empty!")
                    return
                for i in self.bookObj.bookDetails.keys():
                    if aut.strip().lower() in self.bookObj.bookDetails[i]['author'].lower():
                        required_items.append((i,self.bookObj.bookDetails[i]))
                
                c=0
                for i in viewBooks_frame.winfo_children():
                    if c==0:
                        c=1
                        continue
                    i.destroy()
                if len(required_items)==0:
                    GUI.alert("...","No Results Found!")
                else:
                    for items in required_items:        
                        self.admin_book_component(viewBooks_frame,items[1],items[0])


            elif(search_type=="Title"):
               
                aut=entry.get().strip()
                
                if not aut :
                    GUI.alert("Error","Seach field is empty!")
                    return
                for i in self.bookObj.bookDetails.keys():
                    if aut.strip().lower() in self.bookObj.bookDetails[i]['name'].lower():
                        required_items.append((i,self.bookObj.bookDetails[i]))
                
                c=0
                for i in viewBooks_frame.winfo_children():
                    if c==0:
                        c=1
                        continue
                    i.destroy()
                
                if len(required_items)==0:
                    GUI.alert("...","No Results Found!")               
                else:
                    for items in required_items:        
                        self.admin_book_component(viewBooks_frame,items[1],items[0])
                
            
            else:
                GUI.alert("ERROR","Something Went Wrong!")
                return


        viewBooks_search_frame = tk.Frame(viewBooks_frame)
        viewBooks_search_frame.pack(pady=20) 

        label = tk.Label(viewBooks_search_frame, text="Search by ", font=GUI.label_font)
        label.pack(side=tk.LEFT, padx=5)

        dropdown_var = tk.StringVar(viewBooks_search_frame)
        dropdown_var.set("Title") 
        
        options = ["Title" , "Author"]
        dropdown_menu = tk.OptionMenu(viewBooks_search_frame, dropdown_var, *options)
        dropdown_menu.pack(side=tk.LEFT,pady=10)
        dropdown_menu.config(font=GUI.button_font,
                                 padx=2, bd=1)

        entry = tk.Entry(viewBooks_search_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry.pack(side=tk.LEFT, padx=5)

        search_button = tk.Button(viewBooks_search_frame, text="Search", command=search,font=GUI.button_font, bg="#4CAF50", fg="white",
                                activebackground="#45a049", activeforeground="white", padx=2, bd=0)
        search_button.pack(side=tk.LEFT, padx=5)


        def display_books_function(dict):
            c=0
            for i in viewBooks_frame.winfo_children():
                if c==0:
                    c=1
                    continue
                i.destroy()
            for bookID in dict.keys():
                self.admin_book_component(viewBooks_frame,dict[bookID],bookID)

        
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

        def submit_form1():
            book_id = entry_book_id1.get()
            name = entry_name1.get()
            author = entry_author1.get()
            total = entry_total1.get()
            available = entry_available1.get()
            binNO = entry_bin1.get()
           

            if not (book_id and name and author and binNO and total.isdigit() and available.isdigit()):
                messagebox.showerror("Input Error", "Please enter valid details in all fields!")
                return

            self.bookObj.addBook({book_id:{'name':name,'author':author,'total':total,'available':available,'bin':binNO,'borrowers':[]}})    
            entry_bin1.delete(0,tk.END)
            entry_available1.delete(0,tk.END)
            entry_total1.delete(0,tk.END)
            entry_author1.delete(0,tk.END)
            entry_name1.delete(0,tk.END)
            entry_book_id1.delete(0,tk.END)


        header_label = tk.Label(addBooks_frame, text="Add Books", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label.pack(pady=10)

        label_book_id1 = tk.Label(addBooks_frame, text="Book ID:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_book_id1.pack(pady=5)
        entry_book_id1 = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_book_id1.pack(pady=5)

        label_name1 = tk.Label(addBooks_frame, text="Name:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_name1.pack(pady=5)
        entry_name1 = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_name1.pack(pady=5)

        label_author1 = tk.Label(addBooks_frame, text="Author:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_author1.pack(pady=5)
        entry_author1 = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_author1.pack(pady=5)

        label_total1 = tk.Label(addBooks_frame, text="Total Copies:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_total1.pack(pady=5)
        entry_total1 = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_total1.pack(pady=5)

        label_available1 = tk.Label(addBooks_frame, text="Available Copies:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_available1.pack(pady=5)
        entry_available1 = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_available1.pack(pady=5)
      
        label_bin1 = tk.Label(addBooks_frame, text="Bin Number:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_bin1.pack(pady=5)
        entry_bin1 = tk.Entry(addBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_bin1.pack(pady=5)

        submit_button1 = tk.Button(addBooks_frame, text="Submit", font=GUI.button_font, bg="#4CAF50", fg="white",
                                activebackground="#45a049", activeforeground="white", padx=20, pady=10, bd=0, 
                                command=submit_form1)
        submit_button1.pack(pady=20)



        




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


        def submit_form():
            book_id = entry_book_id.get()
           

            if not (book_id):
                messagebox.showerror("Input Error", "Please enter valid details in all fields!")
                return
            answer = messagebox.askyesno("Careful!","Are you sure you want to remove the book with ID: "+str(book_id))
            if answer==True:
                self.bookObj.removeBook(book_id)   
            entry_book_id.delete(0,tk.END)

        header_label = tk.Label(delBooks_frame, text="Remove a Book", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label.pack(pady=10)

        label_book_id = tk.Label(delBooks_frame, text="Book ID:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_book_id.pack(pady=5)
        entry_book_id = tk.Entry(delBooks_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_book_id.pack(pady=5)


        submit_button = tk.Button(delBooks_frame, text="Remove", font=GUI.button_font, bg="#bd2d2d", fg="white",
                                activebackground="#f12d2d", activeforeground="white", padx=20, pady=10, bd=0, 
                                command=submit_form)
        submit_button.pack(pady=20)


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



        header_label = tk.Label(addMembers_frame, text="Add a Member", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label.pack(pady=10)

        label_roll = tk.Label(addMembers_frame, text="Roll Number:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_roll.pack(pady=5)
        entry_roll2 = tk.Entry(addMembers_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_roll2.pack(pady=5)
        
        label_name = tk.Label(addMembers_frame, text="Full Name:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_name.pack(pady=5)
        entry_name2 = tk.Entry(addMembers_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_name2.pack(pady=5)
        
        label_password = tk.Label(addMembers_frame, text="Password:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_password.pack(pady=5)
        entry_password2 = tk.Entry(addMembers_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_password2.pack(pady=5)


        def submit_form_1():
            name=entry_name2.get()
            roll=entry_roll2.get().upper()
            pswd=entry_password2.get()
            self.membersObj.addMember({ roll : { 'name':name , 'password':pswd } })
            
            entry_name2.delete(0,tk.END)
            entry_roll2.delete(0,tk.END)
            entry_password2.delete(0,tk.END)
             
            
            

        submit_button = tk.Button(addMembers_frame, text="Add a Member", font=GUI.button_font, bg="#4CAF50", fg="white",
                                activebackground="#45a049", activeforeground="white", padx=20, pady=10, bd=0, 
                                command=submit_form_1)
        submit_button.pack(pady=20)


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


        header_label = tk.Label(delMembers_frame, text="Remove a Member", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label.pack(pady=10)

        label_roll = tk.Label(delMembers_frame, text="Roll Number:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_roll.pack(pady=5)
        entry_roll6 = tk.Entry(delMembers_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_roll6.pack(pady=5)

        def submit_form2():
            self.membersObj.removeMember(entry_roll6.get().upper())
            entry_roll6.delete(0,tk.END)

        submit_button = tk.Button(delMembers_frame, text="Remove", font=GUI.button_font, bg="#bd2d2d", fg="white",
                                activebackground="#45a049", activeforeground="white", padx=20, pady=10, bd=0, 
                                command=submit_form2)
        submit_button.pack(pady=20)



#==============================================================================================================================
        





        #delMembers Frame
        bookHistory_canvas = tk.Canvas(bookHistory)
        bookHistory_canvas.pack(fill="both", expand=True, side="left")

        bookHistory_scrollBar = tk.Scrollbar(bookHistory, orient="vertical", command=bookHistory_canvas.yview)
        bookHistory_scrollBar.pack(side="right", fill="y")

        bookHistory_canvas.configure(yscrollcommand=bookHistory_scrollBar.set)

        bookHistory_frame = tk.Frame(bookHistory_canvas)
        bookHistory_canvas.create_window((0, 0), anchor="nw", window=bookHistory_frame)

        def on_frame_configure(event):
            bookHistory_canvas.configure(scrollregion=bookHistory_canvas.bbox("all"))

        bookHistory_frame.bind("<Configure>", on_frame_configure)

        def on_canvas_configure(event):
            bookHistory_canvas.itemconfig(bookHistory_canvas.create_window((0, 0), anchor='nw', window=bookHistory_frame), width=event.width)

        bookHistory_canvas.bind("<Configure>", on_canvas_configure)
        
        #now you can use bookHistory_frame as your main frame

        header_label33 = tk.Label(bookHistory_frame, text="Book Borrowing History", font=GUI.header_font, bg="#f5f5f5", fg="#333333")
        header_label33.pack(pady=10)

        label_roll33 = tk.Label(bookHistory_frame, text="Book ID:", font=GUI.label_font, bg="#f5f5f5", fg="#555555")
        label_roll33.pack(pady=5)
        entry_bkid = tk.Entry(bookHistory_frame, font=GUI.input_font, width=30, bd=1, relief="solid")
        entry_bkid.pack(pady=5)

        def clear_bookHistory():
            j=0    

            

            for i in bookHistory_frame.winfo_children():
                if j<=3:
                    j+=1
                    continue
                
                i.destroy()


        def view_book_history():
            bkid=entry_bkid.get()
            clear_bookHistory()    

            
            try:
                history_list=self.bookObj.bookHistory[bkid]
                
                mainbox=tk.Frame(bookHistory_frame,border=1,relief='solid')
                mainbox.pack(fill='x',pady=5,padx=10)
                
                tk.Label(mainbox, text="Roll Number", font=GUI.content_font, bg="#f5f5f5", fg="#333333").grid(row=1,column=1,pady=5)
                tk.Label(mainbox, text="Date Issued", font=GUI.content_font, bg="#f5f5f5", fg="#333333").grid(row=1,column=2,pady=5)
                tk.Label(mainbox, text="Date Returned", font=GUI.content_font, bg="#f5f5f5", fg="#333333").grid(row=1,column=3,pady=5)
                mainbox.columnconfigure((1,2,3),weight=1)
                
                i=2
                for item in history_list:
                    tk.Label(mainbox, text=list(item.keys())[0], font=GUI.content_font, bg="#f5f5f5", fg="#333333").grid(row=i,column=1,pady=5)
                    tk.Label(mainbox, text=item[list(item.keys())[0]][0], font=GUI.content_font, bg="#f5f5f5", fg="#333333").grid(row=i,column=2,pady=5)
                    tk.Label(mainbox, text=item[list(item.keys())[0]][1], font=GUI.content_font, bg="#f5f5f5", fg="#333333").grid(row=i,column=3,pady=5)
                    i+=1

            except KeyError:
                self.alert("Error","History does not exist for this bookID")            
            except:
                self.alert("Error","Something Went Wrong!")

        submit_button33 = tk.Button(bookHistory_frame, text="View", font=GUI.button_font, bg="#4CAF50", fg="white",
                                activebackground="#45a049", activeforeground="white", padx=20, pady=10, bd=0, 
                                command=view_book_history)
        submit_button33.pack(pady=20)
        






#=================================================================================================================================================================

        def switch_frame(frame,button):
            viewBooks.pack_forget()
            addBooks.pack_forget()
            delBooks.pack_forget()
            addMembers.pack_forget()
            delMembers.pack_forget()
            bookHistory.pack_forget()
            viewBooks_button.configure(bg='#45a049')
            addBooks_button.configure(bg='#45a049')
            delBooks_button.configure(bg='#45a049')
            addMembers_button.configure(bg='#45a049')
            delMembers_button.configure(bg='#45a049')
            bookHistory_button.configure(bg='#45a049')
            entry_bkid.delete(0,tk.END)
            clear_bookHistory()

            if button=="viewBooks":
                display_books_function(self.bookObj.bookDetails)

            frame.pack(fill="both", expand=True)
            exec( f"{button}_button.configure(bg='#215c52')")
            

        switch_frame(viewBooks,'viewBooks')

#===============================================================================================================================================

    @staticmethod
    def alert(title,message):    
        messagebox.showerror(title, message)

#===============================================================================================================================================


    @staticmethod
    def success(title,message):
        messagebox.showinfo(title,message) 
