from textwrap import fill
from tkinter import *
import tkinter as tk
from turtle import width
from PIL import Image, ImageTk

global path

# Hover Button Module
def hoverActive(boton, color1, color2, color3):
	boton.configure(bg=color1)
	def fuera(e):
		boton.configure(bg=color1)
	def dentro(e):
		boton.configure(bg=color2)
	def activo(e):
		boton.configure(activebackground=color3)
	boton.bind("<Enter>", dentro)
	boton.bind("<Leave>", fuera)
	boton.bind("<ButtonPress-1>", activo)

# define of gui of app
root = tk.Tk()
root.title('Template')
# Designate Height and Width of our app
app_width = 750
app_height = 297
# The Height and Width of our pc screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
label_1 = Label(root,width="550",height="285",bg="#EE4E34") #to colorate the space of application
label_1.place(x=0,y=0)
root.resizable(False,False)
root.iconbitmap('logo.ico')

image=Image.open('logo.ico')
img=image.resize(( 30, 30))
my_img=ImageTk.PhotoImage(img)

Btn1 = Button(root,fg= "#000", image=my_img,borderwidth=1)
# Btn1 = Button(root,fg= "#000",text="Logo",borderwidth=0,width=20, height=3) #if you want to use text and not logo
Btn1.grid(column=1, row=1, ipadx=56,ipady=10)

var = StringVar()
var.set("Wirte Here")
labelAfterButton = Label( root,fg= "#000", textvariable=var, relief=RAISED ,borderwidth=3,width=86 , height=3)
labelAfterButton.grid(column=2, row=1)

Btn2 = Button(root,fg= "#000",text="Click 1",borderwidth=0,width=20, height=2)
Btn2.grid(column=1, row=2)

Btn3 = Button(root,fg= "#000",text="Click 2",borderwidth=0,width=20, height=2)
Btn3.grid(column=1, row=3)

Btn4 = Button(root,fg= "#000",text="Click 3",borderwidth=0,width=20, height=2)
Btn4.grid(column=1, row=4)

Btn5 = Button(root,fg= "#000",text="Click 4",borderwidth=0,width=20, height=2)
Btn5.grid(column=1, row=5)

Btn6 = Button(root,fg= "#000",text="Click 5",borderwidth=0,width=20, height=2)
Btn6.grid(column=1, row=6)

Btn7 = Button(root,fg= "#000",text="Click 6",borderwidth=0,width=20, height=2)
Btn7.grid(column=1, row=7)

# Application of hover function
hoverActive(Btn1, "#FCEDDA", "#FCE77D", "#ffffff")
hoverActive(Btn2, "#FCEDDA", "#FCE77D", "#ffffff")
hoverActive(Btn3, "#FCEDDA", "#FCE77D", "#ffffff")
hoverActive(Btn4, "#FCEDDA", "#FCE77D", "#ffffff")
hoverActive(Btn5, "#FCEDDA", "#FCE77D", "#ffffff")
hoverActive(Btn6, "#FCEDDA", "#FCE77D", "#ffffff")
hoverActive(Btn7, "#FCEDDA", "#FCE77D", "#ffffff")
hoverActive(labelAfterButton, "#FCEDDA", "#FCE77D", "#ffffff")

footer = Label(root, text = "Bilal Belli | ©2022",bg="#FCEDDA",width=107)
footer.place(x=0,y=276)

root.mainloop()