from tkinter import *

class Frames(object):
    def __init__(self):
        self.nr = IntVar()
        self.n = StringVar()
        self.cn = StringVar()
        self.jt = StringVar()
        self.a = StringVar()
        self.a1 = StringVar()
        self.e1 = StringVar()
        self.w = StringVar()
        self.f = IntVar()

    def newframe(self):
        new = Toplevel(root)
        new.geometry("530x210")
        new.title("Visiting card")
        new.configure(bg="black")
        d1 = Label(new, text=self.cn.get(), font="cambria 17 italic bold",bg="black", fg="white",anchor="e",justify=CENTER).pack()
        d0 = Label(new, text="-------------------------------------------------------------------------------------------------------------",bg="black", fg="lightgreen").place(x=10,y=30)
        d2 = Label(new, text=self.n.get(), font="cambria 12 italic", bg="black", fg="lightblue").place(x=180,y=50)
        d3 = Label(new, text=self.jt.get(), font="cambria 12 italic", bg="black", fg="lightblue").place(x=180, y=75)
        d4 = Label(new, text=str(self.nr.get()), font="cambria 12 italic", bg="black", fg="lightblue").place(x=180, y=100)
        d5 = Label(new, text=self.a.get(), font="cambria 12 italic", bg="black", fg="lightblue").place(x=150, y=125)
        d9 = Label(new, text=self.a1.get(), font="cambria 12 italic", bg="black", fg="lightblue").place(x=150, y=150)
        d6 = Label(new, text=self.e1.get(), font="cambria 12 italic", bg="black", fg="lightblue").place(x=10, y=175)
        d7 = Label(new, text=self.w.get(), font="cambria 12 italic", bg="black", fg="lightblue").place(x=210, y=175)
        d8 = Label(new, text=str(self.f.get()), font="cambria 12 italic", bg="black", fg="lightblue").place(x=380, y=175)




    def mainframe(self, root):
        root.geometry("2000x2000")
        root.configure(bg="black")
        root.title("Visiting Card Maker")



        texts1 = Label(root, text="Enter the details in their respective boxes below.", font="cambria 18 italic bold", bg="black",fg="orange").place(x=45, y=195)
        texts2 = Label(root, text="Once done press the submit button to check out your new visiting card!!",font="cambria 18 italic bold", bg="black",fg="lightblue").place(x=570, y=195)
        compName = Label(root, text="Company Name(in caps)",font="cambria 16 italic", bg="black", fg="white").place(x=220, y=280)
        cname = Entry(root,textvariable=self.cn).place(x=450, y=280,width=200)
        Name = Label(root, text="Name",font="cambria 16 italic", bg="black", fg="white").place(x=720, y=280)
        nme = Entry(root,textvariable=self.n).place(x=920, y=280,width=200)
        jobttl = Label(root, text="Job title",font="cambria 16 italic", bg="black", fg="white").place(x=220, y=360)
        jbt = Entry(root,textvariable=self.jt).place(x=450, y=360,width=200)
        phonenum = Label(root, text="Phone number",font="cambria 16 italic", bg="black", fg="white").place(x=720, y=360)
        phn = Entry(root,textvariable=self.nr).place(x=920, y=360,width=200)
        address = Label(root, text="Address line 1",font="cambria 16 italic", bg="black", fg="white").place(x=220, y=440)
        adr = Entry(root,textvariable=self.a).place(x=450, y=440,width=200)
        address2 = Label(root, text="Address line 2",font="cambria 16 italic", bg="black", fg="white").place(x=720, y=440)
        adr2 = Entry(root,textvariable=self.a1).place(x=920, y=440,width=200)
        email = Label(root, text=" E-mail",font="cambria 16 italic", bg="black", fg="white").place(x=220, y=520)
        ee1 = Entry(root,textvariable=self.e1).place(x=450, y=520,width=200)
        website = Label(root, text="Website",font="cambria 16 italic",bg="black", fg="white").place(x=720, y=520)
        w1 = Entry(root,textvariable=self.w).place(x=920, y=520,width=200)
        fax = Label(root, text="Fax details",font="cambria 16 italic",bg="black", fg="white").place(x=220, y=580)
        f1 = Entry(root,textvariable=self.f).place(x=450, y=580,width=500)

        btn = Button(root,text="SUBMIT",font="cambria 18 bold italic",bg = "pink",fg = "black", command=self.newframe).place(x=450, y = 630)
        btn2 = Button(root,text="EXIT",font="cambria 18 bold italic",bg = "lightblue",fg = "black", command=root.quit).place(x=850, y = 630)
root = Tk()
photo = PhotoImage(file="VISCA6.png")
label = Label(root, image=photo).place(x=0, y=0)
app = Frames()
app.mainframe(root)


root.mainloop()
