from tkinter import *
from tkinter import ttk


def clear_history(list_boxes):
    list_boxes.delete(0, END)
    output_log.clear()

def txt():
    file = open('items.txt', 'w')
    for item in output_log:
        file.write(item+"\n")
    file.close()

def log_gui():
    take_answers = float(fahrenheit_input.get())
    take_answer = float(celsius_input.get())
    take_entry1 = float(celsius_entry.get())
    take_entry2 = float(fahrenheit_entry.get())
    format_temp = "{:.2f}°F to {:.2f}°C".format(take_entry2, take_answers)
    if format_temp not in output_log:
        output_log.append(format_temp)

    format_temps = "{:.2f}°C to {:.2f}°F".format(take_entry1, take_answer)
    if format_temps not in output_log:
        output_log.append(format_temps)

    log = Toplevel()
    log.title("History/Log")
    input_log.append(take_answer)
    input_log.append(take_answers)
    print(input_log)
    list_boxes = Listbox(log)
    list_boxes.insert(0, *output_log)
    clear_button = ttk.Button(log, text="Clear", command=lambda: clear_history(list_boxes))
    clear_button.grid(column=1, row=0, padx=5, pady=5)
    list_boxes.grid(column=0, row=0, padx=5, pady=5)
    file_button = ttk.Button(log, text="Turn into TXT", command=txt)
    file_button.grid(column=1, row=1, padx=5, pady=5)


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
    try:
        output = celsius_entry.get()
        output_a = (float(output) * 9 / 5) + 32
        celsius_input.set(str(output_a))
    except ValueError:
        print_error = "Input a Number"
        celsius_input.set(print_error)


def fahrenheit_calc():
    try:
        take_fahrenheit = fahrenheit_entry.get()
        celsius = (float(take_fahrenheit) - 32) * 5 / 9
        fahrenheit_input.set(str(celsius))
    except ValueError:
        print_error = "Input a Number"
        fahrenheit_input.set(print_error)


root = Tk()
root.title("Temperature convertor")
input_log = []
output_log = []
# text for the input boxes
celsius_label = ttk.Label(root, text="Celsius")
celsius_label.grid(row=0, column=0)
fahrenheit_label = ttk.Label(root, text="Fahrenheit")
fahrenheit_label.grid(row=0, column=1)

celsius_input = StringVar()
fahrenheit_input = StringVar()
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
help_button.grid(row=4, column=0, padx=5, pady=5)

celsius_button = ttk.Button(root, text="Convert to Fahrenheit", command=celsius_calc)
celsius_button.grid(row=2, column=0, padx=5, pady=5)

fahrenheit_button = ttk.Button(root, text="Convert to Celsius", command=fahrenheit_calc)
fahrenheit_button.grid(row=2, column=1, padx=5, pady=5, sticky="WE")

conversion_log_button = ttk.Button(root, text="History", command=log_gui)
conversion_log_button.grid(row=4, column=1, padx=5, pady=5)
# closing the program with one button
close_button = ttk.Button(root, text="Close", command=root.destroy)
close_button.grid(row=4, column=2, padx=5, pady=5)

root.resizable(False, False)
root.mainloop()
