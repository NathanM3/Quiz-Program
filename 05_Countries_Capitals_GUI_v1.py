"""Based on 04_Get_Name_v3.py
Coding for the design of the 'Countries' and 'Capitals' GUIs.
Basing GUI off of lines 34-74 from Main Menu GUI.
This component has taken the code from Main Menu GUI and reused it due to the
button frame. Everything down from line 188 is essentially additions to the
previous version of code.
"""
# importing modules to use within program
# tkinter module used to create GUIs
from tkinter import *
from tkinter.ttk import Separator
# using re to control what characters are allowed within a string
import re
# random will be used later on in the quiz component to randomise the questions
import random
from functools import partial  # to eliminate duplicate windows


# Creating my own Errors that apply to my functions conditions
class Error(Exception):
    """Bass Class for other exceptions"""
    pass


# Is a custom Error to be raised when conditions are not met in try except
class NamingError(Error):
    """Raised when there is more than one sequential space or a string with
    less than 3 characters"""
    pass


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
                                       bg="blue", fg="snow",
                                       command=self.countries)
        self.countries_button.grid(row=0, column=0, padx=5, pady=10)

        # Capitals button (column 1) shows a button to open capitals mode
        self.capitals_button = Button(self.buttons_frame, text="Capitals",
                                      font="Arial 14 bold", width=10,
                                      bg="forest green",
                                      fg="snow", command=self.capitals)
        self.capitals_button.grid(row=0, column=1, padx=5, pady=10)

        # Separator (row 1) should produce a line inside the buttons frame
        # that separates the top 2 buttons from the bottom 2
        self.frame_separator = Separator(self.buttons_frame,
                                         orient="horizontal")
        self.frame_separator.grid(row=1, sticky="ew", columnspan=2)

        # History button (row 2, column 0) shows a button on the
        # GUI to go to history
        self.history_button = Button(self.buttons_frame,
                                     text="Answer Record History", wrap=150,
                                     font="Arial 12 bold", bg="light grey",
                                     width=12)
        self.history_button.grid(row=2, column=0, padx=5, pady=10)

        # Help Button (row 2, column 1) shows a button to open help window
        self.help_button = Button(self.buttons_frame, text="Help", width=12,
                                  font="Arial 12 bold", bg="light grey",
                                  height=2, command=self.help)
        self.help_button.grid(row=2, column=1, padx=5, pady=10)

    def name_check(self):
        valid_char = "[A-Za-z ]"
        while True:  # Loop does not end
            name = str(self.get_name_entry.get())
            try:
                for letter in name:
                    if not re.match(valid_char, letter):
                        self.get_name_label.configure(
                            text="no {}'s allowed".format(letter), fg="red")
                        raise NamingError
                if len(name) < 3 or "  " in name:
                    raise NamingError
                # If conditions are met, name will be returned
                self.get_name_label.configure(
                    text="Enjoy the quiz {}".format(name), fg="black")
                return name
            except NamingError:
                self.get_name_label.configure(
                    text="Please enter a name that contains at least 3 "
                         "letters and only 1 space between names: ", fg="red")
                break

    # functions that open pop up windows and also start using corresponding
    # classes
    def capitals(self):
        user_name = self.name_check()
        if user_name:
            get_capitals = Capitals(self)  # Opens Capitals GUI

    def countries(self):
        user_name = self.name_check()
        if user_name:
            get_countries = Countries(self)  # Opens Countries GUI

    def help(self):
        get_help = Help(self)  # Opens Help GUI


class Help:
    def __init__(self, partner):
        background = "dark orange"

        # to disable help button
        partner.help_button.config(state=DISABLED)

        # sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If a user presses the red cross at the top, it will use close_help
        # This enables the help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help,
                                                           partner))

        # set up GUI Frame
        self.help_frame = Frame(self.help_box, width=450, bg=background)
        self.help_frame.grid()
        # set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Information",
                                 font="Arial 10 bold",
                                 bg=background, pady=10)
        self.how_heading.grid(row=0)
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame,
                               text="This is a Geographical Quiz that will "
                                    "show you the name of a country or "
                                    "capital and ask you to enter the "
                                    "corresponding capital or country.\nAfter "
                                    "you have completed the quiz or decided "
                                    "to stop playing, a record of answers can "
                                    "be exported by pressing the 'Answer "
                                    "Record History' button and following the "
                                    "instructions given.\nEnjoy", justify=LEFT,
                               width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)
        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="slate gray",
                                  font="arial 10 bold",
                                  command=partial(self.close_help, partner),
                                  fg="white")

        self.dismiss_btn.grid(row=2, pady=5)

    def close_help(self, partner):
        # Enabling the help button again in the close help function
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()


class Capitals:
    def __init__(self, partner):
        background_color = "chartreuse4"

        # to disable countries and capitals buttons when quiz is open.
        partner.countries_button.config(state=DISABLED)
        partner.capitals_button.config(state=DISABLED)

        # Sets up a child window for capitals
        self.capitals_box = Toplevel()

        # Capitals GUI
        self.capitals_frame = Frame(self.capitals_box, width=375, height=300,
                                    bg=background_color)
        self.capitals_frame.grid()

        # Capitals heading (row 0)
        self.capitals_label = Label(self.capitals_frame,
                                    text="Capitals", font="Arial 18 bold",
                                    bg=background_color, padx=10, pady=10)
        self.capitals_label.grid(row=0)

        # Question label (row 1)
        self.question_label = Label(self.capitals_frame,
                                    text="<ask question here>",
                                    font="Arial 12", wrap=250, pady=10,
                                    bg=background_color)
        self.question_label.grid(row=1)

        # Answer entry box label (row 2)
        self.answer_label = Label(self.capitals_frame,
                                  text="Type your Answer and press 'Check' "
                                       "to enter", font="Arial 10 italic",
                                  bg=background_color)
        self.answer_label.grid(row=2)
        # Answer entry box (row 3)
        self.get_answer_entry = Entry(self.capitals_frame, width=17,
                                      font="Arial 12")
        self.get_answer_entry.grid(row=3)

        # Buttons Frame (row 4)
        self.buttons_frame = Frame(self.capitals_frame, pady=10, padx=10,
                                   width=200, bg=background_color)
        self.buttons_frame.grid(row=4)

        # Check button will inform the user if they were correct or incorrect
        # (row 0, column 0 of button frame)
        self.check_button = Button(self.buttons_frame, text="Check",
                                   font="Arial 14 bold", width=10,
                                   bg="sandy brown", fg="black")
        self.check_button.grid(row=0, column=0, padx=5, pady=10)

        # 'Next' button will change the GUI to the next question of the quiz
        # (row 0, column 1) on the same horizontal line as check button.
        self.next_button = Button(self.buttons_frame, text="Next",
                                  font="Arial 14 bold", width=10,
                                  bg="firebrick2", fg="snow")
        self.next_button.grid(row=0, column=1, padx=5, pady=10)


class Countries:
    def __init__(self, partner):
        background = "Green"

        # to disable countries and capitals buttons when quiz is open.
        partner.countries_button.config(state=DISABLED)
        partner.capitals_button.config(state=DISABLED)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geographical Quiz Game")
    something = Menu()
    root.mainloop()
