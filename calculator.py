from tkinter import *


root =Tk()
root.title("Simple Calculator")

size = Entry(root,width=40 , borderwidth=6)
size.grid(row = 0 , column = 0 , columnspan = 3 ,padx = 10 , pady = 10)
size.insert(0 , "")

icon = PhotoImage(file = 'Calculator.png')
root.tk.call('wm' , 'iconphoto' , root._w , icon)


def button_click(number):
	current = size.get()
	size.delete(0 , END)
	size.insert(0 , str(current) + str(number))
	
def button_clear():
	size.delete(0 , END)

def button_add():
	add = size.get()
	global f_num
	global math
	math = "addition"
	f_num = int(add)
	size.delete(0 , END)
	

def button_sub():
	add = size.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(add)
	size.delete(0 , END)
	

def button_div():
	add = size.get()
	global f_num
	global math
	math = "division"
	f_num = int(add)
	size.delete(0 , END)
	

def button_mult():
	add = size.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(add)
	size.delete(0 , END)
	

def button_equal():
	second_number= size.get()
	size.delete(0 , END)

	if math == "addition":
		size.insert(0 , f_num + int(second_number))

	if math == "subtraction":
		size.insert(0 , f_num - int(second_number))

	if math == "multiplication":
		size.insert(0 , f_num * int(second_number))
		
	if math == "division":
		size.insert(0 , f_num / int(second_number))		

	

button_1 = Button(root , text="1" , padx=40 , pady=20 , command = lambda: button_click(1))
button_2 = Button(root , text="2" , padx=40 , pady=20 , command = lambda: button_click(2))
button_3 = Button(root , text="3" , padx=40 , pady=20 , command = lambda: button_click(3))
button_4 = Button(root , text="4" , padx=40 , pady=20 , command = lambda: button_click(4))
button_5 = Button(root , text="5" , padx=40 , pady=20 , command = lambda: button_click(5))
button_6 = Button(root , text="6" , padx=40 , pady=20 , command = lambda: button_click(6))
button_7 = Button(root , text="7" , padx=40 , pady=20 , command = lambda: button_click(7))
button_8 = Button(root , text="8" , padx=40 , pady=20 , command = lambda: button_click(8))
button_9 = Button(root , text="9" , padx=40 , pady=20 , command = lambda: button_click(9))
button_0 = Button(root , text="0" , padx=40 , pady=20 , command = lambda: button_click(0))
button_add=Button(root , text="+" , padx=40 , pady=20 , command = button_add )
button_sub=Button(root , text="-" , padx=40 , pady=20 , command = button_sub)
button_div=Button(root , text="%" , padx=40 , pady=20 , command = button_div)
button_mult=Button(root , text="X" , padx=40 , pady=20 , command = button_mult)
button_equal=Button(root , text="=" , padx = 40 , pady = 20 , command = button_equal)
button_clear=Button(root , text="AC" , padx = 35 , pady=20 , command = button_clear )



button_1.grid(row=3 , column=0)
button_2.grid(row=3 , column=1)
button_3.grid(row=3 , column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)

button_7.grid(row=1 , column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1 , column=2)

button_0.grid(row=4 , column=1)

button_add.grid(row=1 , column=3)
button_sub.grid(row=2 , column=3)
button_mult.grid(row=3 , column=3)
button_div.grid(row=4 , column=3)

button_equal.grid(row=4 , column=2)
button_clear.grid(row=4 , column=0)





root.mainloop()