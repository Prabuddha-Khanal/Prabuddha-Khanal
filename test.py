from tkinter import *
import webbrowser
from googlesearch import search

class MyWindow:
    
    def __init__(self, win):
        self.lbl1=Label(win, text='Keyword')
        self.lbl2=Label(win, text='Website')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.btn1 = Button(win, text='Start')
        self.btn2=Button(win, text='Stop')
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.b1=Button(win, text='Start', command=self.add)
        self.b2=Button(win, text='Stop')
        self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=100, y=150)
        self.b2.place(x=200, y=150)
    def add(self):
        query=(self.t1.get())
        url=(self.t2.get())
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")

        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.com/search_q=" + query)
        for j in search(query, tld="co.in", num=2, start=0, stop=1, pause=4):
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(j)

    def sub(self, event):
        print('hi')

window=Tk()
mywin=MyWindow(window)
window.title('Site Booster')
window.geometry("400x300+10+10")
window.configure(bg='#34495E')
window.mainloop()