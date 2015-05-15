# Author: Kristoffer Ostlund
# Website: http://kristofferostlund.com/
# Git Repo: https://github.com/kristofferostlund/sdb2_scenario
# Copyright (C) 2015 Kristoffer Ostlund. All rights reserved.

# import standard libraries
import os
from tkinter import *
from tkinter import filedialog
import tkinter.font as tkfont

# import my own files

from .models.csvfile import CsvFile
from .questions import Questions
from .helpers import filepathhelper as PathHelper

class App:
    """The GUI for this application.
    This handles the main loop of the program."""
    def __init__(self, parent):

        # --- none GUI specific init ---

        self.file = None # Left empty on init
        self.path = '' # Left empty on init
        self.questions = None # Left empty on init

        # --- end none GUI specific inits ----

        # --- constants ----

        self.color_bg = '#f2f2f2'
        self.color_fg = '#242424'
        self.color_white = '#fafafa'
        self.color_green = '#66998d'

        self.font_family = 'Helvetica'
        self.font = tkfont.Font(family=self.font_family, size=8, weight='normal')

        self.str_origin = 'Input one of the following:\n- letter for the file (a, b or c),\n- the filename (e.g. 3328505a or 3328505b.csv) or\n- the complete file path.'

        self.geometry = '640x400'

        # ---- end constants ----

        # ---- widgets ----

        # Set parent or master
        self.parent = parent
        self.parent.geometry(self.geometry)

        # Set the container for the widgets
        self.container = Frame(
            self.parent,
            background=self.color_bg
            )
        self.container.pack(side=TOP, expand=YES, fill=BOTH)

        # Set the label displaying the result
        self.result = Label(
            self.container,
            font=self.font,
            foreground=self.color_white,
            background=self.color_green,
            text=self.str_origin,
            justify=LEFT
            )
        self.result.pack(
            side=TOP,
            anchor=E,
            expand=YES,
            fill=BOTH,
            ipadx=5,
            ipady=5
            )

        # Set the input and its events
        self.input = Entry(
            self.container,
            font=self.font,
            background=self.color_white,
            foreground=self.color_fg
        )
        self.input.bind('<Return>', self.get_input_handler)
        self.input.focus_force()
        self.input.pack(
            side=LEFT,
            anchor=S,
            expand=YES,
            fill=X,
            padx=5,
            pady=5,
            ipady=3
            )

        # Set the OK button and its events
        self.ok_button = Button(
            self.container,
            font=self.font,
            background=self.color_white,
            text='OK'
        )
        self.ok_button.bind('<ButtonRelease-1>', self.get_input_handler)
        self.ok_button.pack(
            side=RIGHT,
            anchor=S,
            expand=NO,
            fill=NONE,
            padx=5,
            pady=5,
            ipadx=10
            )

        # Set the browse button and its events
        self.browse_button = Button(
            self.container,
            font=self.font,
            background=self.color_white,
            text='...'
        )
        self.browse_button.bind('<ButtonRelease-1>', self.open_file_handler)
        self.browse_button.pack(
            side=RIGHT,
            anchor=S,
            expand=NO,
            fill=NONE,
            padx=5,
            pady=5,
            ipadx=10
            )

        # ---- end widgets ----

    # --- event handlers ----

    def get_input_handler(self, event):
        """Reads the input from self.input and sends it off to the self.display_anwsers method."""
        self.path = PathHelper.get_file_by(self.input.get())
        self.display_answers(self.path)

    def open_file_handler(self, event):
        """Opens a filedialog and passing the result to self.display_answers if there's a chosen filename in the picker.
        """
        filetypes = [('CSV files' , '*.csv'), ('All files', '*')]
        path = filedialog.askopenfilename()
        self.path = path if (path != None and path != '') else self.path
        if (path != None and path != ''):
            self.input.delete(0, END)
            self.input.insert(0, self.path)
            self.display_answers(self.path)

    def display_answers(self, filename):
        """Displays the answers.
        Sets self.path to the filepath (either by letter of file, filename or full filepath).
        If one is given, it proceeds to answer the questions, otherwise the program will complain."""
        self.path = PathHelper.get_file_by(filename)
        self.file = CsvFile.init_by(self.path)
        if filename is '':
            res = 'Sorry, your must input a value. \n{}'.format(self.str_origin)
        elif self.file.iscorrect:
            self.questions = Questions(self.file.coloumns)
            res = '\n'.join(self.questions.get_list_of_answers_and_strings())
        else:
            res = 'Sorry, a valid file could not be found at {} \n{}'.format(self.file.path, self.str_origin)

        self.result.config(text = res)

def main():
    """The program's main loop"""
    root = Tk()
    app = App(root)
    root.mainloop()
