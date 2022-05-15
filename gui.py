import email
import tkinter as tk
from turtle import window_height, window_width
from tkinter import ttk
from getter import Getter


g = Getter()

"""Test action"""
def test():
    print("howdy")

"""Action here used for when enter to activate the getProductData"""
def enterAction(text):
    g.getProductData()




# window =  tk.Tk()
# window.title("Best Buy Price Notifier")
# window_width = 400
# window_height = 300

# """Get the screen dimensions"""
# screen_width = window.winfo_screenwidth()
# screen_height = window.winfo_screenheight()

# """Getting the center point of the screen"""
# center_x = int(screen_width/2 - window_width / 2)
# center_y = int (screen_height/2 - window_height / 2)

# """Create a frame"""
# topFrame = ttk.Frame(window)
# topFrame.columnconfigure(0, weight = 1)
# topFrame.columnconfigure(1, weight = 3)

# topFrame.pack()

# """Creating the entry widget"""
# text = tk.StringVar()
# textbox = ttk.Entry(topFrame, textvariable=text)
# textbox.grid(column=1, row=1, sticky=tk.W)

# """Creating a button to enter"""
# enterButton = ttk.Button(topFrame, text='Enter', command=enterAction(textbox))
# enterButton.grid(column=0, row=1, padx=10, pady= 10)

# """Creating an entry for the email"""
# emailText = tk.StringVar()
# emailBox = ttk.Entry(topFrame, textvariable=emailText)
# emailBox.grid(column=1, row=2, sticky=tk.W)

# """Button for configuring email"""
# emailButton = ttk.Button(topFrame, text="Email", command=test)
# emailButton.grid(column=0, row = 2, padx=10, pady= 10)

# """Creating a button to exit."""
# exitButton = ttk.Button(window, text='Exit', command=lambda: window.quit() )
# exitButton.pack()


# window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# window.mainloop()


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Best Buy Price Notifier")
        window_width = 400
        window_height = 300

        """Get the screen dimensions"""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        """Getting the center point of the screen"""
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int (screen_height/2 - window_height / 2)

        """Create a frame"""
        topFrame = ttk.Frame(self)
        topFrame.columnconfigure(0, weight = 1)
        topFrame.columnconfigure(1, weight = 3)

        topFrame.pack()

        """Creating the entry widget"""
        text = tk.StringVar()
        textbox = ttk.Entry(topFrame, textvariable=text)
        textbox.grid(column=1, row=1, sticky=tk.W)

        """Creating a button to enter"""
        enterButton = ttk.Button(topFrame, text='Enter', command=enterAction(textbox))
        enterButton.grid(column=0, row=1, padx=10, pady= 10)

        """Creating an entry for the email"""
        emailText = tk.StringVar()
        emailBox = ttk.Entry(topFrame, textvariable=emailText)
        emailBox.grid(column=1, row=2, sticky=tk.W)

        """Button for configuring email"""
        emailButton = ttk.Button(topFrame, text="Email", command=test)
        emailButton.grid(column=0, row = 2, padx=10, pady= 10)

        """Creating a button to exit."""
        exitButton = ttk.Button(self, text='Exit', command=lambda: self.quit() )
        exitButton.pack()