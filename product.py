from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class proclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Vanishka")
        self.root.config(bg="#f5f0e1")
        self.root.focus_force()

        self.var_pid=StringVar()
        self.var_cat=StringVar()
        self.var_supp=StringVar()
        self.cl=[]
        self.sl=[]
        self.fetch()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stat=StringVar()

        proFrame=Frame(self.root,bg="#f5f0e1")
        proFrame.place(x=10,y=10,width=450,height=480)
       
        #title
        title=Label(proFrame,text="Manage Product Deatils",bg="white",fg="black",font=("arial",18)).pack(side=TOP,fill=X)
        lbl_pid=Label(proFrame,text="ID",bg="white",fg="black",font=("arial",18)).place(x=30,y=60)
        lbl_cat=Label(proFrame,text="Category",bg="white",fg="black",font=("arial",18)).place(x=30,y=110)
        lbl_supp=Label(proFrame,text="Supplier",bg="white",fg="black",font=("arial",18)).place(x=30,y=160)
        lbl_pro=Label(proFrame,text="Name",bg="white",fg="black",font=("arial",18)).place(x=30,y=210)
        lbl_pri=Label(proFrame,text="Price",bg="white",fg="black",font=("arial",18)).place(x=30,y=260)
        lbl_qty=Label(proFrame,text="Qty",bg="white",fg="black",font=("arial",18)).place(x=30,y=310)
        lbl_stat=Label(proFrame,text="Status",bg="white",fg="black",font=("arial",18)).place(x=30,y=360)

        txt_pid=Entry(proFrame,textvariable=self.var_pid,font=("arial",10)).place(x=150,y=60,width=200)


        cmb_cat=ttk.Combobox(proFrame,textvariable=self.var_cat,values=self.cl,state='readonly',justify=CENTER,font=("arial",10))
        cmb_cat.place(x=150,y=110,width=200)
        cmb_cat.current(0)

        cmb_supp=ttk.Combobox(proFrame,textvariable=self.var_supp,values=self.sl,state='readonly',justify=CENTER,font=("arial",10))
        cmb_supp.place(x=150,y=160,width=200)
        cmb_supp.current(0)

        txt_name=Entry(proFrame,textvariable=self.var_name,font=("arial",10)).place(x=150,y=210,width=200)
        txt_pri=Entry(proFrame,textvariable=self.var_price,font=("arial",10)).place(x=150,y=260,width=200)
        txt_qty=Entry(proFrame,textvariable=self.var_qty,font=("arial",10)).place(x=150,y=310,width=200)

        cmb_stat=ttk.Combobox(proFrame,textvariable=self.var_stat,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("arial",10))
        cmb_stat.place(x=150,y=360,width=200)
        cmb_stat.current(0)

        btn_add=Button(proFrame,text="Save",command=self.add,font=("arial",10),bg="blue",fg="black",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(proFrame,text="Update",command=self.update,font=("arial",10),bg="blue",fg="black",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_delete=Button(proFrame,text="Delete",command=self.delete,font=("arial",10),bg="blue",fg="black",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(proFrame,text="Clear",command=self.clear,font=("arial",10),bg="blue",fg="black",cursor="hand2").place(x=340,y=400,width=100,height=40)
#details treeview
        pFrame=Frame(self.root,bg="#f5f0e1")
        pFrame.place(x=480,y=100,width=600,height=390)

        scrolly=Scrollbar(pFrame,orient=VERTICAL)
        scrollx=Scrollbar(pFrame,orient=HORIZONTAL)

        self.proclass=ttk.Treeview(pFrame,columns=("PId","Category","Supplier","Name","Price","Qty","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side='bottom',fill=X)
        scrolly.pack(side='right',fill=Y)
        scrollx.config(command=self.proclass.xview)
        scrolly.config(command=self.proclass.yview)
        self.proclass.heading("PId",text="PId")
        self.proclass.heading("Category",text="Category")
        self.proclass.heading("Supplier",text="Supplier")
        self.proclass.heading("Name",text="Name")
        self.proclass.heading("Price",text="Price")
        self.proclass.heading("Qty",text="Qty")
        self.proclass.heading("Status",text="Status")

        self.proclass["show"] = "headings"

        self.proclass.column("PId",width=90)
        self.proclass.column("Category",width=100)
        self.proclass.column("Supplier",width=100)
        self.proclass.column("Name",width=100)
        self.proclass.column("Price",width=100)
        self.proclass.column("Qty",width=100)
        self.proclass.column("Status",width=100)
        self.proclass.pack(fill=BOTH, expand=1)
        self.proclass.bind("<ButtonRelease-1>",self.get_data)

        self.show()
#funcs
    def fetch(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            cur.execute("select name from category")
            cat=cur.fetchall()
            self.cl.append("Empty")
            if(len(cat)>0):
                del self.cl[:]
                self.cl.append("Select")
                for i in cat:
                    self.cl.append(i[0])
            cur.execute("select name from supplier")
            supp=cur.fetchall()
            self.sl.append("Empty")
            if(len(supp)>0):
                del self.sl[:]
                self.sl.append("Select")
                for i in supp:
                    self.sl.append(i[0])

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
 

    def add(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_supp.get()=="Select" or self.var_name.get()=="" or self.var_cat.get()=="Empty":
                messagebox.showerror("Error", "All fields are required",parent=self.root)

            else:
                cur.execute("select * from product where Name=%s",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This name already exists, use a different one",parent=self.root)

                else:
                    cur.execute("Insert into product( PId ,Category , Supplier , Name , Price , Qty , Status  ) values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_pid.get(),
                        self.var_cat.get(),
                        self.var_supp.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_stat.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product added successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()

    def show(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.proclass.delete(*self.proclass.get_children())
            for row in rows:
                self.proclass.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.proclass.focus()
        content=(self.proclass.item(f))
        row=content['values']
        self.var_pid.set(row[0]),
        self.var_cat.set(row[1]),
        self.var_supp.set(row[2]),
        self.var_name.set(row[3]),
        self.var_price.set(row[4]),
        self.var_qty.set(row[5]),
        self.var_stat.set(row[6]),

    def update(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error", "Product ID is required",parent=self.root)

            else:
                cur.execute("select * from product where PId=%s",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product",parent=self.root)

                else:
                    cur.execute("update product set Category=%s , Supplier=%s , Name=%s , Price=%s , Qty=%s , Status=%s where PId=%s",(
                        self.var_cat.get(),
                        self.var_supp.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_stat.get(),
                        self.var_pid.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product updated successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()

    def delete(self):
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error", "Select product from list ",parent=self.root)

            else:
                cur.execute("select * from product where PId=%s",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product id",parent=self.root)

                else:
                    op=messagebox.askyesno("Confirm","Are you sure?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where PId=%s",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Product deleted successfully",parent=self.root)
                        self.clear()
                        
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        self.show()

    def clear(self):
        self.var_pid.set(""),
        self.var_cat.set("Select"),
        self.var_supp.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_stat.set("Active"),
        self.show()


if __name__=="__main__":
    root = Tk()
    obj = proclass(root)
    root.mainloop()