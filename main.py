import tkinter as tk

app=tk.Tk()
app.title("Basic Calculator")

entry = tk.Entry(app, width=20)
entry.grid(row=0, column=0, columnspan=6)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)

    except Exception:
        entry.delete(0,tk.END)
        entry.insert(0, "Error")

button1 = tk.Button(app, text="1", command=lambda : button_click(1))
button2 = tk.Button(app, text="2", command=lambda : button_click(2))
button3 = tk.Button(app, text="3", command=lambda : button_click(3))
button4 = tk.Button(app, text="4", command=lambda : button_click(4))
button5 = tk.Button(app, text="5", command=lambda : button_click(5))
button6 = tk.Button(app, text="6", command=lambda : button_click(6))
button7 = tk.Button(app, text="7", command=lambda : button_click(7))
button8 = tk.Button(app, text="8", command=lambda : button_click(8))
button9 = tk.Button(app, text="9", command=lambda : button_click(9))
button0 = tk.Button(app, text="0", command=lambda : button_click(0))

button_add = tk.Button(app, text="+", command=lambda : button_click("+"))
button_sub = tk.Button(app, text="-", command=lambda : button_click("-"))
button_mul = tk.Button(app, text="*", command=lambda : button_click("*"))
button_div = tk.Button(app, text="/", command=lambda : button_click("/"))
button_mod = tk.Button(app, text="%", command=lambda : button_click("%"))

button_clear = tk.Button(app, text="C", command=clear)
button_equal = tk.Button(app, text="=", command=calculate)

button1.grid(row=1, column=0, columnspan=1)
button2.grid(row=1, column=1, columnspan=1)
button3.grid(row=1, column=2, columnspan=1)
button_clear.grid(row=1, column=3, columnspan=1)

button4.grid(row=2, column=0, columnspan=1)
button5.grid(row=2, column=1, columnspan=1)
button6.grid(row=2, column=2, columnspan=1)
button_add.grid(row=2, column=3, columnspan=1)

button7.grid(row=3, column=0, columnspan=1)
button8.grid(row=3, column=1, columnspan=1)
button9.grid(row=3, column=2, columnspan=1)
button_sub.grid(row=3, column=3, columnspan=1)

button0.grid(row=4, column=0, columnspan=1)
button_mul.grid(row=4, column=1, columnspan=1)
button_div.grid(row=4, column=2, columnspan=1)
button_mod.grid(row=4, column=3, columnspan=1)

button_equal.grid(row=5, column=0)


app.mainloop()






