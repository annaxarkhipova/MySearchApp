#Создание поискового окна с выбором браузера
from tkinter import *
import webbrowser

#Создание рамки
root = Tk()
root.title('Search')
root.geometry('300x100')

#Создание поискового поля
search_query = StringVar()
search_entry = Entry(textvariable=search_query)
search_entry.grid(row=1, column=1)

#Условия при выборе кнопок браузера
#pass - исключение других условий
url = "https://www.google.ru/search?q="

def openweb():
  if browser_id.get() == 1:
    webbrowser.get(using='chrome').open(url+search_query.get(), new=1)
    pass
  elif browser_id.get() == 2:
    webbrowser.get(using='safari').open(url+search_query.get(), new=1)
    pass

#Настройка кнопки поиска и кнопок браузера
btn = Button(text = "Search", command=openweb, bg="white", fg="pink")
btn.grid(row=2, column=1, rowspan=2)

browser_id = IntVar()
browser_id.set() #выбор бразуера по дефолту

chrome_checkbutton = Radiobutton(text="Chrome", value=1, variable=browser_id)
chrome_checkbutton.grid(row=2, column=2, sticky=W)
 
safari_checkbutton = Radiobutton(text="Safari", value=2, variable=browser_id)
safari_checkbutton.grid(row=3, column=2, sticky=W)


root.mainloop()
