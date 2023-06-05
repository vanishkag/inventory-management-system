import mysql.connector
def create_db():
    con=mysql.connector.connect(host='localhost',username='root',password='123456',database='ims')
    cur=con.cursor()
    cur.execute("create table if not exists employee(Empid integer(10) primary key auto_increment, Name varchar(10), Email varchar(10), Gender text, Contact integer(10), DOB date, DOJ date, Password varchar(8), Utype text, Address text, Salary text)")
    cur.execute("create table if not exists supplier(Invoice integer(10) primary key auto_increment, Name text, Contact integer(10), Description text)")
    cur.execute("create table if not exists category(CId integer(10) primary key auto_increment, Name text);")
    cur.execute("create table if not exists product(PId integer(10) primary key auto_increment, Category text, Supplier text, Name text, Price text, Qty text, Status text )")

    con.commit()

create_db()

