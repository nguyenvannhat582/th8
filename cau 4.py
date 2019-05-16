from tkinter import*
window = Tk()
window.title("welcome to likegeeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="Button was clinked !!")
btn=Button(window,text="click me", command=clicked)
btn.grid(column=1,row=0)
window.mainloop()