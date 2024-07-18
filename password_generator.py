from tkinter import *
import random

def click_me():
    global root,enter
    global character
    lenght = len(character)
    password=""
    for i in range(0,enter.get()):
        password+=character[random.randint(0,lenght-1)]

    passl = Label(root, text=password,font="lucida 13 bold")
    passl.pack()




root = Tk()
root.geometry("600x500")
root.title("My Password generator")

character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
             '1','2','3','4','5','6','7','8','9','0',
             '@','#','$','_']

mainl = Label(root, text="Password Generator", font="comicsansms 40 bold", borderwidth=3, relief=RIDGE)
mainl.pack(fill=X)
info = "Welcome to our GUI\nIn this GUI, enter the number of character you want in your password and password will be generated accordingy"
infolabel = Label(root, text=info, font="comicsansms 14 bold", borderwidth=3, relief=RIDGE)
infolabel.pack(fill=X)

label_entry = Label(root,text="enter the number of character you want in your password",font="lucida 12 bold")
label_entry.pack(pady=10)

enter = IntVar()
enter.set("")
entry_enter = Entry(root,textvariable=enter,font="lucida 12 bold")
entry_enter.pack()

b = Button(root,text="click me to generate password",font="lucida 6 bold",command=click_me)
b.pack()
root.mainloop()