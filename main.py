from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Temperature convertor")
celsius_label = ttk.Label(root, text="Celsius")
celsius_label.grid(row=0, column=0)
fahrenheit_label = ttk.Label(root, text="Fahrenheit")
fahrenheit_label.grid(row=0, column=1)

celsius_input = DoubleVar()
fahrenheit_input = DoubleVar()

celsius_entry = ttk.Entry(root, textvariable=celsius_input)
celsius_entry.grid(row=1, column=0, padx=5, pady=5)
fahrenheit_entry = ttk.Entry(root, textvariable=fahrenheit_input)
fahrenheit_entry.grid(row=1, column=1, padx=5, pady=5)

celsius_button = ttk.Button(root, text="Convert to Fahrenheit")
celsius_button.grid(row=2, column=0, padx=5, pady=5)
fahrenheit_button = ttk.Button(root, text="Convert to Celsius")
fahrenheit_button.grid(row=2, column=1, padx=5, pady=5, sticky="WE")

root.mainloop()
