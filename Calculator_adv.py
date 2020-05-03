from tkinter import *
root=Tk()
root.title("new calculator")
root.configure(bg='black')
Text=Entry(root,text='txt',font=("Arial Bold",16),borderwidth=5)
Text.grid(column=0,row=0,columnspan=6,padx=10,pady=10)
'''------------------- BUTTONS --------------------------'''
def value(number):
    cur=str(Text.get())
    Text.delete(0,END)
    Text.insert(0, cur + str(number))
def clear():
    Text.delete(0, END)
btn1=Button(root,text="7",command=lambda: value(7),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn1.grid(row=1,column=1)
btn2=Button(root,text="8",command=lambda: value(8),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn2.grid(row=1,column=2)
btn3=Button(root,text="9",command=lambda: value(9),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn3.grid(row=1,column=3)

btn4=Button(root,text="4",command=lambda: value(4),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn4.grid(row=2,column=1)
btn5=Button(root,text="5",command=lambda: value(5),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn5.grid(row=2,column=2)
btn6=Button(root,text="6",command=lambda: value(6),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn6.grid(row=2,column=3)

btn7=Button(root,text="1",command=lambda: value(1),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn7.grid(row=3,column=1)
btn8=Button(root,text="2",command=lambda: value(2),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn8.grid(row=3,column=2)
btn9=Button(root,text="3",command=lambda: value(3),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn9.grid(row=3,column=3)

btn0=Button(root,text="0",command=lambda: value(0),font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
btn0.grid(row=4,column=2)
'''------------------------- operand buttons -------------'''
def clicked1():
    global num
    num=float(Text.get())
    global operand
    operand= '+'
    Text.delete(0,END)


def clicked2():
    global num
    num=float(Text.get())
    global operand
    operand= '-'
    Text.delete(0,END)


def clicked3():
    global num
    num=float(Text.get())
    global operand
    operand= '*'
    Text.delete(0,END)


def clicked4():
    global num
    num=float(Text.get())
    global operand
    operand= '/'
    Text.delete(0,END)


def calculate():
    n2=float(Text.get())
    if operand =='+':
        ans=num + n2
    if operand =='-':
        ans=num - n2
    if operand =='/':
        ans=num / n2
    if operand =='*':
        ans=num * n2
    Text.delete(0,END)
    Text.insert(0,ans)
Obtn1=Button(root,text="+",command=clicked1,font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
Obtn1.grid(row=1,column=4)
Obtn2=Button(root,text="-",command=clicked2,font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
Obtn2.grid(row=2,column=4)
Obtn3=Button(root,text="*",command=clicked3,font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
Obtn3.grid(row=3,column=4)
Obtn4=Button(root,text="/",command=clicked4,font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
Obtn4.grid(row=4,column=4)
Fbtn=Button(root,text="=",command=calculate,font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
Fbtn.grid(row=4,column=3)
Cbtn=Button(root,text="C",command=clear,font=("Arial Bold",16),padx=20,pady=20,fg='#ffffff',bg="#000000")
Cbtn.grid(row=4,column=1)
root.mainloop()

'''
problems i faced:-
global variables need to be initalized inside the functions so that can come into existence
always make sure if loops are working
'''