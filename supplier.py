from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class suppclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Vanishka")
        self.root.config(bg="#f5f0e1")
        self.root.focus_force()
        # all variables

        self.var_suppinvoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        

        #title
        title=Label(self.root,text="Supplier Deatils",bg="white",fg="black",font=("arial",15)).place(x=50,y=100,width=1000)

        #content
        #row1
        lbl_suppin=Label(self.root,text="Invoice No",bg="white",fg="black",font=("arial",15)).place(x=50,y=150)
        txt_suppin=Entry(self.root,textvariable=self.var_suppinvoice,bg="white",fg="black",font=("arial",15)).place(x=150,y=150,width=180)
    
        #row2

        lbl_name=Label(self.root,text="Name",bg="white",fg="black",font=("arial",15)).place(x=50,y=190)
        txt_name=Entry(self.root,textvariable=self.var_name,bg="white",fg="black",font=("arial",15)).place(x=150,y=190,width=180)

        #row3

        lbl_contact=Label(self.root,text="Contact",bg="white",fg="black",font=("arial",15)).place(x=50,y=230)
        txt_contact=Entry(self.root,textvariable=self.var_contact,bg="white",fg="black",font=("arial",15)).place(x=150,y=230,width=180)

        #row4

        lbl_desc=Label(self.root,text="Description",bg="white",fg="black",font=("arial",15)).place(x=50,y=270)
        self.txt_desc=Text(self.root,bg="white",fg="black",font=("arial",15))
        self.txt_desc.place(x=150,y=270,width=300,height=60)

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

        self.suppclass=ttk.Treeview(emp_frame,columns=("Invoice","Name","Contact","Description"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side='bottom',fill=X)
        scrolly.pack(side='right',fill=Y)
        scrollx.config(command=self.suppclass.xview)
        scrolly.config(command=self.suppclass.yview)
        self.suppclass.heading("Invoice",text="Invoice")
        self.suppclass.heading("Name",text="Name")
        self.suppclass.heading("Contact",text="Contact")
        self.suppclass.heading("Description",text="Description")

        self.suppclass["show"] = "headings"

        self.suppclass.column("Invoice",width=90)
        self.suppclass.column("Name",width=100)
        self.suppclass.column("Contact",width=100)
        self.suppclass.column("Description",width=100)
        self.suppclass.pack(fill=BOTH, expand=1)
        self.suppclass.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#funcs start
    def add(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_suppinvoice.get()=="":
                messagebox.showerror("Error", "Invoice no is required",parent=self.root)

            else:
                cur.execute("select * from supplier where Invoice=%s",(self.var_suppinvoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice No already exists, use a different one",parent=self.root)

                else:
                    cur.execute("Insert into supplier(Invoice, Name, Contact, Description ) values(%s,%s,%s,%s)",(
                        self.var_suppinvoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()

    def show(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.suppclass.delete(*self.suppclass.get_children())
            for row in rows:
                self.suppclass.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.suppclass.focus()
        content=(self.suppclass.item(f))
        row=content['values']
        self.var_suppinvoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[4])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[9])                       
        
    def update(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_suppinvoice.get()=="":
                messagebox.showerror("Error", "Invoice No is required",parent=self.root)

            else:
                cur.execute("select * from supplier where Invoice=%s",(self.var_suppinvoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No",parent=self.root)

                else:
                    cur.execute("update supplier set Name=%s ,  Contact=%s , Description=%s where Invoice=%s",(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),                        
                        self.var_suppinvoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier updated successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()

    def delete(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_suppinvoice.get()=="":
                messagebox.showerror("Error", "Invoice No is required",parent=self.root)

            else:
                cur.execute("select * from supplier where Invoice=%s",(self.var_suppinvoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice No",parent=self.root)

                else:
                    op=messagebox.askyesno("Confirm","Are you sure?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where Invoice=%s",(self.var_suppinvoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier deleted successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def clear(self):
        self.var_suppinvoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)                       
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
            else:
                cur.execute("select * from supplier where %s = %s",(self.var_searchby.get(),self.var_searchtxt.get(),))
                print(self.var_searchby.get(),self.var_searchtxt.get())
                rows=cur.fetchall()
                if(len(rows)==0):
                    messagebox.showerror("Error","No record found",parent=self.root)   
                         
                else:
                    self.suppclass.delete(*self.suppclass.get_children())
                for row in rows:
                        self.suppclass.insert('',END,values=row)
                con.commit()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj = suppclass(root)
    root.mainloop()