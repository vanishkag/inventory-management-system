from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class empclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Vanishka")
        self.root.config(bg="#f5f0e1")
        self.root.focus_force()
        # all variables
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_empid=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()

        
        #search
        searchfr=LabelFrame(self.root,text="Search Employee",fg="black",bg="#f5f0e1",font=("arial",12,"bold"))
        searchfr.place(x=250,y=20,width=600,height=70)

        #options
        cmb_search=ttk.Combobox(searchfr,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("arial",10))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(searchfr,textvariable=self.var_searchtxt,font=("arial",10),bg="#f5f0e1").place(x=200,y=10)
        btn_search=Button(searchfr,text="Search",command=self.search,font=("arial",10),bg="blue",fg="black",cursor="hand2").place(x=350,y=7,width=150,height=25)

        #title
        title=Label(self.root,text="Employee Deatils",bg="white",fg="black",font=("arial",15)).place(x=50,y=100,width=1000)

        #content
        #row1
        lbl_empid=Label(self.root,text="EmpID",bg="white",fg="black",font=("arial",15)).place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",bg="white",fg="black",font=("arial",15)).place(x=350,y=150)
        lbl_contact=Label(self.root,text="Contact",bg="white",fg="black",font=("arial",15)).place(x=750,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_empid,bg="white",fg="black",font=("arial",15)).place(x=150,y=150,width=180)
        txt_gender=Entry(self.root,textvariable=self.var_gender,bg="white",fg="black",font=("arial",15)).place(x=500,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("arial",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,bg="white",fg="black",font=("arial",15)).place(x=850,y=150,width=180)

        #row2

        lbl_name=Label(self.root,text="Name",bg="white",fg="black",font=("arial",15)).place(x=50,y=190)
        lbl_dob=Label(self.root,text="DOB",bg="white",fg="black",font=("arial",15)).place(x=350,y=190)
        lbl_doj=Label(self.root,text="DOJ",bg="white",fg="black",font=("arial",15)).place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,bg="white",fg="black",font=("arial",15)).place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,bg="white",fg="black",font=("arial",15)).place(x=500,y=190,width=180)       
        txt_doj=Entry(self.root,textvariable=self.var_doj,bg="white",fg="black",font=("arial",15)).place(x=850,y=190,width=180)

        #row3

        lbl_email=Label(self.root,text="Email",bg="white",fg="black",font=("arial",15)).place(x=50,y=230)
        lbl_pass=Label(self.root,text="Password",bg="white",fg="black",font=("arial",15)).place(x=350,y=230)
        lbl_utype=Label(self.root,text="User Type",bg="white",fg="black",font=("arial",15)).place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,bg="white",fg="black",font=("arial",15)).place(x=150,y=230,width=180)
        txt_pass=Entry(self.root,textvariable=self.var_pass,bg="white",fg="black",font=("arial",15)).place(x=500,y=230,width=180)       
        txt_utype=Entry(self.root,textvariable=self.var_utype,bg="white",fg="black",font=("arial",15)).place(x=850,y=230,width=180)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("arial",15))
        cmb_utype.place(x=850,y=230,width=180)
        cmb_utype.current(0)

        #row4

        lbl_address=Label(self.root,text="Address",bg="white",fg="black",font=("arial",15)).place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",bg="white",fg="black",font=("arial",15)).place(x=500,y=270)

        self.txt_address=Text(self.root,bg="white",fg="black",font=("arial",15))
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,bg="white",fg="black",font=("arial",15)).place(x=600,y=270,width=180)

        #buttons
        btn_add=Button(self.root,text="Save",command=self.add,font=("arial",10),bg="blue",fg="black",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="Update",command=self.update,font=("arial",10),bg="blue",fg="black",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("arial",10),bg="blue",fg="black",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("arial",10),bg="blue",fg="black",cursor="hand2").place(x=860,y=305,width=110,height=28)
        
        #employee details
        emp_frame=Frame(self.root)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.empclass=ttk.Treeview(emp_frame,columns=("Empid","Name","Email","Gender","Contact","DOB","DOJ","Password","Utype","Address","Salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side='bottom',fill=X)
        scrolly.pack(side='right',fill=Y)
        scrollx.config(command=self.empclass.xview)
        scrolly.config(command=self.empclass.yview)
        self.empclass.heading("Empid",text="Empid")
        self.empclass.heading("Name",text="Name")
        self.empclass.heading("Email",text="Email")
        self.empclass.heading("Gender",text="Gender")
        self.empclass.heading("Contact",text="Contact")
        self.empclass.heading("DOB",text="DOB")
        self.empclass.heading("DOJ",text="DOJ")
        self.empclass.heading("Password",text="Password")
        self.empclass.heading("Utype",text="Utype")
        self.empclass.heading("Address",text="Address")
        self.empclass.heading("Salary",text="Salary")

        self.empclass["show"] = "headings"

        self.empclass.column("Empid",width=90)
        self.empclass.column("Name",width=100)
        self.empclass.column("Email",width=100)
        self.empclass.column("Gender",width=100)
        self.empclass.column("Contact",width=100)
        self.empclass.column("DOB",width=100)
        self.empclass.column("DOJ",width=100)
        self.empclass.column("Password",width=100)
        self.empclass.column("Utype",width=100)
        self.empclass.column("Address",width=100)
        self.empclass.column("Salary",width=100)
        self.empclass.pack(fill=BOTH, expand=1)
        self.empclass.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#funcs start
    def add(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_empid.get()=="":
                messagebox.showerror("Error", "Employee ID is required",parent=self.root)

            else:
                cur.execute("select * from employee where Empid=%s",(self.var_empid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This employee ID is already assigned, use a different one",parent=self.root)

                else:
                    cur.execute("Insert into employee( Empid , Name , Email , Gender , Contact , DOB , DOJ , Password , Utype , Address , Salary ) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_empid.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),                        
                        self.var_salary.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()

    def show(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.empclass.delete(*self.empclass.get_children())
            for row in rows:
                self.empclass.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.empclass.focus()
        content=(self.empclass.item(f))
        row=content['values']
        self.var_empid.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])                       
        self.var_salary.set(row[10])

    def update(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_empid.get()=="":
                messagebox.showerror("Error", "Employee ID is required",parent=self.root)

            else:
                cur.execute("select * from employee where Empid=%s",(self.var_empid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee id",parent=self.root)

                else:
                    cur.execute("update employee set Name=%s , Email=%s , Gender=%s , Contact=%s , DOB=%s , DOJ=%s , Password=%s , Utype=%s , Address=%s , Salary=%s where Empid=%s",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get('1.0',END),                        
                        self.var_salary.get(),
                        self.var_empid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee updated successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()

    def delete(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_empid.get()=="":
                messagebox.showerror("Error", "Employee ID is required",parent=self.root)

            else:
                cur.execute("select * from employee where Empid=%s",(self.var_empid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid employee id",parent=self.root)

                else:
                    op=messagebox.askyesno("Confirm","Are you sure?",parent=self.root)
                    if op==True:
                        cur.execute("delete from employee where Empid=%s",(self.var_empid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()
    
    def clear(self):
        self.var_empid.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("")
        self.txt_address.delete('1.0',END)                       
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("")
        self.show()

    def search(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Select input is required",parent=self.root)
            elif self.var_searchby.get()=="Email":
                cur.execute("select * from employee where  Email= %s",(self.var_searchtxt.get(),))
                print(self.var_searchtxt.get())
                rows=cur.fetchall()
                if(len(rows)==0):
                    messagebox.showerror("Error","No record found",parent=self.root)   
                         
                else:
                    messagebox.showinfo("Success","Record Found",parent=self.root)

                    self.empclass.delete(*self.empclass.get_children())
                    for row in rows:
                        self.empclass.insert('',END,values=row)
            elif self.var_searchby.get()=="Name":
                cur.execute("select * from employee where  Name= %s",(self.var_searchtxt.get(),))
                print(self.var_searchtxt.get())
                rows=cur.fetchall()
                if(len(rows)==0):
                    messagebox.showerror("Error","No record found",parent=self.root)   
                         
                else:
                    self.empclass.delete(*self.empclass.get_children())
                    for row in rows:
                        self.empclass.insert('',END,values=row)
            elif self.var_searchby.get()=="Contact":
                cur.execute("select * from employee where  Contact= %s",(self.var_searchtxt.get(),))
                print(self.var_searchtxt.get())
                rows=cur.fetchall()
                if(len(rows)==0):
                    messagebox.showerror("Error","No record found",parent=self.root)   
                         
                else:
                    self.empclass.delete(*self.empclass.get_children())
                    for row in rows:
                        self.empclass.insert('',END,values=row)
            con.commit

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()
if __name__=="__main__":
    root = Tk()
    obj = empclass(root)
    root.mainloop()