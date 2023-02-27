"""
A program that stores this book information:
Title, Author
Year, ISBN

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend

window = Tk()
window.wm_title("Bookstore")

#connecting backend and frontend
#function for button and clicks
def get_selected_row(event):
    try:
        global selected_tuple             #global variable
        index = list1.curselection()[0] #tuple ko first item selected
        #print(index)
        selected_tuple = list1.get(index)
        #print(selected_tuple)
        #fill entries with selected items
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
# Since the listbox is empty,  list1.curselection()  will be an empty list with no items.
# Trying to access the first item on the list with [0]  in line 3 will throw 
# an error because there is no first item in the list. 

def view_command():
    list1.delete(0,END)       #helps to stop repeat view ie.empty the listbox
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)       #helps to stop repeat view 
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())   #this line is enough
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())) #to show in listbox

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())    

#frontend
#label
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text='Author')
l2.grid(row=0,column=2)

l3 = Label(window,text='Year')
l3.grid(row=1,column=0)

l4 = Label(window,text='ISBN')
l4.grid(row=1,column=2)

#entry
title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

#listbox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

#lets connect listbox and scrollbar
list1.configure(yscrollcommand=sb1.set) #vertical scroll
sb1.configure(command=list1.yview)

#binding a function to a widget
list1.bind('<<ListboxSelect>>',get_selected_row)

#button
b1 = Button(window,text='View all',width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text='Search entry',width=12,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text='Add entry',width=12,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text='Update',width=12,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text='Delete',width=12,command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text='Close',width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()