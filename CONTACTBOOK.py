from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x550')
root.config(bg='#d9534f')
root.title("SAHANA'S CONTACT BOOK")
root.resizable(0, 0)

contactlist =[]

Name = StringVar()
Number = StringVar()
Search = StringVar()

frame = Frame(root)
frame.pack(side=BOTTOM)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Helvetica', 14, 'bold'), bg="#f0fffc", width=20, height=13,
                 borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill in all the information")


def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Successfully Updated Contact")
        EntryReset()
        Select_set()
    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please select a contact")
        else:
            messagebox.showerror("Error", "Please fill in all the information")


def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', f'Are you sure you want to delete {select.get(Selected())}?')
        if result:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select a contact')


def VIEW():
    if len(select.curselection()) != 0:
        Name.set(contactlist[Selected()][0])
        Number.set(contactlist[Selected()][1])
    else:
        messagebox.showerror("Error", "Please select a contact")


def SearchContact():
    search_name = Search.get()
    for i, contact in enumerate(contactlist):
        if contact[0] == search_name:
            select.selection_clear(0, END)
            select.selection_set(i)
            select.activate(i)
            select.see(i)
            VIEW()
            return
    messagebox.showinfo("Search Result", f"No contact found with the name '{search}'")


def EXIT():
    root.destroy()


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


def EntryReset():
    Name.set("")
    Number.set("")


Label(root, text='Name', font=("Helvetica", 20, "bold"), bg='#d9534f', fg='white').place(x=50, y=50)
Entry(root, textvariable=Name, width=30, font=("Helvetica", 16)).place(x=200, y=55)
Label(root, text='Contact No.', font=("Helvetica", 20, "bold"), bg='#d9534f', fg='white').place(x=50, y=100)
Entry(root, textvariable=Number, width=30, font=("Helvetica", 16)).place(x=200, y=105)

Label(root, text='Search Name', font=("Helvetica", 20, "bold"), bg='#d9534f', fg='white').place(x=50, y=170)
Entry(root, textvariable=Search, width=30, font=("Helvetica", 16)).place(x=200, y=175)

Button(root, text=" ADD", font=('Helvetica', 18, 'bold'), bg='#8B4513', fg='white', command=AddContact).place(x=50, y=230)
Button(root, text="EDIT", font=('Helvetica', 18, 'bold'), bg='#8B4513', fg='white', command=UpdateDetail).place(x=50, y=280)
Button(root, text="DELETE", font=('Helvetica', 18, 'bold'), bg='#8B4513', fg='white', command=Delete_Entry).place(x=50, y=330)
Button(root, text="VIEW", font=('Helvetica', 18, 'bold'), bg='#8B4513', fg='white', command=VIEW).place(x=50, y=380)
Button(root, text="SEARCH", font=('Helvetica', 18, 'bold'), bg='#8B4513', fg='white', command=SearchContact).place(x=50, y=430)
Button(root, text="RESET", font=('Helvetica', 18, 'bold'), bg='#8B4513', fg='white', command=EntryReset).place(x=50, y=480)
Button(root, text="EXIT", font=('Helvetica', 24, 'bold'), bg='#d9534f', fg='white', command=EXIT).place(x=250, y=470)

Select_set()
root.mainloop()
