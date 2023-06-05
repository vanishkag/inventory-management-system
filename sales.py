from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import os

class saleclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Vanishka")
        self.root.config(bg="#f5f0e1")
        self.root.focus_force()
        self.bl = []
        self.var_invoice=StringVar()
        #title
        lbl_title=Label(self.root,text="View Customer Bill", font=("arial",30),bg="white",fg="black").pack(side=TOP,fill=X)
        lbl_invoice=Label(self.root,text="Invoice No.",font=('arial',15),bg="white",fg="black").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=('arial',15),bg="white",fg="black").place(x=160,y=100,width=180,height=28)
   
        btn_search=Button(self.root,text="Search",command=self.search,font=("arial",15),bg="white",fg="black",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Clear",font=("arial",15),bg="white",fg="black",cursor="hand2").place(x=490,y=100,width=120,height=28)
        
#bill list
        sFrame=Frame(self.root,bg="white")
        sFrame.place(x=50,y=140,width=200,height=330)

        scrolly=Scrollbar(sFrame,orient=VERTICAL)
        self.sal=Listbox(sFrame,font=("arial",15),bg="white",yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.sal.yview)
        self.sal.pack(fill=BOTH,expand=1)
        #self.sal.bind("<ButtonRelease-1>",self.get_data)
        
#bill area
        bFrame=Frame(self.root,bg="white")
        bFrame.place(x=280,y=140,width=410,height=330)

        lbl_btitle=Label(bFrame,text="Customer Bill", font=("arial",20),bg="white",fg="black").pack(side=TOP,fill=X)

        scrollb=Scrollbar(bFrame,orient=VERTICAL)
        self.ba=Text(sFrame,font=("arial",15),bg="white",yscrollcommand=scrollb.set)
        scrollb.pack(side=RIGHT,fill=Y)
        scrollb.config(command=self.sal.yview)
        self.sal.pack(fill=BOTH,expand=1)

        self.show()

    """def search():
        con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
        cur=con.cursor()
        try:
            if self.var_invoice.get()=="":
                messagebox.showerror("Error","Invoice No is required",parent=self.root)
            
            else:
                cur.execute("select ")

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)"""
    
    def show(self):
        del self.bl[:]
        self.sal.delete(0,END)
        for i in os.listdir('C:\Personal\Minty\inventory management system'):
            if i.split('.')[-1]=='txt':
                self.sal.insert(END,i)
                self.bl.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.sal.curselection()
        fi=self.sal.get(index_)
        self.ba.delete('1.0',END)
        fp=open(f'{fi}','r')
        for i in fp:
            self.ba.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No is required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bl:
                fp=open(f'{self.var_invoice.get()}.txt','r')
                self.ba.delete('1.0',END)
                for i in fp:
                    self.ba.insert(END,i)
                fp.close()


if __name__=="__main__":
    root = Tk()
    obj = saleclass(root)
    root.mainloop()