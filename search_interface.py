#Description

from tkinter import *

root = Tk()
root.title('Search')
root.geometry('400x200')

app = Frame(root, bg='pink')
app.grid()

lang = IntVar()
 
chrome_checkbutton = Radiobutton(text="Chrome", value=1, variable=lang, padx=15, pady=10)
chrome_checkbutton.grid(row=1, column=0, sticky=W)
 
safari_checkbutton = Radiobutton(text="Safari", value=2, variable=lang, padx=15, pady=10)
safari_checkbutton.grid(row=2, column=0, sticky=W)

message = StringVar()
message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor='c')
       
Button(root, text = 'Search').place(x = 150, y = 100, width=90)
def __init__(self, btn):
     self.btn = Button(root, width=25,height=10, bg="white",fg="pink")
     self.btn.bind("<Button-1>", )

root.mainloop()
