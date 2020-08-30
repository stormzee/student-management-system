# importing relevant Packages

try:
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter import Menu,Menubutton
    from main import Main_win
except Exception as error:
    print(error)
else:
    pass
try:
    from main import Main_win
except ImportError as Error:
    print(Error)

# creating the gui window.

class App:
    # create and configure the widgets for the app
    def __init__(self, root=None):
        self.root = root
        self.image_label = PhotoImage(file="login_48px.png")
        self.loginUI_image = PhotoImage(file="manager_80px.png")
        self.main_win = ttk.Frame(self.root)
        self.main_win.grid()
        self.login_logo = ttk.Label(self.main_win)
        self.login_logo.grid(row=0, column=3, padx=70, pady=20)
        self.login_logo.configure(image=self.loginUI_image)
        self.user_label = ttk.Label(self.main_win, text='Username')
        self.user_label.grid(row=1, column=2, padx=40, pady=10)
        self.user_label.configure(font='Arial 12 bold')
        self.pswd_label = ttk.Label(self.main_win, text='Password')
        self.pswd_label.grid(row=2, column=2, padx=40, pady=10)
        self.pswd_label.configure(font='Arial 12 bold')
        self.login_label = ttk.Label(self.main_win, text='Login')
        self.login_label.grid(row=3, column=3, sticky=W, padx=5)
        self.login_label.configure(font='Arial 12 bold')

        # creating the entry fields

        self.name = StringVar()
        self.name_entry = ttk.Entry(self.main_win,textvariable=self.name)
        self.name_entry.grid(row=1, column=3, sticky=EW, ipady=3, ipadx=5)
        self.name_entry.configure( font='Arial 12 bold')
        self.name_entry.focus()
        self.pswd = StringVar()
        self.pswd_entry = ttk.Entry(self.main_win,textvariable=self.pswd)
        self.pswd_entry.grid(row=2, column=3, sticky=EW, ipady=3, ipadx=5)
        self.pswd_entry.configure( font='Arial 12 bold', show="*")
        # self.main_win.configure(background='#d2b9e9')
        # creating a login logo
        # creating buttons
        self.Login_btn = ttk.Button(self.main_win, text='Login',command=self.login_validate)
        self.Login_btn.grid(row=3, column=3, padx=70)
        self.Login_btn.configure(image=self.image_label)
        
    def login_validate(self):
        if self.name.get()=="Admin" and self.pswd.get()=="Adminpass" and self.name.get()!="" and self.pswd.get()!="":
            messagebox.showinfo("Login Successful",message=self.name.get()+" , Access Granted")
            self.root.destroy()
            # self.main_win.destroy()
            Main_win()
            
        else:
            messagebox.showerror("Error",message="Wrong Username and Password")
            self.name_entry.delete(0,END)
            self.pswd_entry.delete(0,END)

def main():
    global root
    root = Tk()
    login_page = App(root)
    root.title('login')
    root.geometry("500x300+338+162")
    # root.maxsize(1370, 749)
    root.resizable(1, 1)
    root.mainloop()

# the main function to run the program
if __name__ == "__main__":
    # Main_win()
    main()
