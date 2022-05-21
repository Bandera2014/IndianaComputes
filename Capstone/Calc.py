#as = alias
#import tkinter as tk
#* = wildcard or when you import, it is everything
from tkinter import *

groot=Tk()
groot.wm_geometry("312x324")
groot.title("Calculator")

inputText=StringVar()
expression=""

def btnClick(btnTXT):
    global expression
    expression = expression + str(btnTXT)
    inputText.set(expression)

def btnClear():
    global expression
    expression=""
    inputText.set("")    

def btnEqual():
    global expression
    result=str(eval(expression)) #eval function evaluates the string expression
    inputText.set(result)
    expression=""




inputFrame = Frame(groot,width=312,height=50)
inputFrame.pack(side=TOP)

inputField = Entry(inputFrame,font=('arial',18,'bold'),width=50,justify=RIGHT,textvariable=inputText)
inputField.grid(row=0,column=0)
inputField.pack()

btnFrame = Frame(groot, width=300, height=300)
btnFrame.pack()

clear=Button(btnFrame,width=30,height=3,text="C",command=btnClear).grid(row=0,column=0,columnspan=3, padx = 1, pady = 1)
divide=Button(btnFrame,width=10,height=3,text="/",command=lambda:btnClick("/")).grid(row=0,column=3, padx = 1, pady = 1)

#           (positional,keyword)
seven=Button(btnFrame,width=10,height=3,text="7",command=lambda:btnClick("7")).grid(row=1,column=0, padx = 1, pady = 1)
eight=Button(btnFrame,width=10,height=3,text="8",command=lambda:btnClick("8")).grid(row=1,column=1, padx = 1, pady = 1)
nine=Button(btnFrame,width=10,height=3,text="9",command=lambda:btnClick("9")).grid(row=1,column=2, padx = 1, pady = 1)
mult=Button(btnFrame,width=10,height=3,text="*",command=lambda:btnClick("*")).grid(row=1,column=3, padx = 1, pady = 1)

four=Button(btnFrame,width=10,height=3,text="4",command=lambda:btnClick("4")).grid(row=2,column=0, padx = 1, pady = 1)
five=Button(btnFrame,width=10,height=3,text="5",command=lambda:btnClick("5")).grid(row=2,column=1, padx = 1, pady = 1)
six=Button(btnFrame,width=10,height=3,text="6",command=lambda:btnClick("6")).grid(row=2,column=2, padx = 1, pady = 1)
minus=Button(btnFrame,width=10,height=3,text="-",command=lambda:btnClick("-"))
print(type(minus))
minus.grid(row=2,column=3, padx = 1, pady = 1)

one=Button(btnFrame,width=10,height=3,text="1",command=lambda:btnClick("1")).grid(row=3,column=0, padx = 1, pady = 1)
two=Button(btnFrame,width=10,height=3,text="2",command=lambda:btnClick("2")).grid(row=3,column=1, padx = 1, pady = 1)
three=Button(btnFrame,width=10,height=3,text="3",command=lambda:btnClick("3")).grid(row=3,column=2, padx = 1, pady = 1)
plus=Button(btnFrame,width=10,height=3,text="+",command=lambda:btnClick("+")).grid(row=3,column=3, padx = 1, pady = 1)

zero=Button(btnFrame,width=20,height=3,text="0",command=lambda:btnClick("0")).grid(row=4,column=0,columnspan=2, padx = 1, pady = 1)
deci=Button(btnFrame,width=10,height=3,text=".",command=lambda:btnClick(".")).grid(row=4,column=2, padx = 1, pady = 1)
equals=Button(btnFrame,width=10,height=3,text="=",command=btnEqual).grid(row=4,column=3, padx = 1, pady = 1)

groot.mainloop()