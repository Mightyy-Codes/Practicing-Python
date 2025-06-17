import tkinter as tk # Import the tkinter module for GUI & tkinter shortcut as tk
window = tk.Tk() # Create a window object
window.title("GUI Calculator") # Set the title of the window
window.configure(bg="#4A148C") # Set the background purple for the window
import tkinter.font as font # Import font module for custom fonts
custom_font = font.Font(family="Helvetica", size=16, weight="bold")

entry = tk.Entry(window, width=35, borderwidth=5, font=custom_font, bg="#79659C", fg="white")
entry.grid(row=0, column= 0, columnspan=4, padx=10, pady=10) # Create an entry widget for input

def custom_button(text, command):
    return tk.Button(window, text=text, padx=20, pady=20, font=custom_font,
                     bg="#79659C", fg="black", command=command) # Function to create custom buttons

def button_click(number):  # Function to handle button clicks
    current = entry.get() # Get the current text in the entry widget
    entry.delete(0, tk.END) # Clear the entry widget
    entry.insert(0, current + str(number)) # Insert the clicked number into the entry widg
    
def button_clear(): # Function to clear the entry widget
    entry.delete(0, tk.END) # Clear the entry widget

def button_equal(): # Function to evaluate the expression in the entry widget
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
# Number of buttons
buttons = [] # Create a list to hold button objects
for i in range(10):
    buttons.append(tk.Button(window, text=str(i), padx=20, pady=20, 
                             command=lambda i=i: button_click(i)))
# Operators
button_add = custom_button("+", lambda: button_click("+"))
button_sub = custom_button("-", lambda: button_click("-"))
button_mul = custom_button("*", lambda: button_click("*"))
button_dix = custom_button("/", lambda: button_click("/"))
button_equal = custom_button("=", button_equal)
button_clear = tk.Button(window, text="Clear", padx=50, pady=20, command=button_clear)
# Arrange buttons in the grid (Layout)
buttons[1].grid(row=1, column=0)
buttons[2].grid(row=1, column=1)
buttons[3].grid(row=1, column=2)
button_add.grid(row=1, column=3)

buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)
buttons[6].grid(row=2, column=2)
button_sub.grid(row=2, column=3)

buttons[7].grid(row=3, column=0)
buttons[8].grid(row=3, column=1)
buttons[9].grid(row=3, column=2)
button_mul.grid(row=3, column=3)

buttons[0].grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_dix.grid(row=4, column=3)

button_equal.grid(row=5, column=0, columnspan=4)

# Start the main event loop)
window.mainloop() # Start the GUI event loop to keep the window open