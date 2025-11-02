import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()
root.title("My First App")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()