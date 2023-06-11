from tkinter import *
from tkinter import ttk


def log_gui():
    log = Toplevel()
    log.title("History/Log")
    input_log = []


def temp_checker(min_value):
    error = "Please enter a number that is more\n then {}".format(min_value)
    try:
        response = float(input("Enter a number: "))

        if response < min_value:
            print(error)
        else:
            return response
    except ValueError:
        print(error)


def help_gui():
    help_screen = Toplevel()
    help_screen.title("Help")
    help_label = Label(help_screen, text="Make sure that the input is a actual number,\n"
                                         "not the lettered form of the numbers."
                                         "\n\nNo letters should be included in the input."
                                         "\n\nYou do not need to put the unit of the temperature."
                                         "\n\nclick convert to whatever you want to convert and it should convert.")
    help_label.grid(row=0, column=0)


def celsius_calc():
    output = celsius_entry.get()
    output_a = (float(output) * 9/5) + 32
    celsius_input.set(output_a)


def fahrenheit_calc():
    take_fahrenheit = fahrenheit_entry.get()
    celsius = (float(take_fahrenheit) - 32) * 5/9
    fahrenheit_input.set(celsius)



root = Tk()
root.title("Temperature convertor")
# text for the input boxes
celsius_label = ttk.Label(root, text="Celsius")
celsius_label.grid(row=0, column=0)
fahrenheit_label = ttk.Label(root, text="Fahrenheit")
fahrenheit_label.grid(row=0, column=1)


celsius_input = DoubleVar()
fahrenheit_input = DoubleVar()
celsius_input2 = DoubleVar()
fahrenheit_input2 = DoubleVar()

# user input boxes
celsius_entry = ttk.Entry(root, textvariable=celsius_input2)
celsius_entry.grid(row=1, column=0, padx=5, pady=5)
fahrenheit_entry = ttk.Entry(root, textvariable=fahrenheit_input2)
fahrenheit_entry.grid(row=1, column=1, padx=5, pady=5)


celsius_label2 = Label(root, textvariable=celsius_input)
celsius_label2.grid(row=3, column=0, padx=5, pady=5)
fahrenheit_label2 = Label(root, textvariable=fahrenheit_input)
fahrenheit_label2.grid(row=3, column=1, padx=5, pady=5)

# all the buttons
help_button = ttk.Button(root, text="Help", command=help_gui)
help_button.grid(row=1, column=2, padx=5, pady=5)

celsius_button = ttk.Button(root, text="Convert to Fahrenheit", command=celsius_calc)
celsius_button.grid(row=2, column=0, padx=5, pady=5)

fahrenheit_button = ttk.Button(root, text="Convert to Celsius", command=fahrenheit_calc())
fahrenheit_button.grid(row=2, column=1, padx=5, pady=5, sticky="WE")

conversion_log_button = ttk.Button(root, text="History", command=log_gui)
conversion_log_button.grid(row=2, column=2, padx=5, pady=5)
# closing the program with one button
close_button = ttk.Button(root, text="Close", command=root.destroy)
close_button.grid(row=3, column=2, padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
