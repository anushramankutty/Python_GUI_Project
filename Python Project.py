from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector

#Box
window=Tk()
window.geometry("1080x720")
window.title("IV FORM")
window.config(bg="Black")
window.iconbitmap("bus.ico")

#Bg Img
image=Image.open("mysore.JPG")
image=image.resize((1275,720))
photo=ImageTk.PhotoImage(image)


#Cse,Industrial visit name
lb2=Label(window,text="CSE",font=("FootLight MT Light",30,"bold"),bg="white",fg="black")
lb2.place(x=300,y=275)
lb3=Label(window,text="INDUSTRIAL VISIT",font=("FootLight MT Light",30),bg="white")
lb3.place(x=190,y=330)

#Reg frame
frame=Frame(window,bg="white")
frame.grid(row=0,column=0,ipadx=245,ipady=225,padx=650,pady=100)
lb4=Label(frame,text="PARTICULARS",font=("Dubai",30,"bold"),bg="white",fg="black")
lb4.place(x=120,y=5)


#Def submit,delete,view
def submit():
    data1 = en1.get()
    data2 = en2.get()
    data3 = en3.get()
    data4 = en4.get()
    data5 = en5.get()
    
    if data1 != '' and data2 != '' and data3 != '' and data4 != '':
        messagebox.showinfo("INFO", "SUBMITTED")
        en1.delete(0, END)
        en2.delete(0, END)
        en3.delete(0, END)
        en4.delete(0, END)
        en5.delete(0, END)
        en1.focus()
        
        mydb = mysql.connector.connect(host="localhost", user="root", password="Anush@1604", database="reglist")
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO cse_reg (REGISTER_NUMBER, STUDENT_NAME, DEPT_YEAR, AMOUNT, CURRENT_STATUS) VALUES (%s, %s, %s, %s, %s)",(int(data1), data2, int(data3), int(data4), data5))
        mydb.commit()
        mycursor.close()
        mydb.close()
    else:
        messagebox.showinfo("INFO","DATA MISSING")

def delete():
    data1 = en1.get()
    if data1 != '':
        mydb = mysql.connector.connect(host="localhost", user="root", password="Anush@1604", database="reglist")
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM cse_reg WHERE REGISTER_NUMBER = %s", (int(data1),))
        mydb.commit()
        mycursor.close()
        mydb.close()
        messagebox.showinfo("INFO", "RECORD DELETED")
        en1.delete(0, END)
        en2.delete(0, END)
        en3.delete(0, END)
        en4.delete(0, END)
        en5.delete(0, END)
        en1.focus()
    else:
        messagebox.showinfo("INFO", "REGISTER_NUMBER IS REQUIRED")

def view():
    data1=en1.get()
    mydb=mysql.connector.connect(host="localhost",user="root",password="Anush@1604",database="reglist")
    mycursor=mydb.cursor()
    mycursor.execute("select * from cse_reg where REGISTER_NUMBER='%d'"%(int(data1)))
    mydata=mycursor.fetchall()
    en2.insert("end",mydata[0][1])
    en3.insert("end",mydata[0][2])
    en4.insert("end",mydata[0][3])
    en5.insert("end",mydata[0][4]) 
    mydb.commit()
    mycursor.close()
    mydb.close()

#Details with entry box
lb5=Label(frame,text="REGISTER_NUMBER",font=("Dubai Medium",15),bg="white")
lb5.place(x=35,y=100)
en1=Entry(frame,font=("Courier New",14),width=14,border=3)
en1.place(x=255,y=100)

lb6=Label(frame,text="STUDENT_NAME",font=("Dubai Medium",15),bg="white")
lb6.place(x=35,y=150)
en2=Entry(frame,font=("Courier New",14),width=14,border=3)
en2.place(x=255,y=150)

lb7=Label(frame,text="DEPT_YEAR",font=("Dubai Medium",15),bg="white")
lb7.place(x=35,y=200)
en3=Entry(frame,font=("Courier New",14),width=14,border=3)
en3.place(x=255,y=200)

lb8=Label(frame,text="AMOUNT",font=("Dubai Medium",15),bg="white")
lb8.place(x=35,y=250)
en4=Entry(frame,font=("Courier New",14),width=14,border=3)
en4.place(x=255,y=250)

lb9=Label(frame,text="CURRENT_STATUS",font=("Dubai Medium",15),bg="white")
lb9.place(x=35,y=300)
en5=Entry(frame,font=("Courier New",14),width=14,border=3)
en5.place(x=255,y=300)

#Buttons for submit,delete,view
bt=Button(frame,text="SUBMIT",font=("verdana",10),bg="white",padx=5,pady=3,command=submit)
bt.place(x=255,y=350)

bt2=Button(frame,text="DELETE",font=("verdana",10),bg="white",padx=5,pady=3,command=delete)
bt2.place(x=345,y=350)

bt=Button(frame,text="VIEW",font=("verdana",10),bg="white",padx=5,pady=3,command=view)
bt.place(x=308,y=390)

