from tkinter import *
import random

#******************************************************************************    
count=0
def quiz1():
    def add():
        global count
        count+=1
        l1.config(text=count)

    def su():
        global count
        count-=1
        l1.config(text=count)
        if count == 0:
            l1.config(text="0")

    def sub():
        if count == 25:
            l2.config(text="Right")
        else:
            l2.config(text="Wrong")
            
    global b    
    b=Tk()
    a.destroy()
    
    

    photo1 = PhotoImage(master=b, file='quiz1.png')
    img_label = Label(b, image=photo1)
    img_label.image = photo1
    img_label.grid(row=0, column=0, columnspan=5)
    
    Button(b,text="+",font=("normal",50),height=1,width=1,command=add).grid(row=2,column=4)
    Button(b,text="-",font=("normal",50),height=1,width=1,command=su).grid(row=2,column=0)
    
    l1=Label(b,text="0",font=("normal",50))
    l1.grid(row=2,column=1,columnspan=2)
    
    Button(b,text="Sub",font=("normal",50),command=sub).grid(row=3,column=2)

    l2=Label(b,text="",font=("normal",50))
    l2.grid(row=4,column=0,columnspan=3)

    Button(b,text=">>>",command=quiz2).grid(row=4,column=4)
##    Button(b,text="Retry",command=quiz1).grid(row=4,column=3)

#****************************************************************************

def quiz2():
    def d(event):
        widget = event.widget
        widget.startx = event.x
        widget.starty = event.y
    def da(event):
        widget = event.widget
        x = widget.winfo_x() - widget.startx + event.x
        y = widget.winfo_y() - widget.starty + event.y
        widget.place(x=x,y=y)

    global c   
    c=Tk()
    b.destroy()
    c.geometry("600x600")

    
    rand=random.randint(0,8)
    

    pos=[[0,0],[174,0],[348,0],[0,164],[174,164],[348,164],[0,328],[174,328],[348,328]]
    x_cood=pos[rand][0]
    y_cood=pos[rand][1]
    
    
    

    
    Label(c,text="Find The Different One")

    Button(c,text=">>>",command=quiz3).place(x=500,y=500)
    
    notmo= Button(c,text="",bg="black",activeforeground="white",activebackground="black",width=5,height=3,relief=FLAT,command=quiz3)
    notmo.place(x=x_cood,y=y_cood)  
    

    l11 = Label(c,text="",bg="red",width=10,height=5)
    l11.place(x=0,y=0)

    l22 = Label(c,text="",bg="red",width=10,height=5)
    l22.place(x=174,y=0)

    l3 = Label(c,text="",bg="red",width=10,height=5)
    l3.place(x=348,y=0)

    l4 = Label(c,text="",bg="red",width=10,height=5)
    l4.place(x=0,y=164)

    l5 = Label(c,text="",bg="red",width=10,height=5)
    l5.place(x=174,y=164)

    l6 = Label(c,text="",bg="red",width=10,height=5)
    l6.place(x=348,y=164)

    l7 = Label(c,text="",bg="red",width=10,height=5)
    l7.place(x=0,y=328)

    l8 = Label(c,text="",bg="red",width=10,height=5)
    l8.place(x=174,y=328)

    l9 = Label(c,text="",bg="red",width=10,height=5)
    l9.place(x=348,y=328)


    






    l11.bind("<Button-1>",d)
    l11.bind("<B1-Motion>",da)

    l22.bind("<Button-1>",d)
    l22.bind("<B1-Motion>",da)

    l3.bind("<Button-1>",d)
    l3.bind("<B1-Motion>",da)

    l4.bind("<Button-1>",d)
    l4.bind("<B1-Motion>",da)

    l5.bind("<Button-1>",d)
    l5.bind("<B1-Motion>",da)

    l6.bind("<Button-1>",d)
    l6.bind("<B1-Motion>",da)

    l7.bind("<Button-1>",d)
    l7.bind("<B1-Motion>",da)

    l8.bind("<Button-1>",d)
    l8.bind("<B1-Motion>",da)
    
    l9.bind("<Button-1>",d)
    l9.bind("<B1-Motion>",da)
#******************************************************************************



def quiz3():


    def sub1():
        if cou.get() == 56:
            ch.config(text="Right")
        else:
            ch.config(text="Wrong")

    global d
    d=Tk()
    c.destroy()

    Label(d,text="Solve",font=("NORMAL",30)).pack()
    

    Label(d,text="1+2+3+1\n4+8+4+1\n1+2+4+7",font=("NORMAL",30)).pack()
    

    cou=Scale(d,
             from_=0,
             to=100,
             length=200,
             orient=HORIZONTAL)
    cou.pack()

        
    Button(d,text="Sub",font=("normal",30),command=sub1).pack()

    ch=Label(d,text="",font=("normal",50))
    ch.pack()

    Button(d,text=">>>",command=quiz4).pack()



