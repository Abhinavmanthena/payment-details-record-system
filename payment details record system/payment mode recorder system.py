from tkinter import *
win=Tk()
def getvalues():
    print( f"{namevalue.get(),phonevalue.get(),gendervalue.get(),paymentidvalue.get(),paymenttype.get(),foodservice.get()}")
    with open("records.txt","a") as f:
        f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),paymentidvalue.get(),paymenttype.get(),foodservice.get()}\n")


win.geometry("300x300")
Label(win,text="Welcome to the store",font="Comicsansms 13 bold",pady=15).grid(row=0,column=3)
name=Label(win,text="Name")
phone=Label(win,text="Phone")
gender=Label(win,text="Gender")
paymentid=Label(win,text="PaymentID")
paymenttype=Label(win,text="Payment Mode")


name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
paymentid.grid(row=4,column=2)
paymenttype.grid(row=5,column=2)


namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
paymentidvalue=StringVar()
paymenttype=StringVar()
foodservice=IntVar()



nameentry=Entry(win,textvariable=namevalue)
phoneentry=Entry(win,textvariable=phonevalue)
genderentry=Entry(win,textvariable=gendervalue)
paymentidentry=Entry(win,textvariable=paymentidvalue)
paymenttypeentry=Entry(win,textvariable=paymenttype)



nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
paymentidentry.grid(row=4,column=3)
paymenttypeentry.grid(row=5,column=3)

foodservicee=Checkbutton(win,text="want to book pre meals",variable=foodservice)
foodservicee.grid(row=6,column=3)

Button(win,text="submit to the Store",command=getvalues).grid(row=7,column=3)

win.mainloop()




