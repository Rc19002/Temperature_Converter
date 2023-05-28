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

# user input box
celsius_entry = ttk.Entry(root, textvariable=celsius_input)
celsius_entry.grid(row=1, column=0, padx=5, pady=5)

fahrenheit_entry = ttk.Entry(root, textvariable=fahrenheit_input)
fahrenheit_entry.grid(row=1, column=1, padx=5, pady=5)

celsius_button = ttk.Button(root, text="Convert to Fahrenheit")
celsius_button.grid(row=2, column=0, padx=5, pady=5)

fahrenheit_button = ttk.Button(root, text="Convert to Celsius")
fahrenheit_button.grid(row=2, column=1, padx=5, pady=5, sticky="WE")


# help gui pop up
def help_gui():
    help_screen = Toplevel()
    help_screen.title("Help")
    help_label = Label(help_screen, text="Make sure that the input is a actual number,\n"
                                         "not the lettered form of the numbers."
                                         "\n\nNo letters should be included in the input."
                                         "\n\nYou do not need to put the unit of the temperature."
                                         "\n\nclick convert to whatever you want to convert and it should convert.")
    help_label.grid(row=0, column=0)


help_button = ttk.Button(root, text="Help", command=help_gui)
help_button.grid(row=1, column=2, padx=5, pady=5)


# log gui pop up
def log_gui():
    log = Toplevel()
    log.title("History/Log")


conversion_log_button = ttk.Button(root, text="History", command=log_gui)
conversion_log_button.grid(row=2, column=2, padx=5, pady=5)


#closing the program with one button
def closing():
    root.destroy()


close_button = ttk.Button(root, text="Close", command=closing)
close_button.grid(row=3, column=2, padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
