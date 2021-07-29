# Based on 01_Main_Menu_v2.py, this is a second method of coding for the
# separator to go in between the 4 buttons (lines 55-59)
# I also have to use 2 button frames instead of 1 (lines 38-41 and 62-65)
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
                                         "the buttons below", wrap="250",
                                    font="Arial 10 italic",
                                    bg=background_color, pady=10)
        self.get_name_label.grid(row=1)

        # Name entry box (row 2)
        self.get_name_entry = Entry(self.main_menu_frame, width=20,
                                    font="Arial 12")
        self.get_name_entry.grid(row=2)

        # Buttons Frame 1
        self.buttons_frame = Frame(self.main_menu_frame, pady=10, padx=10,
                                   width=200, bg=background_color)
        self.buttons_frame.grid(row=3)

        # Countries button (column 0) shows a button to open countries mode
        self.countries_button = Button(self.buttons_frame, text="Countries",
                                       font="Arial 14 bold", width=10,
                                       bg="blue", fg="snow")
        self.countries_button.grid(row=0, column=0, padx=10, pady=10)

        # Capitals button (column 1) shows a button to open capitals mode
        self.capitals_button = Button(self.buttons_frame, text="Capitals",
                                      font="Arial 14 bold", width=10,
                                      bg="forest green",
                                      fg="snow")
        self.capitals_button.grid(row=0, column=1, padx=10, pady=10)

        # Separator (row 4) should produce a line between the 2 buttons frames
        # that separates the top 2 buttons from the bottom 2 buttons
        self.frame_separator = Separator(self.main_menu_frame,
                                         orient="horizontal")
        self.frame_separator.grid(row=4, sticky="ew")

        # Buttons Frame 2
        self.buttons_frame_2 = Frame(self.main_menu_frame, pady=10, padx=10,
                                     width=200, bg=background_color)
        self.buttons_frame_2.grid(row=5)

        # History button (row 2, column 0) shows a button on the GUI to go to history
        self.history_button = Button(self.buttons_frame_2,
                                     text="Answer Record History", wrap=150,
                                     font="Arial 12 bold", bg="light grey",
                                     width=12)
        self.history_button.grid(row=1, column=0, padx=10, pady=10)

        # Help Button (row 2, column 1) shows a button to open help window
        self.help_button = Button(self.buttons_frame_2, text="Help", width=12,
                                  font="Arial 12 bold", bg="light grey",
                                  height=2)
        self.help_button.grid(row=1, column=1, padx=10, pady=10)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geographical Quiz Game")
    something = Menu()
    root.mainloop()
