import email
import tkinter as tk
from turtle import window_height, window_width
from tkinter import ttk
from main import main


def test():
    print("howdy")




window =  tk.Tk()
window.title("Best Buy Price Notifier")
window_width = 800
window_height = 600

"""Get the screen dimensions"""
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

"""Getting the center point of the screen"""
center_x = int(screen_width/2 - window_width / 2)
center_y = int (screen_height/2 - window_height / 2)

"""Create a frame"""
topFrame = ttk.Frame(window)
topFrame.columnconfigure(0, weight = 1)
topFrame.columnconfigure(1, weight = 3)

topFrame.pack()

"""Creating the entry widget"""
text = tk.StringVar()
textbox = ttk.Entry(topFrame, textvariable=text)
textbox.grid(column=1, row=1, sticky=tk.W)

"""Creating a button to enter"""
enterButton = ttk.Button(topFrame, text='Enter', command=test)
enterButton.grid(column=0, row=1, padx=10, pady= 10)

"""Button for configuring email"""
emailButton = ttk.Button(topFrame, text="Email", command=test)
emailButton.grid(column=0, row = 2, padx=10, pady= 10)

"""Creating a button to exit."""
exitButton = ttk.Button(window, text='Exit', command=lambda: window.quit() )
exitButton.pack()


window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.mainloop()