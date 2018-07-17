from tkinter import *
import random
import time
root=Tk()
root.title("Resturant Management")
root.geometry("1600x800+0+0")
root.configure(background="powder blue")
frame_1=Frame(root, bg='powder blue', width=1600,height=50)
frame_1.pack(side=TOP)
frame_2=Frame(root, bg='powder blue', width=600,height=100)
frame_2.pack(side=LEFT)
frame_3=Frame(root, bg='powder blue', width=1000,height=700)
frame_3.pack(side=RIGHT)
Fries=StringVar()
lunch=StringVar()
burger=StringVar()
pizza=StringVar()
cheese=StringVar()
drinks=StringVar()
service=StringVar()
cost=StringVar()
tax=StringVar()
subtotal=StringVar()
Total=StringVar()
order=StringVar()
#---------labels-----------------------------------------------------------------------------------------------------------
lab1L=Label(frame_1,text="Restaurant Management System",font=( 'aria' ,50, 'bold' ),bd=10,anchor="w",fg="steel blue")
lab1L.grid(row=0,column=0)
localtime=time.asctime(time.localtime(time.time()))
lab2L=Label(frame_1,text=localtime,font=( 'aria' ,20, 'bold' ))
lab2L.grid(row=1,column=0)
lab3L=Label(frame_1,text="Made By:- PRATTAY SANYAL",font=( 'aria' ,20, 'bold' ),fg="steel blue")
lab3L.grid(row=2,column=0)
                #---------------order--------------------------
orderL=Label(frame_2,text="order number",font=( 'aria' ,18, 'bold' ),fg="steel blue",bg="powder blue")
orderL.grid(row=0,column=0)
orderE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=order , bd=6,insertwidth=2,bg="white" ,justify='right')
orderE.grid(row=0,column=1)

                #------fries--------------------------------------------
friesL=Label(frame_2,text="fires meal",font=( 'aria' ,18, 'bold' ),anchor="w",fg="steel blue",bg="powder blue")
friesL.grid(row=1,column=0)
friesE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="white" ,justify='right')
friesE.grid(row=1,column=1)

                #---------lunch meal----------------------------
lunchL=Label(frame_2,text="lunch meal",font=( 'aria' ,18, 'bold' ),anchor="w",fg="steel blue",bg="powder blue")
lunchL.grid(row=2,column=0)
lunchE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=lunch , bd=6,insertwidth=4,bg="white" ,justify='right')
lunchE.grid(row=2,column=1)
                #---------burger------------------------------------------------
burgerL=Label(frame_2,text="burger meal",font=( 'aria' ,18, 'bold'),anchor="w",fg="steel blue",bg="powder blue")
burgerL.grid(row=3,column=0)
burgerE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=burger , bd=6,insertwidth=4,bg="white" ,justify='right')
burgerE.grid(row=3,column=1)
                #--------------pizza----------------------------------------------
pizzaL=Label(frame_2,text="pizza meal",font=( 'aria' ,18, 'bold'),anchor="w",fg="steel blue",bg="powder blue")
pizzaL.grid(row=4,column=0)
pizzaE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=pizza , bd=6,insertwidth=4,bg="white" ,justify='right')
pizzaE.grid(row=4,column=1)
                #------------------cheese----------------------------------------------
cheeseL=Label(frame_2,text="cheese meal",font=( 'aria' ,18, 'bold' ),anchor="w",fg="steel blue",bg="powder blue")
cheeseL.grid(row=5,column=0)
cheeseE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=cheese , bd=6,insertwidth=4,bg="white" ,justify='right')
cheeseE.grid(row=5,column=1)
                #------------------drinks-------------------------------
drinkL=Label(frame_2,text="drinks",font=( 'aria' ,18, 'bold' ),anchor="w",fg="steel blue",bg="powder blue")
drinkL.grid(row=0,column=2)
drinkE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=drinks , bd=6,insertwidth=4,bg="white" ,justify='right')
drinkE.grid(row=0,column=3)
                 #-------------------cost-------------------------------
costL=Label(frame_2,text="costs",font=( 'aria' ,18, 'bold' ),anchor="w",fg="steel blue",bg="powder blue")
costL.grid(row=1,column=2)
costE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
costE.grid(row=1,column=3)
                  #--------------------service--------------------------------
serviceL=Label(frame_2,text="service charge",font=( 'aria' ,18, 'bold' ),anchor="w",fg="steel blue",bg="powder blue")
serviceL.grid(row=2,column=2)
serviceE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=service, bd=6,insertwidth=4,bg="white" ,justify='right')
serviceE.grid(row=2,column=3)
                  #---------------------tax--------------------------------
taxL=Label(frame_2,text="tax",font=( 'aria' ,18, 'bold' ),anchor="w",fg="steel blue",bg="powder blue")
taxL.grid(row=3,column=2)
taxE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=tax , bd=6,insertwidth=4,bg="white" ,justify='right')
taxE.grid(row=3,column=3)
                   #----------------------------subtotal---------------------
