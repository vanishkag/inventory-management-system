from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class catclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Vanishka")
        self.root.config(bg="#f5f0e1")
        self.root.focus_force()

        self.var_catid=StringVar()
        self.var_name=StringVar()

        #title
        lbl_title=Label(self.root,text="Manage Product Categories", font=("arial",30),bg="white",fg="black").pack(side=TOP,fill=X)
        lbl_name=Label(self.root,text="Enter Category", font=("arial",30),bg="white",fg="black").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name, font=("arial",18),bg="white",fg="black").place(x=50,y=170,width=300)
  
        btn_add=Button(self.root,text="Add",command=self.add, font=("arial",15),bg="white",fg="black",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete, font=("arial",15),bg="white",fg="black",cursor="hand2").place(x=520,y=170,width=150,height=30)

        #category details
        cat_frame=Frame(self.root)
        cat_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.catclass=ttk.Treeview(cat_frame,columns=("CId","Name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side='bottom',fill=X)
        scrolly.pack(side='right',fill=Y)
        scrollx.config(command=self.catclass.xview)
        scrolly.config(command=self.catclass.yview)
        self.catclass.heading("CId",text="CId")
        self.catclass.heading("Name",text="Name")

        self.catclass["show"] = "headings"

        self.catclass.column("CId",width=90)
        self.catclass.column("Name",width=100)
        self.catclass.pack(fill=BOTH, expand=1)
        self.catclass.bind("<ButtonRelease-1>",self.get_data)
        self.show()
    def add(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error", "Category is required",parent=self.root)

            else:
                cur.execute("select * from category where Name=%s",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Category already exists, use a different one",parent=self.root)

                else:
                    cur.execute("Insert into category(Name) values(%s)",(
                        self.var_name.get(),                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Category added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()

    def show(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.catclass.delete(*self.catclass.get_children())
            for row in rows:
                self.catclass.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.catclass.focus()
        content=(self.catclass.item(f))
        row=content['values']
        self.var_catid.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_catid.get()=="":
                messagebox.showerror("Error", "Category Id is required",parent=self.root)

            else:
                cur.execute("select * from category where CId=%s",(self.var_catid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Category ID",parent=self.root)

                else:
                    op=messagebox.askyesno("Confirm","Are you sure?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where CId=%s",(self.var_catid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category deleted successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()

if __name__=="__main__":
    root = Tk()
    obj = catclass(root)
    root.mainloop()