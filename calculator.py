from tkinter import *


def btn_click(number):
    global val
    val = val+str(number)
    data.set(val)



def button_clear():
    global val
    val = ""
    data.set("")


def button_equal():
    global val
    result = str(eval(val))
    data.set(result)



root = Tk()
root.title("Calculator")
root.resizable(False, False)
val = ""
data = StringVar()
entry = Entry(root, textvariable=data, width=15, justify="right", font=('Arial', 20), bg="light blue", fg="white")
entry.grid(row=0, column=0, columnspan=4)

button_addition = Button(root, text="+", width=5, height=1, command=lambda: btn_click('+'), bg="gold")
button_addition.grid(row=1, column=0)
button7 = Button(root, text="7", width=5, height=1, command=lambda: btn_click(7), bg="gold")
button7.grid(row=1, column=1)
button8 = Button(root, text="8", width=5, height=1, command=lambda: btn_click(8), bg="gold")
button8.grid(row=1, column=2)
button9 = Button(root, text="9", width=5, height=1, command=lambda: btn_click(9), bg="gold")
button9.grid(row=1, column=3)

button_minus = Button(root, text="-", width=5, height=1, command=lambda: btn_click('-'), bg="gold")
button_minus.grid(row=2, column=0)
button4 = Button(root, text="4", width=5, height=1, command=lambda: btn_click(4), bg="gold")
button4.grid(row=2, column=1)
button5 = Button(root, text="5", width=5, height=1, command=lambda: btn_click(5), bg="gold")
button5.grid(row=2, column=2)
button6 = Button(root, text="6", width=5, height=1, command=lambda: btn_click(6), bg="gold")
button6.grid(row=2, column=3)

button_multiplication = Button(root, text="*", width=5, height=1, command=lambda: btn_click('*'), bg="gold")
button_multiplication.grid(row=3, column=0)
button1 = Button(root, text="1", width=5, height=1, command=lambda: btn_click(1), bg="gold")
button1.grid(row=3, column=1)
button2 = Button(root, text="2", width=5, height=1, command=lambda: btn_click(2), bg="gold")
button2.grid(row=3, column=2)
button3 = Button(root, text="3", width=5, height=1, command=lambda: btn_click(3), bg="gold")
button3.grid(row=3, column=3)

button_division = Button(root, text="/", width=5, height=1, command=lambda: btn_click('/'), bg="gold")
button_division.grid(row=4, column=0)
btn_c = Button(root, text="C", width=5, height=1, command=button_clear, bg="gold")
btn_c.grid(row=4, column=1)
btn0 = Button(root, text="0", width=5, height=1, command=lambda: btn_click(0), bg="gold")
btn0.grid(row=4, column=2)
btn_equ = Button(root, text="=", width=5, height=1, command=button_equal, bg="gold")
btn_equ.grid(row=4, column=3)

root.mainloop()
