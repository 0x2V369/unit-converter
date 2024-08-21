from tkinter import *

conversion_factors = {
    'km -> miles': 1 / 1.609,
    'miles -> km': 1.609
}


def unit_conversion_choice(event):
    """Handles the change of labels based on the user's conversion choice."""
    choice = get_unit_conversion()
    if choice == 'km -> miles':
        label1.config(text="km")
        label4.config(text='miles')
    elif choice == 'miles -> km':
        label1.config(text='miles')
        label4.config(text="km")


def get_unit_conversion():
    """Returns the selected conversion type."""
    if not listbox.curselection():
        return None
    return listbox.get(listbox.curselection())


def unit_conversion():
    """Performs the unit conversion based on user input."""
    try:
        num = float(user_input.get())
        conversion = get_unit_conversion()

        # if conversion not selected print "Select..."
        if not conversion:
            label3.config(text="Select a conversion type")
            return

        factor = conversion_factors[conversion]
        result = num * factor
        label3.config(text=f"{result:.4f}")

    except ValueError:
        label3.config(text="Invalid input")


# Create the main window
window = Tk()
window.title("Unit Converter")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# Label for unit conversion
text_1 = Label(text="Choose unit conversion")
text_1.grid(column=1, row=0, pady=10)

# Box of choices for unit conversion
listbox = Listbox(height=4)
units = ['km -> miles', 'miles -> km']
for unit in units:
    listbox.insert(END, unit)
listbox.grid(column=1, row=1, padx=10, pady=10)
listbox.bind("<<ListboxSelect>>", unit_conversion_choice)

# User input (entry)
user_input = Entry(width=10)
user_input.grid(column=3, row=3, padx=5)

# Units from label
label1 = Label(text='')
label1.grid(column=4, row=3, padx=5)

# "is equal to" label
label2 = Label(text="is equal to")
label2.grid(column=2, row=4, padx=5)

# Converted Unit
label3 = Label(text="")
label3.grid(column=3, row=4, padx=5)

# Unit to
label4 = Label(text="Unit To")
label4.grid(column=4, row=4, padx=5)

# "Convert" button
button = Button(text="Convert", command=unit_conversion)
button.grid(column=3, row=5, pady=10)

window.mainloop()
