import imp
import tkinter as tk
from turtle import window_height, window_width
from tkinter import ttk
from main import main

window =  tk.Tk()
window.title("Best Buy Price Notifier")
window_width = 800
window_height =600

"""Get the screen dimensions"""
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

"""Getting the center point of the screen"""
center_x = int(screen_width/2 - window_width / 2)
center_y = int (screen_height/2 - window_height / 2)


"""Creating the entry widget"""
text = tk.StringVar()
textbox = ttk.Entry(window, textvariable=text)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.mainloop()