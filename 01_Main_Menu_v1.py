# First version of Main Menu GUI shows everything up to the first two buttons
# I was still working out how to place the buttons where I wanted
# I used a button frame to do this in the second version
from tkinter import *
import random


class Menu:
    def __init__(self):
        print("hello world")

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
                                    font="Arial 10 italic",
                                    bg=background_color, pady=10)
        self.get_name_label.grid(row=1)

        # Name entry box (row 2)
        self.get_name_entry = Entry(self.main_menu_frame, width=20,
                                    font="Arial 12")
        self.get_name_entry.grid(row=2)

        # Countries button (row 3, column 0)
        self.countries_button = Button(self.main_menu_frame, text="Countries",
                                       font="Arial 14 bold", width=10,
                                       bg="blue", padx=10, pady=10, fg="snow")
        self.countries_button.grid(column=0)

        # Capitals button (column 1, row 3)
        self.capitals_button = Button(self.main_menu_frame, text="Capitals",
                                      font="Arial 14 bold", width=10,
                                      bg="forest green", padx=10, pady=10,
                                      fg="snow")
        self.capitals_button.grid(column=1)

        # Separator


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geographical Quiz Game")
    something = Menu()
    root.mainloop()
