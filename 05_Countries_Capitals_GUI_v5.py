"""Based on 05_Countries_Capitals_GUI_v4.py
This is refining the new 'quiz' class that I designed in the previous version.
This will work on taking in "countries" and "capitals" as the expression in
replacement of '1' and '2' when pressing the buttons.
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
                                    font="Arial 12", justify=CENTER)
        self.get_name_entry.grid(row=2)

        # Buttons Frame
        self.buttons_frame = Frame(self.main_menu_frame, pady=10, padx=10,
                                   width=200, bg=background_color)
        self.buttons_frame.grid(row=3)
        # Countries button (column 0) shows a button to open countries mode
        self.countries_button = Button(self.buttons_frame, text="Countries",
                                       font="Arial 14 bold", width=10,
                                       bg="blue", fg="snow",
                                       command=lambda: self.quiz("Countries"))
        self.countries_button.grid(row=0, column=0, padx=5, pady=10)

        # Capitals button (column 1) shows a button to open capitals mode
        self.capitals_button = Button(self.buttons_frame, text="Capitals",
                                      font="Arial 14 bold", width=10,
                                      bg="forest green",
                                      fg="snow", command=
                                      lambda: self.quiz("Capitals"))
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
    def quiz(self, mode):
        user_name = self.name_check()
        if user_name:
            get_quiz = Quiz(self, mode)

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


class Quiz:
    def __init__(self, partner, mode):
        #  default settings mean the quiz will be set to capitals
        # More may be added to these as the quiz is developed later on.
        background_color = "chartreuse4"  # default color for capitals
        heading_text = mode  # since mode is either "Capitals" or "Countries"
        if mode == "Countries":
            background_color = "DodgerBlue2"  # bg is changed for countries

        # to disable countries and capitals buttons when quiz is open.
        partner.countries_button.config(state=DISABLED)
        partner.capitals_button.config(state=DISABLED)

        # Sets up a child window for the quiz
        self.quiz_box = Toplevel()

        # If a user presses the red cross at the top, it will use close_quiz
        # This closes the quiz window and enables the capitals and countries
        # buttons in the main menu.
        self.quiz_box.protocol('WM_DELETE_WINDOW', partial(self.close_quiz,
                                                           partner))

        # Quiz GUI
        self.quiz_frame = Frame(self.quiz_box, width=375, height=300,
                                bg=background_color)
        self.quiz_frame.grid()

        # Heading (row 0)
        self.quiz_label = Label(self.quiz_frame,
                                text=heading_text, font="Arial 18 bold",
                                bg=background_color, padx=10, pady=10)
        self.quiz_label.grid(row=0)

        # Question label (row 1)
        self.question_label = Label(self.quiz_frame,
                                    text="<ask question here>",
                                    font="Arial 12", wrap=250, pady=10,
                                    bg=background_color)
        self.question_label.grid(row=1)

        # Answer entry box label (row 2)
        self.answer_label = Label(self.quiz_frame,
                                  text="Type your Answer and press 'Check' "
                                       "to enter", font="Arial 10 italic",
                                  bg=background_color)
        self.answer_label.grid(row=2, padx=30)
        # Answer entry box (row 3)
        self.get_answer_entry = Entry(self.quiz_frame, width=17,
                                      font="Arial 12", justify=CENTER)
        self.get_answer_entry.grid(row=3)

        # Buttons Frame (row 4)
        self.buttons_frame = Frame(self.quiz_frame, pady=10, padx=10,
                                   width=200, bg=background_color)
        self.buttons_frame.grid(row=4)

        # Check button will inform the user if they were correct or incorrect
        # (row 0, column 0 of button frame)
        self.check_button = Button(self.buttons_frame, text="Check",
                                   font="Arial 14 bold", width=8,
                                   bg="sandy brown", fg="black")
        self.check_button.grid(row=0, column=0, padx=5, pady=10)

        # 'Next' button will change the GUI to the next question of the quiz
        # (row 0, column 1) on the same horizontal line as check button.
        self.next_button = Button(self.buttons_frame, text="Next",
                                  font="Arial 14 bold", width=8,
                                  bg="firebrick2", fg="snow")
        self.next_button.grid(row=0, column=1, padx=5, pady=10)

    def close_quiz(self, partner):
        # Enabling the help button again in the close help function
        partner.capitals_button.config(state=NORMAL)
        partner.countries_button.config(state=NORMAL)
        self.quiz_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geographical Quiz Game")
    something = Menu()
    root.mainloop()
