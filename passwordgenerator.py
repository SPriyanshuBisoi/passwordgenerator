from tkinter import *
import random

window=Tk()
window.title('Password Generator')
window.geometry('500x300')
window.configure(bg="#3c345c") 


label1 = Label(window,text='Password Generator',width=25,height=2,font='Ivy 22 bold',bg="#3c345c",fg="#FF9B9B")
label1.place(x=40,y=2)

label2 = Label(window, text='Enter user name:',width=20,height=1,font='Ivy 10 bold',bg="#3c345c",fg="#FF9B9B")
label2.place(x=15,y=80)

label3 = Label(window, text='Enter password length:',width=20,height=1,font='Ivy 10 bold',bg="#3c345c",fg="#FF9B9B")
label3.place(x=15, y=140)

label4 = Label(window, text='Generated password:',width=20,height=1,font='Ivy 10 bold',bg="#3c345c",fg="#FF9B9B")
label4.place(x=15, y=200)

entry1 = Entry(window, width=30, font='Ivy 12')
entry1.place(x=200, y=80)

entry2 = Entry(window, width=20, font='Ivy 12')
entry2.place(x=200, y=140)

entry3 = Entry(window, width=30, font='Ivy 12')
entry3.place(x=200, y=200)

def generate():

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbol = "@#$^&*_"
    num = "0123456789"

    all = lower + upper + symbol + num

    n = int(entry2.get())

    password = "".join(random.sample(all, n))

    entry3.delete(0, END)
    entry3.insert(0, password)

icon=PhotoImage(file="gene.png")
Button(window,image=icon,bd=0,command=generate,bg="#3c345c").pack(side=RIGHT,pady=13)

window.mainloop()