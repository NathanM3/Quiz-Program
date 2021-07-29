# Based on 01_Main_Menu_v2.py. This is the finished version of my main menu GUI
# (without commands and other small details which will be added later on.)
# changed some widths and padding values to format the GUI how I thought
# looked best (lines 50-74 button details)

from tkinter import *
import random
from tkinter.ttk import Separator


class Menu:
    def __init__(self):
        # Formatting variables of the GUI
        background_color = "#89B4E5"

        # Main Menu GUI
        self.main_menu_frame = Frame(width=375, height=300,
                                     bg=background_color)
        self.main_menu_frame.grid()

        # Main Menu heading (row 0)
        self.main_menu_label = Label(self.main_menu_frame,
                                     text="Main Menu", font="Arial 18 bold",
                                     bg=background_color, padx=10, pady=10)
        self.main_menu_label.grid(row=0)

        # Get name label (row 1)
        self.get_name_label = Label(self.main_menu_frame,
                                    text="Enter your name and press one of "
                                         "the buttons below",
                                    font="Arial 10 italic", wrap=250, pady=10,
                                    bg=background_color)
        self.get_name_label.grid(row=1)

        # Name entry box (row 2)
        self.get_name_entry = Entry(self.main_menu_frame, width=17,
                                    font="Arial 12")
        self.get_name_entry.grid(row=2)

        # Buttons Frame
        self.buttons_frame = Frame(self.main_menu_frame, pady=10, padx=10,
                                   width=200, bg=background_color)
        self.buttons_frame.grid(row=3)
        # Countries button (column 0) shows a button to open countries mode
        self.countries_button = Button(self.buttons_frame, text="Countries",
                                       font="Arial 14 bold", width=10,
                                       bg="blue", fg="snow")
        self.countries_button.grid(row=0, column=0, padx=5, pady=10)

        # Capitals button (column 1) shows a button to open capitals mode
        self.capitals_button = Button(self.buttons_frame, text="Capitals",
                                      font="Arial 14 bold", width=10,
                                      bg="forest green",
                                      fg="snow")
        self.capitals_button.grid(row=0, column=1, padx=5, pady=10)

        # Separator (row 1) should produce a line inside the buttons frame
        # that separates the top 2 buttons from the bottom 2
        self.frame_separator = Separator(self.buttons_frame,
                                         orient="horizontal")
        self.frame_separator.grid(row=1, sticky="ew", columnspan=2)

        # History button (row 2, column 0) shows a button on the GUI to go to history
        self.history_button = Button(self.buttons_frame,
                                     text="Answer Record History", wrap=150,
                                     font="Arial 12 bold", bg="light grey",
                                     width=12)
        self.history_button.grid(row=2, column=0, padx=5, pady=10)

        # Help Button (row 2, column 1) shows a button to open help window
        self.help_button = Button(self.buttons_frame, text="Help", width=12,
                                  font="Arial 12 bold", bg="light grey",
                                  height=2)
        self.help_button.grid(row=2, column=1, padx=5, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geographical Quiz Game")
    something = Menu()
    root.mainloop()
