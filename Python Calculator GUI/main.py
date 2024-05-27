import tkinter as tk

def on_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input and output
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == "C":
        button = tk.Button(root, text=text, padx=30, pady=20, command=clear_entry)
    elif text == "=":
        button = tk.Button(root, text=text, padx=30, pady=20, command=calculate)
    else:
        button = tk.Button(root, text=text, padx=30, pady=20, command=lambda val=text: on_click(val))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
