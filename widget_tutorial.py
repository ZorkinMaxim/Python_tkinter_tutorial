from tkinter import *
from tkinter import ttk


def set_entry(*args):
    entry_1_txt.set("Hello")


def chk_but_changed(*args):
    entry_1_txt.set(chk_but_1_txt.get())


def radio_changed(*args):
    entry_1_txt.set(radio_but_1_val.get())


def combo_changed(*args):
    entry_1_txt.set(combo_1_val.get())


root = Tk()
root.title("Widget Example")
frame = ttk.Frame(root, padding="10 10 10 10")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

lable_1_txt = StringVar()
lable_1 = ttk.Label(frame, text="Data :")
lable_1.grid(column=1, row=1, sticky=(W, E))

lable_1['textvariable'] = lable_1_txt
lable_1_txt.set("Data")

entry_1_txt = StringVar()
entry_1 = ttk.Entry(frame, width=7, textvariable=entry_1_txt)
entry_1.grid(column=2, row=1, sticky=(W, E))
entry_1_txt.set(lable_1_txt.get())

button_1 = ttk.Button(frame, text="Click", command=set_entry)
button_1.grid(column=3, row=1, sticky=(W, E))

button_1['state'] = 'disabled'  # To disable the button
button_1['state'] = 'enable'  # To enable the button

chk_but_1_txt = StringVar()
chk_but_1 = ttk.Checkbutton(frame, text='Feeling', command=chk_but_changed, variable=chk_but_1_txt, onvalue='Happy',
                            offvalue='Sad')
chk_but_1.grid(column=4, row=1, sticky=(W, E))

radio_but_1_val = StringVar()
red_r_but = ttk.Radiobutton(frame, text='Red', variable=radio_but_1_val, value='Red', command=radio_changed)
blue_r_but = ttk.Radiobutton(frame, text='Blue', variable=radio_but_1_val, value='Blue', command=radio_changed)
green_r_but = ttk.Radiobutton(frame, text='Green', variable=radio_but_1_val, value='Green', command=radio_changed)
red_r_but.grid(column=2, row=2, sticky=(W, E))
blue_r_but.grid(column=3, row=2, sticky=(W, E))
green_r_but.grid(column=4, row=2, sticky=(W, E))
lable_2 = ttk.Label(frame, text='Fav Color')
lable_2.grid(column=1, row=2, sticky=(W, E))

combo_1_val = StringVar()
combo_1 = ttk.Combobox(frame, textvariable=combo_1_val)
lable_3 = ttk.Label(frame, text='Size')
lable_3.grid(column=1, row=3, sticky=(W, E))
combo_1['values'] = ('Small', 'Medium', 'Large')
combo_1.grid(column=2, row=3, sticky=(W, E))
combo_1.bind('<<ComboboxSelected>>', combo_changed)

root.mainloop()
