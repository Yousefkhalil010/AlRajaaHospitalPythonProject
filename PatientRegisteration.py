import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector


def Show_inlabels(event):
   
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    print(select)
    if 'PatientName' in select:
        e1.insert(0, select['PatientName'])
    if 'Age' in select:
        e2.insert(0, select['Age'])
    if 'Gender' in select:
        e3.insert(0, select['Gender'])
    if 'Address' in select:
        e4.insert(0, select['Address'])
    if 'Mobile' in select:
        e5.insert(0, select['Mobile'])
    if 'HireDate' in select:
        e6.insert(0, select['HireDate'])
    
def update():
    PatientName = e1.get()
    Age = e2.get()
    Gender = e3.get()
    Address = e4.get()
    Mobile = e5.get()
    HireDate= e6.get()
    mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="14678Naseem",
        database="hospital"
        )
    mycursor = mysqldb.cursor()
    try:
        sql="UPDATE Patient set Age =%s, Gender=%s, Address= %s, Mobile= %s, HireDate = %s where PatientName = %s "
        val = (Age, Gender, Address, Mobile, HireDate,PatientName)
        mycursor.execute(sql,val)
        mysqldb.commit()
        messagebox.showinfo("GoodJob","Information Updated Successfully...")
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
        
 
def clear_fields():
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)
    e6.delete(0, tk.END)

def delete():
    pname=e1.get()
    mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="14678Naseem",
        database="hospital"
        )
    mycursor = mysqldb.cursor()
    try:
        sql="DELETE from patient WHERE PatientName=%s"
        val = (pname,)
        mycursor.execute(sql,val)
        mysqldb.commit()
        messagebox.showinfo("GoodJob","Record Deleted Successfully...")
        
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysql.close()
    
def register_patient():
    PatientName = e1.get()
    Age = e2.get()
    Gender = e3.get()
    Address = e4.get()
    Mobile = e5.get()
    HireDate= e6.get()
  
    if not (PatientName and Age and Gender and Address and Mobile and HireDate):
        messagebox.showerror("Error", "Please fill in all fields")
        return

    try:
        Age = int(Age)
    except ValueError:
        messagebox.showerror("Error", "Age must be a number")
        return
    try:
        Mobile = int(Mobile)
    except ValueError:
        messagebox.showerror("Error", "Mobile must be a number")
        return

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="14678Naseem",
        database="hospital"
    )

    mycursor = db.cursor()

    sql = "INSERT INTO patient (PatientName, Age, Gender, Address, Mobile, HireDate) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (PatientName, Age, Gender, Address, Mobile, HireDate)

    mycursor.execute(sql, val)

    db.commit()
    db.close()

    messagebox.showinfo("Success", "Patient registered successfully")

def show():
    mysqldb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="14678Naseem",
        database="hospital"
        )
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT PatientName, Age, Gender, Address, Mobile, HireDate FROM patient")
    records = mycursor.fetchall()
    print(records)
    for i, (PatientName, Age, Gender, Address, Mobile, HireDate) in enumerate(records, start=1):
        listBox.insert("", "end", values=(PatientName, Age, Gender, Address, Mobile, HireDate))
        mysqldb.close()
    
root = tk.Tk()
root.geometry("1200x500")
root.title("AlRajaa Hospital Patients Archive")
global e1
global e2
global e3
global e4
global e5
global e6

tk.Label(root, text="Patient Registeration",fg="black",font=(None, 30)).place(x=400,y=5)
tk.Label(root, text="Patient Name:").place(x=10,y=10)
tk.Label(root, text="Age:").place(x=10,y=30)
tk.Label(root, text="Gender:").place(x=10,y=50)
tk.Label(root, text="Address:").place(x=10,y=70)
tk.Label(root, text="Mobile:").place(x=10,y=90)
tk.Label(root, text="HireDate:").place(x=10,y=110)
e1=tk.Entry(root)
e1.place(x=140, y=10)
e2=tk.Entry(root)
e2.place(x=140, y=30)
e3=tk.Entry(root)
e3.place(x=140, y=50)
e4=tk.Entry(root)
e4.place(x=140, y=70)
e5=tk.Entry(root)
e5.place(x=140, y=90)
e6=tk.Entry(root)
e6.place(x=140, y=110)
register_button = tk.Button(root,text="Register",command=register_patient,height=3,width=13).place(x=30, y=130)
update_button = tk.Button(root,text="Update",command=update,height=3,width=13).place(x=140, y=130)
delete_button = tk.Button(root,text="Delete",command=delete,height=3,width=13).place(x=250, y=130)
erase_button = tk.Button(root,text="Erase",command=clear_fields,height=3,width=13).place(x=370, y=130)

cols=("PatientName","Age","Gender","Address","Mobile","HireDate")
listBox = ttk.Treeview(root, columns=cols,show="headings")
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=1)
    listBox.place(x=0,y=200)
show()
listBox.bind('<Double-Button-1>',Show_inlabels)
root.mainloop()