subtotalL=Label(frame_2,text="subtotal",font=( 'aria' ,18, 'bold' ),fg="steel blue",bg="powder blue")
subtotalL.grid(row=4,column=2)
subtotalE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
subtotalE.grid(row=4,column=3)
                     #------------------------total---------------------------------
totalL=Label(frame_2,text="total",font=( 'aria' ,18, 'bold' ),anchor="w",fg="steel blue",bg="powder blue")
totalL.grid(row=5,column=2)
totalE=Entry(frame_2,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="white" ,justify='right')
totalE.grid(row=5,column=3)
#----------------------price function------------------------------------------------------------------------
def price():
    r=Tk()
    r.title("menu")
    r.geometry("400x240")
    r.configure(background="white")
    labF=Label(r,text="fries------------------------------Rs.30",bg="white",fg="black",anchor="w",font=( 'aria' ,16, 'bold' ))
    labF.grid(row=0,column=0)
    labL=Label(r,text="Lunch meal---------------------------Rs.80",bg="white",fg="black",anchor="w",font=( 'aria' ,16, 'bold' ))
    labL.grid(row=1,column=0)
    labBM=Label(r,text="burger meal-------------------------Rs.100",bg="white",fg="black",anchor="w",font=( 'aria' ,16, 'bold' ))
    labBM.grid(row=2,column=0)
    labP=Label(r,text="pizza--------------------------------Rs.175",bg="white",fg="black",anchor="w",font=( 'aria' ,16, 'bold' ))
    labP.grid(row=3,column=0)
    labC=Label(r,text="cheese meal-------------------------Rs.200",bg="white",fg="black",anchor="w",font=( 'aria' ,16, 'bold' ))
    labC.grid(row=4,column=0)
    labF=Label(r,text="drinks---------------------------Rs.20",bg="white",fg="black",anchor="w",font=( 'aria' ,16, 'bold' ))
    labF.grid(row=5,column=0)
    eB=Button(r,text="EXIT",command=r.destroy,font=( 'aria' ,16, 'bold' ),padx=10,pady=2,bd=10,bg="peach puff")
    eB.grid(row=6,column=0)
    r.mainloop()

#----------------------totalfunction-------------------------------------------------------------------------------
def total():
    x=random.randint(100,9999999)
    order.set(x)
    fp=float(friesE.get())
    lp=float(lunchE.get())
    bp=float(burgerE.get())
    pp=float(pizzaE.get())
    cp=float(cheeseE.get())
    dp=float(drinkE.get())
    try:
        if(type(friesE.get())==str):
           pass
    except Exception as e:
            Fries.set("enter a number")
    if(fp<0):
        fp=0
        Fries.set(0)
    else:
        pass
    if(lp<0 ):
        lp=0
        lunch.set(0)
    else:
        pass
    if(bp<0 ):
        bp=0
        burger.set(0)
    else:
        pass
    if(pp<0 ):
        pp=0
        pizza.set(0)
    else:
        pass
    if(cp<0 ):
        cp=0
        cheese.set(0)
    else:
        pass
    if(dp<0 ):
        dp=0
        drinks.set(0)
    else:
        pass    
    cof=fp*30
    cob=bp*100
    col=lp*80
    cop=cp*175
    coc=cp*200
    cod=dp*20
    co=(cof+cob+col+cop+coc+cod)
    cost.set("Rs."+str(co)) 
    tt=(co*0.05)
    tax.set("Rs."+str(tt))
    service.set("Rs.20.35")
    sb=(20.35+tt+co)
    subtotal.set("Rs."+str(sb))
    to=(sb+100.45)
    Total.set("Rs."+str(to))

#------------------------reset function---------------------------------------------------------
def reset():
    order.set("")
    Fries.set("")
    lunch.set("")
    burger.set("")
    pizza.set("")
    cheese.set("")
    drinks.set("")
    service.set("")
    cost.set("")
    tax.set("")
    subtotal.set("")
    Total.set("")

#-------------buttons---------------------------------------------------------------------------------
priceB=Button(frame_2,padx=14,pady=6,bd=14,text="PRICE",fg="black",width=7,bg="peach puff",font=( 'aria' ,14, 'bold' ),command=price)
priceB.grid(row=8,column=0)

totalB=Button(frame_2,padx=14,pady=6,bd=14,text="TOTAL",fg="black",bg="thistle1",font=( 'aria' ,14, 'bold' ),command=total)
totalB.grid(row=8,column=1)

resetB=Button(frame_2,padx=14,pady=6,bd=14,text="RESET",fg="black",bg="navajo white",font=( 'aria' ,14, 'bold' ),command=reset)
resetB.grid(row=8,column=2)

exitB=Button(frame_2,padx=14,pady=6,bd=14,text="EXIT",fg="black",font=( 'aria' ,14, 'bold' ),bg="misty rose",command=root.destroy)
exitB.grid(row=8,column=3)

root.mainloop()
