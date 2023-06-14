#start of tkinter tutorial
import tkinter as tk
from tkinter import filedialog

def create_gui():

    # Create application window
    root = tk.Tk()


    # Set window size
    root.geometry("600x400")

    #Application title
    root.title("My Forst GUI")

    label = tk.Label(root, text="Hello World!", font=("Arial", 18))
    label.pack(padx=20, pady=20)

    # Add text box
    textbox = tk.Text(root, height=3, font=("Arial", 16))
    textbox.pack(padx=10)

    # Add button
    # button = tk.Button(root, text="Click Me!",font=("Arial", 16))
    # button.pack(padx=10, pady=10)

    # Add gridlines
    buttonframe = tk.Frame(root)
    buttonframe.columnconfigure(0, weight=1)
    buttonframe.columnconfigure(1, weight=1)
    buttonframe.columnconfigure(2, weight=1)

    btn1 = tk.Button(buttonframe, text="1", font=("Arial", 16))
    btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

    btn2 = tk.Button(buttonframe, text="2", font=("Arial", 16))
    btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

    btn3 = tk.Button(buttonframe, text="3", font=("Arial", 16))
    btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

    btn4 = tk.Button(buttonframe, text="4", font=("Arial", 16))
    btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

    btn5 = tk.Button(buttonframe, text="5", font=("Arial", 16))
    btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

    btn6 = tk.Button(buttonframe, text="6", font=("Arial", 16))
    btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

    buttonframe.pack(fill='x')



    

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    create_gui() 