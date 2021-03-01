from tkinter import *
from tkinter import ttk

import Eight_queens

def myfunction():
    global cnt,a,l,queen
    
    for i in range(8):
        for j in range(8):
            l[i][j]['bg']="brown"

    n = len(a)
    s = a[cnt%n]
    for i in range(len(s)):
        l[i][int(s[i])]['bg'] = "darkgreen"
        cnt+=1


root = Tk()
root.title("8queens Visualisation")
root.geometry("480x650") #480,650
root.resizable(0,0)


b = Button(root,width = 25,height= 2,text="Visualize",font=('areial',23,'bold'),command=myfunction)
b.place(x=0,y=0)


l= []
x_co,y_co = 0,100
for i in range(8):
    r=[]
    x_co = 0
    for j in range(8):
        r.append(Label(root,width=5,height=3,padx=10,pady=10,bg="brown"))
        r[j].place(x=x_co,y=y_co)
        x_co += 60
    y_co += 70
    l.append(r)




cnt = 0     
f = open("solution.txt","r")
a = f.readlines()
for i in range(len(a)):
    a[i] = a[i][:-1]
f.close()


root = mainloop()