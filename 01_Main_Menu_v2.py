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
                                    font="Arial 10 italic",
                                    bg=background_color, pady=10)
        self.get_name_label.grid(row=1)

        # Name entry box (row 2)
        self.get_name_entry = Entry(self.main_menu_frame, width=20,
                                    font="Arial 12")
        self.get_name_entry.grid(row=2)

        # Buttons Frame
        self.buttons_frame = Frame(self.main_menu_frame, pady=10, width=20,
                                   bg=background_color)
        self.buttons_frame.grid(row=3)
        # Countries button (column 0)
        self.countries_button = Button(self.buttons_frame, text="Countries",
                                       font="Arial 14 bold", width=10,
                                       bg="blue", padx=10, pady=10, fg="snow")
        self.countries_button.grid(row=0, column=0)

        # Capitals button (column 1)
        self.capitals_button = Button(self.buttons_frame, text="Capitals",
                                      font="Arial 14 bold", width=10,
                                      bg="forest green", padx=10, pady=10,
                                      fg="snow")
        self.capitals_button.grid(row=0, column=1)

        # Separator (row 4)
        self.frame_separator = Separator(self.buttons_frame,
                                         orient="horizontal")
        self.frame_separator.grid(row=3, sticky="ew")



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geographical Quiz Game")
    something = Menu()
    root.mainloop()
