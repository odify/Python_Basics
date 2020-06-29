from tkinter import *


from tkinter import messagebox as msg

from datetime import date
#function part will go here

def exp():
    msg.showinfo("This is notice","Thanks for showing intrest. \nBut you know that i am lerner\nand still learning. \nTry in next version")
def exit_cm():
    ans = msg.askquestion("EXIT","Do you want to exit this GUI")
    if ans == "yes":
        exit()
def info():
    msg.showwarning("Warning !","i dont know more then this . \nthis is my intro.\nKeep in mind this is computer GUI \nall the functions of computer \nwill work here like incresing window \nsize etc.")
def nst_mnu():
    msg.showinfo("Information for this section","it was just made for \ntesting the nested menu.")
def day(day, month, year):


#    d1={--------------------------}

    month = d1[month]
    input_date = date(year, month, day)
    dy_label['text'] = input_date.strftime('%A').upper()
    
root = Tk()
root.geometry("400x800+100+100")
root.geometry('500x500')
#menu bar code goes here
frame = Frame(root)
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu,bg="skyblue")
aks_menu = Menu(main_menu,bg="orange")
hlp_menu = Menu(main_menu,bg="pink")
main_menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="open", command=exp)
file_menu.add_command(label="new", command=exp)
file_menu.add_command(label="save", command=exp)
file_menu.add_command(label="save as", command=exp)
file_menu.add_command(label="close", command=exit_cm)
main_menu.add_cascade(label="about me",menu=aks_menu)
aks_menu.add_command(label="really! click here",command=info)
main_menu.add_cascade(label="help",menu=hlp_menu)
hlp_menu.add_command(label="no action")
hlp_menu.add_command(label="sorry")
sub_menu = Menu(hlp_menu,bg='yellow')
hlp_menu.add_cascade(label="this is something",menu=sub_menu)
sub_menu.add_command(label="nested menu1",command=nst_mnu)
sub_menu.add_command(label="nested menu2",command=nst_mnu)
sub_menu.add_command(label="nested menu3",command=nst_mnu)
sub_menu.add_command(label="nested menu4",command=nst_mnu)
frame.pack()
#menu bar code ends here
#now the main part
frame1 = Frame(root)
d = IntVar()
entry1 = Entry(frame1,textvariable=d,bg="yellow")
d.set(1)
entry1.grid(row=1,column=2)

m = StringVar()
entry2 = Entry(frame1,textvariable=m,bg="pink")
m.set("january")
entry2.grid(row=2,column=2)

y = IntVar()
entry3= Entry(frame1,textvariable=y,bg="orange")
y.set(2020)
entry3.grid(row=3,column=2)

Label(frame1,text="date").grid(row=1,column=1,sticky=E)
Label(frame1,text="month").grid(row=2,column=1,sticky=E)
Label(frame1,text="year").grid(row=3,column=1,sticky=E)
Label(frame1,text="__________").grid(row=4,column=1)
Label(frame1,text="____________________________").grid(row=4,column=2)

btn = Button(frame1,text="find the day",command=lambda: day(int(entry1.get()), entry2.get().capitalize(), int(entry3.get())),bg="yellow",fg="orange")
btn.grid(row=5,column=2)

Label(frame1,text="________").grid(row=6,column=1)

Label(frame1,text="____________________").grid(row=6,column=2)


Label(frame1,text="day").grid(row=7,column=1,sticky=E)


frame1.place(x=50,y=180)



dy_label = Label(frame1,text='')


dy_label.grid(row=7,column=2)


root.mainloop()