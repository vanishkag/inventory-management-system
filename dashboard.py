from tkinter import *
from employee import empclass
from supplier import suppclass
from category import catclass
from product import proclass
from sales import saleclass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Vanishka")
        self.root.config(bg="#f5f0e1")

        #title
        self.icon_title = PhotoImage(file="C:\Personal\Minty\inventory management system\icons8-shopping-cart-40.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT, font=("arial",40,"bold"),bg="#1e3d59",fg="#ff6e40", anchor="w",padx=20).place(x=0,y=0,relwidth=1, height = 70)

        #button logout
        #clock
        self.clock=Label(self.root,text="Date: 05-05-2023\t\tTime: 14:15", font=("arial",15),bg="#ff6e40",fg="white")
        self.clock.place(x=0,y=70,relwidth=1, height = 30)

        #left menu
        self.MenuLogo= PhotoImage(file="C:\Personal\Minty\inventory management system\icons8-menu-24.png")
        LMenu = Frame(self.root,relief=RIDGE,bg="#f5f0e1")
        LMenu.place(x=0,y=102,width=200,height=565)
        menu=Label(self.root,text="Menu",image=self.MenuLogo,compound=LEFT, font=("arial",30,"bold"),bg="#010c48",fg="white", anchor="w",padx=20).place(x=0,y=100,width=200, height = 40)
        btn_emp=Button(menu,text="Employee",command=self.employee,font=("arial",15,),bg="#010c48",fg="white", anchor="c",cursor="hand2").place(x=0,y=140,width=200, height = 40)
        btn_supp=Button(menu,text="Supplier",command=self.supplier,font=("arial",15,),bg="#010c48",fg="white", anchor="c",cursor="hand2").place(x=0,y=180,width=200, height = 40)
        btn_cat=Button(menu,text="Category",command=self.category,font=("arial",15,),bg="#010c48",fg="white", anchor="c",cursor="hand2").place(x=0,y=220,width=200, height = 40)
        btn_pro=Button(menu,text="Products",command=self.product,font=("arial",15,),bg="#010c48",fg="white", anchor="c",cursor="hand2").place(x=0,y=260,width=200, height = 40)
        btn_sales=Button(menu,text="Sales",command=self.sales,font=("arial",15,),bg="#010c48",fg="white", anchor="c",cursor="hand2").place(x=0,y=300,width=200, height = 40)
        #btn_exit=Button(menu,text="Exit",font=("arial",15,),bg="#010c48",fg="white", anchor="c",cursor="hand2").place(x=0,y=340,width=200, height = 40)
        
        #content
        self.lbl_emp=Button(self.root,text="Employees",command=self.employee,bg="white",fg="black",font=("arial",20))
        self.lbl_emp.place(x=300,y=120,height=150,width=300)
        
        self.lbl_sup=Button(self.root,text="Suppliers",command=self.supplier,bg="white",fg="black",font=("arial",20))
        self.lbl_sup.place(x=650,y=120,height=150,width=300)

        self.lbl_cat=Button(self.root,text="Categories",command=self.category,bg="white",fg="black",font=("arial",20))
        self.lbl_cat.place(x=1000,y=120,height=150,width=300)

        self.lbl_pro=Button(self.root,text="Products",command=self.product,bg="white",fg="black",font=("arial",20))
        self.lbl_pro.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Button(self.root,text="Sales",command=self.sales,bg="white",fg="black",font=("arial",20))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)


        #footer
        self.foot=Label(self.root,text="Inventory Management System | Developed by Vanishka Gupta", font=("arial",15),bg="#1e3d59",fg="white").pack(side="bottom",fill=X)

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=empclass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=suppclass(self.new_win)
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=catclass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=proclass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=saleclass(self.new_win)

    #def sale(self):
    #    self.new_win=Toplevel(self.root)
    #    self.new_obj=saleclass(self.new_win)

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
