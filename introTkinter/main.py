import tkinter

root = tkinter.Tk()

root.geometry("800x500") #creates window with width 800px and height 500px
root.title("My First GUI")

label = tkinter.Label(root, text="Hello World", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tkinter.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10)


button = tkinter.Button(root, text="Click Me!", font=('Arial', 18)) #button
button.pack(padx=10, pady=10)

#grid of buttons
buttonframe = tkinter.Frame(root)
buttonframe.columnconfigure(0, weight = 1)
buttonframe.columnconfigure(1, weight = 1)
buttonframe.columnconfigure(2, weight = 1)

btn1 = tkinter.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tkinter.W+tkinter.E)

btn2 = tkinter.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tkinter.W+tkinter.E)

btn3 = tkinter.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tkinter.W+tkinter.E)

btn4 = tkinter.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tkinter.W+tkinter.E)

btn5 = tkinter.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tkinter.W+tkinter.E)

btn6 = tkinter.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tkinter.W+tkinter.E)

buttonframe.pack(fill='x')

anotherbtn = tkinter.Button(root, text="TEST")
anotherbtn.place(x=200, y=200, height=100, width=100)











root.mainloop()