#****************************************************************************

def quiz4():

    def sub2():
        if ent.get() == "1":
            ch1.config(text="Right")
        else:
            ch1.config(text="Wrong")

    global e
    e=Tk()
    d.destroy()

    Label(e,text="Solve",font=("NORMAL",30)).pack()
    

    Label(e,text="if\n 1=5   2=15   3=215   4=3215\nThen 5=?",font=("NORMAL",30)).pack()

    ent=Entry(e)
    ent.pack()


    Button(e,text="Sub",font=("normal",30),command=sub2).pack()

    ch1=Label(e,text="",font=("normal",50))
    ch1.pack()

    Button(e,text=">>>",command=quiz5).pack()




#*******************************************************************************
def quiz5():

    global g
    g=Tk()
    e.destroy()

    def w():
        che2.config(text="Wrong")

    def r():
        che2.config(text="Right")
    Button(g,text="Find The Darkest Color On The Screen",relief=FLAT,activebackground="#D3D3D3",bg="#D3D3D3",command=r).grid(row=0,column=0)

    che2=Label(g,text="",fg="red")
    che2.grid(row=2,column=0)

    Button(g,bg="#632ADD",activebackground="#632ADD",width=3,height=2,relief=FLAT,command=w).grid(row=0,column=1)
    Button(g,bg="#8b15c6",activebackground="#8b15c6",width=3,height=2,relief=FLAT,command=w).grid(row=0,column=2)
    Button(g,bg="#570182",activebackground="#570182",width=3,height=2,relief=FLAT,command=w).grid(row=0,column=3)
    Button(g,bg="#8161C7",activebackground="#8161C7",width=3,height=2,relief=FLAT,command=w).grid(row=0,column=4)

    Button(g,bg="#5826A4",activebackground="#5826A4",width=3,height=2,relief=FLAT,command=w).grid(row=1,column=1)
    Button(g,bg="#C19ADF",activebackground="#C19ADF",width=3,height=2,relief=FLAT,command=w).grid(row=1,column=2)
    Button(g,bg="#460875",activebackground="#460875",width=3,height=2,relief=FLAT,command=w).grid(row=1,column=3)
    Button(g,bg="#9203FF",activebackground="#9203FF",width=3,height=2,relief=FLAT,command=w).grid(row=1,column=4)

    Button(g,bg="#7234A0",activebackground="#7234A0",width=3,height=2,relief=FLAT,command=w).grid(row=2,column=1)
    Button(g,bg="#73226B",activebackground="#73226B",width=3,height=2,relief=FLAT,command=w).grid(row=2,column=2)
    Button(g,bg="#C243B6",activebackground="#C243B6",width=3,height=2,relief=FLAT,command=w).grid(row=2,column=3)
    Button(g,bg="#B100A0",activebackground="#B100A0",width=3,height=2,relief=FLAT,command=w).grid(row=2,column=4)

    Button(g,bg="#730D42",activebackground="#730D42",width=3,height=2,relief=FLAT,command=w).grid(row=3,column=1)
    Button(g,bg="#FF0084",activebackground="#FF0084",width=3,height=2,relief=FLAT,command=w).grid(row=3,column=2)
    Button(g,bg="#FFCCE7",activebackground="#FFCCE7",width=3,height=2,relief=FLAT,command=w).grid(row=3,column=3)
    Button(g,bg="#782E55",activebackground="#782E55",width=3,height=2,relief=FLAT,command=w).grid(row=3,column=4)

    Button(g,text=">>>",command=quiz6).grid(row=5,column=4)


#********************************************************************************

def quiz6():
    def sub3():
        if ent.get()=="6":
            che.config(text="Right")
        else:
            che.config(text="wrong")
            

    global h
    h=Tk()
    g.destroy()

    Label(h,text="One candle is 50cm high and can\nburn for 3 hours.another one\nis 70cm high and can burn\nfor 6 hours.\nHow long does it takes for this\n two candle to reach the same height ",font=("NORMAL",20)).pack()

    ent=Entry(h)
    ent.pack()
    Button(h,text="Sub",font=("normal",30),command=sub3).pack()
    che=Label(h,text="",font=("normal",30))
    che.pack()
    Button(h,text=">>>",command=quiz7).pack()


#*******************************************************************************

