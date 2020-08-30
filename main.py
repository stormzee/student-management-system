try:
    from tkinter import *
except ImportError:
    ImportError

try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

try:
    import mysql.connector
except Exception as error:
    print(error)
else:
    pass

class Main_win:
    def __init__(self,top=None):
        '''This class configures and pop    ulates the toplevel window.
           top is the toplevel containing window.'''
        
        font11 = "-family Verdana -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font12 = "-family Verdana -size 11 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.317, rely=0.044, relheight=0.878
                , relwidth=0.002)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ececec")
        # insert button widget
        self.Button1 = Button(top, command=self.insert)
        self.Button1.place(relx=0.067, rely=0.222, height=34, width=87)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ff9797")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font11)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''Insert''')
        # Search button widget
        self.Button2 = Button(top, command=self.search)
        self.Button2.place(relx=0.067, rely=0.451, height=34, width=87)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#ff9797")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font11)
        self.Button2.configure(foreground="#ffffff")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(relief="groove")
        self.Button2.configure(text='''Search''')
        # Delete button widget
        self.Button3 = Button(top, command=self.delete)
        self.Button3.place(relx=0.067, rely=0.689, height=34, width=87)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#ff9797")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font11)
        self.Button3.configure(foreground="#ffffff")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(relief="groove")
        self.Button3.configure(text='''Delete''')
        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.383, rely=0.2, relheight=0.611, relwidth=0.542)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#8178e4")
        # student_id entry widget
        self.student_id = StringVar()
        self.Entry1 = Entry(self.Frame2, textvariable= self.student_id)
        self.Entry1.place(relx=0.462, rely=0.196,height=30, relwidth=0.505)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font12)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.focus()
        # name entry widget
        self.name = StringVar()
        self.Entry1_1 = Entry(self.Frame2, textvariable= self.name)
        self.Entry1_1.place(relx=0.462, rely=0.495,height=30, relwidth=0.505)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font=font12)
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="#c4c4c4")
        self.Entry1_1.configure(selectforeground="black")
        # class entry widget
        self.class_select = StringVar()
        self.Entry1_2 = ttk.Combobox(self.Frame2,values=("p1","p2","p3","p4","p5","p6","JHS1","JHS2","JHS3"), textvariable=self.class_select)
        self.Entry1_2.place(relx=0.462, rely=0.796,height=30, relwidth=0.505)
        self.Entry1_2.configure(background="white")
        # self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font=font12)
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.current(0)
        self.Label1 = Label(self.Frame2)
        self.Label1.place(relx=0.148, rely=0.2, height=31, width=94)
        self.Label1.configure(background="#8178e4")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font12)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''School ID''')
        self.Label1_3 = Label(self.Frame2)
        self.Label1_3.place(relx=0.231, rely=0.491, height=31, width=54)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#8178e4")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font=font12)
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''Name''')
        self.Label1_4 = Label(self.Frame2)
        self.Label1_4.place(relx=0.237, rely=0.796, height=31, width=64)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#8178e4")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(font=font12)
        self.Label1_4.configure(foreground="#000000")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''Class''')
        self.Label2 = Label(top)
        self.Label2.place(relx=0.408, rely=0.022, height=71, width=134)
        self.Label2.configure(background="#8178e4")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self._img0 = PhotoImage(file='school_96px.png')
        self.Label2.configure(image=self._img0)

    # setup a db connection
        self.host = "localhost"
        self.password = ""
        self.user = "root"
        self.database = "stdntdb"
        try:
            # self.Dbconnec = mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            # self.cursor = self.Dbconnec.cursor()
            # first connect to the database server by creating a connection
            # create a cursor to navigate through the db
            # create a database and connect to that db created
            self.Dbconnec = mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            self.cursor = self.Dbconnec.cursor()
            self.cursor.execute("create table if not exists student_info (school_ID varchar(10), name varchar(255), class varchar(10))")
            # self.curs.close
            # create table if not exist students ()
        except Exception as error:
            print(error)
        else:
            print("connection established")
    
    def insert(self):
        self.query = ("insert into student_info (school_ID,name,class)" "values (%s,%s,%s)")
        self.cursor.execute(self.query,(self.student_id.get(),self.name.get(),self.class_select.get()))
        self.Dbconnec.commit()
        self.Entry1.delete(0,END)
        self.Entry1_1.delete(0,END)
        self.Entry1_2.delete(0,END)
        print("Insertion done")

    def delete(self):
        self.query = "DELETE school_ID,name,class FROM student_info WHERE name = %s" %(self.student_id.get())
        self.cursor.execute(self.query)
        self.Dbconnec.commit()
        self.cursor.close()
        print("Record deleted successfully")
        pass

    def search(self):
        self.Entry1_1.delete(0,END)
        self.Entry1_2.delete(0,END)
        self.query = """SELECT name,class FROM student_info WHERE school_ID = %s""" %(self.student_id.get())
        self.cursor.execute(self.query)
        # self.results contains all the resultset in one row.
        # so we can use row indexing to print the individual tuples in the resultset
        self.results = self.cursor.fetchall()
        self.output_1 = ""
        self.output_2 = ""
        for row in self.results:
            self.output_1 = ''.join(row[0])
            self.output_2 = ''.join(row[1])
        self.Entry1_1.insert(0,self.output_1)
        self.Entry1_2.insert(0,self.output_2)


# main function to 
def main():
    # App()
    win = Tk()
    top = Main_win(win)
    win.geometry("600x450+338+162")
    win.resizable(1, 1)
    win.title("Student Management System")
    # top.configure(relief="ridge")
    win.configure(background="#8178e4")
    win.mainloop()
    

if __name__ == '__main__':
        main()