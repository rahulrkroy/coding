from tkinter import *;
root=Tk()

# mylabel1=Label(root,text="hello").pack()
# mylabel2=Label(root,text="kill bill").grid(row=1,column=2)

def demofunc():
    print("Button is clicked")
    val=float(e1.get())
    t1.insert(END,val*1.6)


b1=Button(root,text="Convert to km",command=demofunc)
b1.grid(row=0,column=0)


e1=Entry(root)
e1.grid(row=0,column=1)

t1=Text(root,height=1,width=20)
t1.grid(row=0,column=2)

root.mainloop()