def quiz7():
    global f
    f=Tk()
    h.destroy()

    def sub3():
        text1=ent.get()
        if ent.get()=="-100":
            che.config(text="Right")            
        elif text1.isalpha() == True:
            che.config(text="Number Only")
        elif len(ent.get()) > 3:
            che.config(text="3 Digit number stupid")
        else:
            che.config(text="wrong")
        

    def de():
        ent.delete(0,END)
            

    Label(f,text="Type The Smallest Possible Number\n  Three Digit Number",font=("normal",20)).pack()

    ent=Entry(f)
    ent.pack()
    Button(f,text="Sub",font=("normal",15),command=sub3).pack()
    Button(f,text="Delete",font=("normal",15),command=de).pack()
    che=Label(f,text="",font=("normal",30))
    che.pack()
    Button(f,text=">>>",command=quiz8).pack()
    

#*******************************************************************************
coo=0
def quiz8():
    global i
    i=Tk()
    f.destroy()
    i.configure(bg="White")

    
    def w():
        global coo
        coo+=1
        if coo == 2:
            che2.config(text="Game Over\nYou have used your chances")
            right.after(2000,quiz9)
        else:
            che2.config(text="Wrong")

    def r():
        global coo
        coo+=1
        if coo == 2:
            che2.config(text="Game Over\nYou have used your chances")
            right.after(2000,quiz9)
        else:
            che2.config(text="Right")
    

    Label(i,text="Which Color Is The Most\nYou have only one chance",font=("normal",10),bg="white").grid(row=0,column=0,columnspan=2)
    
    Label(i,bg="red",activebackground="red",width=5,height=3).grid(row=0,column=2)
    Label(i,bg="#5c49eb",activebackground="#5c49eb",width=5,height=3).grid(row=0,column=3)
    Label(i,bg="red",activebackground="red",width=5,height=3).grid(row=0,column=4)

    Label(i,bg="orange",activebackground="orange",width=5,height=3).grid(row=1,column=2)
    Label(i,bg="red",activebackground="red",width=5,height=3).grid(row=1,column=3)
    Label(i,bg="yellow",activebackground="yellow",width=5,height=3).grid(row=1,column=4)

    Label(i,bg="green",activebackground="green",width=5,height=3).grid(row=2,column=2)
    Label(i,bg="yellow",activebackground="yellow",width=5,height=3).grid(row=2,column=3)
    Label(i,bg="green",activebackground="green",width=5,height=3).grid(row=2,column=4)

    Button(i,text="Red",bg="#5c49eb",activebackground="#5c49eb",relief=FLAT,command=w).grid(row=1,column=0)
    Button(i,text="Yellow",bg="#5c49eb",activebackground="#5c49eb",relief=FLAT,command=w).grid(row=1,column=1)
    Button(i,text="Blue",bg="#5c49eb",activebackground="#5c49eb",relief=FLAT,command=w).grid(row=2,column=0)
    right=Button(i,text="White",bg="#5c49eb",activebackground="#5c49eb",relief=FLAT,command=r)
    right.grid(row=2,column=1)

    che2=Label(i,text="",bg="white")
    che2.grid(row=3,column=0,columnspan=2)

    Button(i,text=">>>",bg="white",activebackground="white",command=quiz9).grid(row=3,column=2,columnspan=3)

    
#*******************************************************************************
    
def quiz9():
    global j
    j=Tk()
    i.destroy()
#*******************************************************************************



    
#*******************************************************************************
#*******************************************************************************


a=Tk()


Button(a,text="Quiz",font=("normal",50),relief=FLAT,command=quiz1).pack()

a.mainloop()










'''
#********************************************************************************
count1=0
count2=0
def quiz100():

    def col():
        bu.config(bg="orange",activebackground="orange")

    def color():
        global count1
        count1+=1
        print(count1)
        if count1 == 4:
            count1-=count1
            che.config(text="wrong")

    def color2():
        global count2
        count2+=1
        print(count2)
        if count2 == 3:
            bu.after(4000,col)
            if count2 == 4:
                che.config(text="wrong")
                count2-=count2
                
    global i
    i=Tk()
    h.destroy()

    che=Label(i,text="",font=("normal",30))
    che.pack()
    Button(i,width=50,height=5,relief=FLAT,bg="orange",activebackground="orange",command=color).pack()
    bu=Button(i,width=50,height=5,relief=FLAT,bg="green",activebackground="green",command=color2)
    bu.pack()

    

#********************************************************************************

def quiz101():

    def up(event):
        obj.place(x=obj.winfo_x(),y=obj.winfo_y()-10)
    def down(event):
        obj.place(x=obj.winfo_x(),y=obj.winfo_y()+10)
    def left(event):
        obj.place(x=obj.winfo_x()-10,y=obj.winfo_y())
    def right(event):
        obj.place(x=obj.winfo_x()+10,y=obj.winfo_y())
    global f
    f=Tk()
    e.destroy()

    f.bind("<w>",up)
    f.bind("<s>",down)
    f.bind("<a>",left)
    f.bind("<d>",right)

    obj=Label(f,text="*")
    obj.place(x=0,y=0)'''
