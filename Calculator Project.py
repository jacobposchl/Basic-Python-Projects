
import tkinter as tk
expression = ""


#Update Input Field
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

#Clear the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

#Evaluate final expression
def btn_equal():
    global expression 
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

#Main Window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.resizable(0, 0)

expression = ""
input_text = tk.StringVar()

#Display Entry Widget
input_frame = tk.Frame(root, width = 312, height = 50, bd = 0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

input_field = tk.Entry(input_frame, font=("arial", 18, "bold"), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

#Button Frame
btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

#First Row Buttons
clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: btn_clear())
clear.grid(row=0, column=0, columnspan=3)
divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("/"))
divide.grid(row=0, column=3)

# Second row Buttons
seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(7))
seven.grid(row=1, column=0)
eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(8))
eight.grid(row=1, column=1)
nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(9))
nine.grid(row=1, column=2)
multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("*"))
multiply.grid(row=1, column=3)

# Third row Buttons
four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(4))
four.grid(row=2, column=0)
five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(5))
five.grid(row=2, column=1)
six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(6))
six.grid(row=2, column=2)
subtract = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("-"))
subtract.grid(row=2, column=3)

# Fourth row Buttons
one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(1))
one.grid(row=3, column=0)
two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(2))
two.grid(row=3, column=1)
three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(3))
three.grid(row=3, column=2)
add = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("+"))
add.grid(row=3, column=3)

# Fifth row Buttons
zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click(0))
zero.grid(row=4, column=0, columnspan=2)
decimal = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_click("."))
decimal.grid(row=4, column=2)
equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: btn_equal())
equals.grid(row=4, column=3)

#Run loop
root.mainloop()