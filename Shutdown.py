import tkinter as tk
import os
from tkinter import messagebox, ttk

# Create the main window and configure
root = tk.Tk()
root.title("Shutdown Timer")
root.geometry("295x70")
root.configure(bg="#424854")
root.iconphoto(True, tk.PhotoImage(file='shutdown.png'))

# Define the color that will be set as background color in widgets
carbon_gray = "#737985"

# Define the list of values used for converting time formats
time_formats = {
  "Hours": 3600,
  "Minutes": 60,
  "Seconds": 1
}

# Define functions that will be called when buttons are pressed -------------------------------------

def shutdown():
  time_format = drop.get() # Get the value from the dropdown menu

  if entry.get().isdigit(): # Check if the value entered in the entry widget is a valid integer
    delay = int(entry.get()) # Get the value from the entry widget, convert it to int and store it in a variable
    os.system(f"shutdown /s /t {delay * time_formats.get(time_format)}")
    root.destroy() # Close application
  else:
    messagebox.showerror(title='Error', message='Please enter a valid integer value for the timer.')

def undo_shutdown():
  os.system("shutdown /a")
  root.destroy()

# ---------------------------------------------------------------------------------------------------

# Create a label and an entry widget
label = tk.Label(root, text="Enter delay:", font=("Arial", 12), bg="#424854")
entry = tk.Entry(root, font=("Arial", 10), bg=carbon_gray, width=7)
entry.focus() # Set focus on the entry widget

# Create Dropdown menu
style = ttk.Style(root)
drop = ttk.Combobox(root, style="TCombobox", values=("Hours", "Minutes", "Seconds"))
drop.current(0)
drop['state'] = 'readonly'

# Create button widgets
shutdown_button = tk.Button(root, text="ShutDown", command=shutdown, font=("Arial", 10), bg=carbon_gray)
undo_shutdown_button = tk.Button(root, text="Undo ShutDown", command=undo_shutdown, font=("Arial", 10), bg=carbon_gray)

# Place the widgets in the window using grid layout
label.grid(row=0, column=0, padx=1, pady=5)
entry.grid(row=0, column=1, padx=1, pady=5)
drop.grid(row=0, column=3, padx=1, pady=5)
shutdown_button.grid(row=1, column=0, padx=0, pady=5)
undo_shutdown_button.grid(row=1, column=3, padx=0, pady=5)

# Run the main loop
root.mainloop()