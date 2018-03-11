import Tkinter

top = Tkinter.Tk(className="Control Bindings")

js_binds = ["Mouse", "WSAD", "ArrowKeys"]
green_r_binds = ["Enter", "MouseLeftClick", "A"]

joystick_list = Tkinter.Listbox(top, exportselection=0)
for i,item in enumerate(js_binds):
    joystick_list.insert(i, item)

green_r_list = Tkinter.Listbox(top, exportselection=0)
for i,item in enumerate(green_r_binds):
    green_r_list.insert(i, item)

def report():
    print js_binds[joystick_list.curselection()[0]]
    print green_r_binds[green_r_list.curselection()[0]]

submit = Tkinter.Button(top, text="Submit", command=report)

joystick_list.pack()
green_r_list.pack()
submit.pack()

top.mainloop()
