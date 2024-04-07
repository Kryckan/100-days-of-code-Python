import tkinter as tk
from datetime import datetime
from os import system
from platform import system as platform
from tkinter import ttk

if platform() == "Darwin":
    system(
        """/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python" to true' """
    )

root = tk.Tk()
root.geometry("1200x800")
root.title("Tkinter Widgets Demo")

# Frame
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Label
label = ttk.Label(frame, text="Label Widget", font=("Helvetica", 16))
label.pack(padx=10, pady=10)

# Button
button = ttk.Button(
    frame, text="Button Widget", command=lambda: label.configure(text="Button Clicked!")
)
button.pack(padx=10, pady=10)

# Checkbutton
check_var = tk.BooleanVar()
checkbutton = ttk.Checkbutton(frame, text="Checkbutton Widget", variable=check_var)
checkbutton.pack(padx=10, pady=10)

# Combobox
combobox = ttk.Combobox(frame, values=["Option 1", "Option 2", "Option 3"])
combobox.pack(padx=10, pady=10)

# Entry
entry = ttk.Entry(frame)
entry.pack(padx=10, pady=10)

# Labelframe
labelframe = ttk.Labelframe(frame, text="Labelframe Widget")
labelframe.pack(padx=10, pady=10, fill="both", expand=True)

# Menubutton
menubutton = ttk.Menubutton(frame, text="Menubutton Widget")
menubutton.pack(padx=10, pady=10)

# Notebook
notebook = ttk.Notebook(frame)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(padx=10, pady=10, fill="both", expand=True)

# Panedwindow
panedwindow = ttk.Panedwindow(frame, orient=tk.HORIZONTAL)
pane1 = ttk.Frame(panedwindow)
pane2 = ttk.Frame(panedwindow)
panedwindow.add(pane1)
panedwindow.add(pane2)
panedwindow.pack(padx=10, pady=10, fill="both", expand=True)

# Progressbar
progressbar = ttk.Progressbar(frame, value=50)
progressbar.pack(padx=10, pady=10)

# Radiobutton
radio_var = tk.IntVar()
radiobutton1 = ttk.Radiobutton(frame, text="Option 1", variable=radio_var, value=1)
radiobutton2 = ttk.Radiobutton(frame, text="Option 2", variable=radio_var, value=2)
radiobutton1.pack(padx=10, pady=10)
radiobutton2.pack(padx=10, pady=10)

# Scale
scale = ttk.Scale(frame, from_=0, to=100)
scale.pack(padx=10, pady=10)

# Scrollbar
scrollbar = ttk.Scrollbar(frame)
scrollbar.pack(padx=10, pady=10, side=tk.RIGHT, fill=tk.Y)

# Separator
separator = ttk.Separator(frame)
separator.pack(padx=10, pady=10, fill=tk.X)

# Sizegrip
sizegrip = ttk.Sizegrip(frame)
sizegrip.pack(padx=10, pady=10, anchor=tk.SE)

# Spinbox
spinbox = ttk.Spinbox(frame, from_=0, to=10)
spinbox.pack(padx=10, pady=10)

# Treeview
treeview = ttk.Treeview(frame)
treeview.pack(padx=10, pady=10)

# Legacy widgets (if any needed can be added here)

root.mainloop()
