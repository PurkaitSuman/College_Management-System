from tkinter import *
from tkinter import ttk
from tkinter import ttk, messagebox
from PIL import ImageTk
def addstudent():
	rt.destroy()
	import addstudent
def login():
	rt.destroy()
	import login
def reg_win():
	rt.destroy()
	import register

rt=Tk()
rt.title("Home Page")
rt.geometry("1400x900+0+0")
bg=ImageTk.PhotoImage(file="pic.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
frame=Frame(rt,bg="white")
frame.place(x=520,y=100,width=800,height=630)
reg=Label(frame,text="Welcome To S D College",font=("constantia",30,"bold"),bg="black",fg="yellow")
reg.place(x=50,y=30,width=700)
#/b1=Button(frame,text="Add Student",command=addstudent,font=("times new roman",15,"bold"),bg="white")
#/b1.place(x=180,y=130)

b2=Button(frame,text="Login",command=login,font=("times new roman",15,"bold"),bg="white")
b2.place(x=270,y=130)
b3=Button(frame,text="Register",command=reg_win,font=("times new roman",15,"bold"),bg="white")
b3.place(x=400,y=130)
bg4=ImageTk.PhotoImage(file="pic2.jpg")
bglb2=Label(frame,image=bg4)
bglb2.place(x=192,y=210,width=350,height=350)
rt.mainloop() 