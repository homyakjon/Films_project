import webbrowser
import tkinter
from tkinter import ttk


go = tkinter.Tk()
go.geometry("600x250")


def link():
    webbrowser.open('https://kinogo.biz')


def link_one():
    webbrowser.open('https://kinogo.biz/fentezi')


def link_two():
    webbrowser.open('https://kinogo.biz/vestern/')


def link_three():
    webbrowser.open('https://kinogo.biz/triller/')


def link_for():
    webbrowser.open('https://kinogo.biz/uzhasy/')


def link_five():
    webbrowser.open('https://kinogo.biz/boevik/')


def link_six():
    webbrowser.open('https://kinogo.biz/komedia/')


f = ttk.Button(go, text='Films Menu', command=link)
f1 = ttk.Button(go, text='Films Fentezi', command=link_one)
f2 = ttk.Button(go, text='Films Vestern', command=link_two)
f3 = ttk.Button(go, text='Films Triller', command=link_three)
f4 = ttk.Button(go, text='Films Horror', command=link_for)
f5 = ttk.Button(go, text='Films Action', command=link_five)
f6 = ttk.Button(go, text='Films Comedy', command=link_six)
f.pack()
f1.pack()
f2.pack()
f3.pack()
f4.pack()
f5.pack()
f6.pack()
go.mainloop()

