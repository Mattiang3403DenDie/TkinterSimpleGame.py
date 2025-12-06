'''Simple simulator game'''
#can bug easily at second better click,btw this is the first version
from tkinter import *

count=0
NyanCount=0
costFirst=50
costSecond=325
GoldCount=0

def click():
    global count
    count+=1
    label.config(text=count)

def better_click():
    global NyanCount
    NyanCount+=3
    label.config(text=NyanCount)
    btn.config(command=better_click)
    btn2.config(command=None)
    return count-costFirst

def InitializeSecond():
    if costFirst<count or costFirst==count:
        better_click()
    else:
        print("not enough clicks")

def SecondBetter():
    global GoldCount
    GoldCount+=7
    label.config(text=GoldCount)
    btn3.config(command=None)

def InitializeThird():
    if costSecond<NyanCount or costSecond<count or costSecond==NyanCount or costSecond==count:
        SecondBetter()
    else:
        print("not enough clicks")

wnd=Tk()
wnd.config(bg="cyan")
btn=Button(wnd,text="click me!",command=click)
label=Label(wnd,text=count,fg="black",bg="Blue")
label.config(font='Serif 20')
btn2=Button(wnd,text="Better click(50 clicks)",command=InitializeSecond)
btn3=Button(wnd,text="Better click(325 clicks)",command=InitializeThird)

btn3.pack()
btn2.pack()
btn.pack()
label.pack()
wnd.mainloop()
