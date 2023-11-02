# دفترچه تلفن نوشته شده برای پای چارم

from logging import root
from tkinter import messagebox
from tkinter import *
import webbrowser
import pyperclip
import random
import os


root = Tk()
root.title('Phone Book')
root.geometry('1000x400')
background = '#121212'
root.config(bg= background)

def Finding_btn():
    with open('E:\Programs\myproject\phonebook\Data2.txt', 'r') as f:
        for line in f:
            if line == name_entry:

                listbox.insert(0,line,END)
            else:
                listbox.insert("tank yuo",name_entry)

    # listbox.insert(END,line)
                name_entry.delete(0, END)
                phone_entry.delete(0, END)
                Mobile_entry.delete(0, END)
                Address_entry.delete(0, END)
                Maill_entry.delete(0, END)


def add_contact() :
    contact_string = name_entry.get() + ': ' + phone_entry.get() + ': ' + Mobile_entry.get() + ': '  + Address_entry.get() + ': ' + Maill_entry.get()

    listbox.insert(END,  contact_string)

    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    Mobile_entry.delete(0, END)
    Address_entry.delete(0, END)
    Maill_entry.delete(0, END)

def delete_contact():
    listbox.delete(ANCHOR)

def save_list():
    """ Save the list to a simple txt file """

    with open('E:\Programs\myproject\phonebook\Data2.txt' ,'w') as  f:
        list_tuple = listbox.get(0, END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item +'\n')

def open_list():
    with open('E:\Programs\myproject\phonebook\Data2.txt' ,'r') as  f:
        for line in f:
            listbox.insert(END, line)

def exit():
    choice = messagebox.askquestion('Exit Aplictation', 'Are you sure you want to ciose the application ?')
    if choice =='yes':
        root.destroy()
    else:
        return


name_label = Label(root, text='Contact Name:', bg=background,  fg='white',  font=('calibri' ,12), anchor='w', justify=LEFT )
name_label. place(relx=0.1, rely=0.1, anchor='c')

name_entry = Entry(root, bg='white', fg=background, width=40, borderwidth=4)
name_entry. place(relx=0.3, rely=0.1, anchor='c')

phone_label = Label(root, text='Contact phone:', bg=background,  fg='white',  font=('calibri' ,12), anchor='w', justify=LEFT )
phone_label. place(relx=0.1, rely=0.2, anchor='c')


phone_entry = Entry(root, bg='white', fg=background, width=40, borderwidth=4)
phone_entry. place(relx=0.3, rely=0.2, anchor='c')

Mobile_label = Label(root, text=' Contact Mobile:', bg=background,  fg='white',  font=('calibri' ,12), anchor='w', justify=LEFT )
Mobile_label. place(relx=0.1, rely=0.3, anchor='c')


Mobile_entry = Entry(root, bg='white', fg=background, width=40, borderwidth=4)
Mobile_entry. place(relx=0.3, rely=0.3, anchor='c')

Address_label = Label(root, text='  Contact Address:', bg=background,  fg='white',  font=('calibri' ,12), anchor='w', justify=LEFT )
Address_label. place(relx=0.1, rely=0.4, anchor='c')


Address_entry = Entry(root, bg='white', fg=background, width=40, borderwidth=4)
Address_entry. place(relx=0.3, rely=0.4, anchor='c')

Maill_label = Label(root, text='Contact Maill :', bg=background,  fg='white',  font=('calibri' ,12), anchor='w', justify=LEFT )
Maill_label. place(relx=0.1, rely=0.5, anchor='c')


Maill_entry = Entry(root, bg='white', fg=background, width=40, borderwidth=4)
Maill_entry. place(relx=0.3, rely=0.5, anchor='c')

Finding_btn = Button(root, text='Finding contact',  bg=background, fg='white', borderwidth=3, padx=160
                     ,command=Finding_btn )
Finding_btn.place(relx=0.25, rely=0.60, anchor='c')

add_btn = Button(root, text='Add Contact',  bg=background, fg='white', borderwidth=3, padx=68 ,command=add_contact )
add_btn.place(relx=0.15, rely=0.70, anchor='c')

save_btn = Button(root, text='Save List',  bg=background, fg='white' ,borderwidth=3, padx=82 ,command=save_list )
save_btn. place(relx=0.37, rely=0.70, anchor='c')

deletePhone = Button(root, text='Delete Contact',  bg=background, fg='white', borderwidth=3, padx=177 ,  command=delete_contact)
deletePhone.place(relx=0.26, rely=0.80, anchor='c')

exit = Button(root, text='Exit App',  bg=background, fg='white' ,borderwidth=3, padx=194, command=exit )
exit.place(relx=0.26, rely=0.90, anchor='c')

listbox = Listbox(root, width=90, height=22)
listbox.place(relx=0.71, rely=0.49, anchor='c')



open_list()
root.mainloop ()
