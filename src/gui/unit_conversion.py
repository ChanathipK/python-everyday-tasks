from tkinter import *
from tkinter import ttk

# tkdocs -> tutorials -> example

def tk_main():

    def calculate(meter, values):
        print(meter, type(meter))
        try:
            values[0].set(round(meter * 100, 4))
            values[1].set(round((meter * 100) / 2.54, 4))
            values[2].set(round((meter * 100) / 30.48, 4))
            values[3].set(round(meter / 1000, 4))
            values[4].set(round(meter / 1609.34, 4))
        except Exception:
            pass


    root = Tk()
    mainframe = ttk.Frame(root, padding="5 5 12 12")
    mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
    
    ttk.Label(mainframe, text="Unit Conversion").grid(column=2, row=1, sticky=(W, E))

    meter = StringVar()
    meter_entry = ttk.Entry(mainframe, textvariable=meter, width=12)
    meter_entry.grid(column=2, row=2, sticky=(W, E))
    ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

    # label, "is equal to", unit, value
    units = ["cm", "inch", "feet", "km", "mile"]
    values = (StringVar(), StringVar(), StringVar(), StringVar(), StringVar())
    for i in range(5):
        ttk.Label(mainframe, text="is equal to").grid(column=1, row=i+3, sticky=E)
        ttk.Label(mainframe, text=units[i]).grid(column=3, row=i+3, sticky=W)
        ttk.Label(mainframe, textvariable=values[i]).grid(column=2, row=i+3, sticky=(W, E))

    for child in mainframe.winfo_children():
        child.grid_configure(padx=8, pady=4)
    
    root.bind("<Return>", lambda e: calculate(float(meter.get()), values))
    meter_entry.focus()
    root.mainloop()
