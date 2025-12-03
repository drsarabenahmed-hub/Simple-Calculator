import tkinter as tk

# Create window
window = tk.Tk()
window.title("Simple calculator")
window.geometry("300x400")

# Entry field
entry = tk.Entry(window, width=15, font=("Arial", 24), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button click function
def button_click(number):
    entry.insert(tk.END, number)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button function wrapper
def make_button(text, row, col):
    btn = tk.Button(window, text=text, width=5, height=2, font=("Arial", 14),
                    command=lambda: button_click(text))
    btn.grid(row=row, column=col, padx=5, pady=5)

# Create number buttons
numbers = [
    (1,1,0), (2,1,1), (3,1,2),
    (4,2,0), (5,2,1), (6,2,2),
    (7,3,0), (8,3,1), (9,3,2),
    (0,4,1)
]

for num, r, c in numbers:
    make_button(num, r, c)

# Operation buttons
ops = [
    ('+',1,3), ('-',2,3),
    ('*',3,3), ('/',4,3)
]

for op, r, c in ops:
    make_button(op, r, c)

# Equal button
equal_btn = tk.Button(window, text="=", width=5, height=2, font=("Arial", 14),
                      bg="lightgreen", command=button_equal)
equal_btn.grid(row=4, column=2, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(window, text="C", width=5, height=2, font=("Arial", 14),
                      bg="lightcoral", command=button_clear)
clear_btn.grid(row=4, column=0, padx=5, pady=5)

window.mainloop()
