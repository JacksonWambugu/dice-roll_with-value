import random 
from tkinter import *
root = Tk()
root.geometry("700x400")

def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    num1=random.choice(number)
    num2=random.choice(number)
    l1.config(text=f'{num1}{num2}')    
    l1.pack()
    val1=ord(num1)-9855
    val2=ord(num2)-9855
    sum= str(val1+val2)
    
    l2.config(text="you Rolled  :: " +sum)
    l2.pack()

l1=Label(root,font=("times",200))
l2=Label(root,font=("times",34))
b1=Button(root,text="Roll dice .. ",command=roll)
b1.place(x=330,y=0)


root.mainloop()