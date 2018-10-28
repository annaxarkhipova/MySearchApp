#Создание поискового окна с выбором браузера
from tkinter import *
import webbrowser

#создание класса,
class Application(Frame):
     def __init__(self, master):
          super(Application, self).__init__(master)
          self.grid()
          self.create_widgets()
     
#поле для ввода текста
          self.search_query = StringVar()
          self.search_ent = Entry(self)
          self.search_ent.grid(row=2,column=3, padx=70, pady=0)

          url= "https://google.ru/search?q="

     def openweb():
          if browser_id.get() == 1:
               webbrowser.get(using='Chrome').open(url+search_query.get(), new=1)
               pass
          elif browser_id.get() == 2:
               webbrowser.get(using='Safari').open(url+search_query.get(), new=1)
               pass
          else:
               webbrowser.get(using='default').open(url+search_query.get(), new=1)
               pass
          
#создание кнопок
     def create_widgets(self): 

          self.btn = Button(self, text = "Search",
             command=openweb             ,
             padx=40, pady=10,
             bg="white",fg="pink")
          self.btn.grid(row=4, column=0, padx = 20, pady = 0)

#выбор браузера
          browser_id = IntVar()
          self.chrome_but = Radiobutton(text="Chrome",
                                                value=1, variable=browser_id)
          self.chrome_but.grid(row=3, column=1, sticky=W,
                                       padx = 0, pady = 0)

          self.safari_but = Radiobutton(text="Safari",
                                                value=0, variable=browser_id)
          self.safari_but.grid(row=4, column=1, sticky=W,
                                       padx = 0, pady = 0)
       
# main
root = Tk()
root.title("Search")
root.geometry("470x150")

app = Application(root)

root.mainloop()
