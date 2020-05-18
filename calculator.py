from tkinter import *
import parser
import math
root=Tk()
root.title("Calculator")
i=0
def get_var(num):
    global i
    display.insert(i,num)
    i+=1
def clear_all():
    display.delete(0,END)

def get_operation(operator):
    global i
    lenght=len(operator)
    display.insert(i,operator)
    i+=lenght

def calculate():
    entire_str=display.get()
    try:
        a=parser.expr(entire_str).compile()
        global result
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
def undo():
    entire_str=display.get()
    if len(entire_str)>0:
        new_str=entire_str[:-1]
        clear_all()
        display.insert(0,new_str)
    else:
        clear_all()
        display.insert(0,"Error")


def factorial():
    whole_string = display.get()
    number = int(whole_string)
    fact = 1
    counter = number
    while counter > 0:
        fact = fact*counter
        counter -= 1
    clear_all()
    display.insert(0, fact)
#Adding input field
display=Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)

#Adding buttons to calculator
Button(root,text="1",command=lambda :get_var(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda :get_var(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda :get_var(3)).grid(row=2,column=2)

Button(root,text="4",command=lambda :get_var(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda :get_var(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda :get_var(6)).grid(row=3,column=2)

Button(root,text="7",command=lambda :get_var(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda :get_var(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda :get_var(9)).grid(row=4,column=2)

#Adding other buttons to calculator
Button(root,text="AC",command=lambda :clear_all()).grid(row=5,column=0)
Button(root,text="0",command=lambda :get_var(0)).grid(row=5,column=1)
Button(root,text="=",command=lambda :calculate()).grid(row=5,column=2)

Button(root,text="+",command=lambda :get_operation("+")).grid(row=2,column=3)
Button(root,text="-",command=lambda :get_operation("-")).grid(row=3,column=3)
Button(root,text="*",command=lambda :get_operation("*")).grid(row=4,column=3)
Button(root,text="/",command=lambda :get_operation("/")).grid(row=5,column=3)

#Adding new operations
Button(root,text="pi",command=lambda :get_operation("3.14")).grid(row=2,column=4)
Button(root,text="%",command=lambda :get_operation("%")).grid(row=3,column=4)
Button(root,text="(",command=lambda :get_operation("(")).grid(row=4,column=4)
Button(root,text="exp",command=lambda :get_operation("**")).grid(row=5,column=4)

Button(root,text="<-",command=lambda :undo()).grid(row=2,column=5)
fact = Button(root, text = "x!", command = factorial, font=("Calibri", 12)).grid(row = 3, column = 5)
Button(root,text=")",command=lambda :get_operation(")")).grid(row=4,column=5)
Button(root,text="^2",command=lambda :get_operation("**2")).grid(row=5,column=5)

root.mainloop()

