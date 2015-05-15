# Author: Kristoffer Ostlund
# Website: http://kristofferostlund.com/
# Git Repo: https://github.com/kristofferostlund/sdb2_scenario
# Copyright (C) 2015 Kristoffer Ostlund. All rights reserved.

"""
Note to teacher:

I chose not to make this a class, as it only would mean more code to write, and developers are inherently lazy.
Of course could I have made this a class, but then I'd either have to instatiate it wherever else I'd use it, or in this file decorate each method with @staticmethod.
"""

import os

def get_os_path(originalpath):
    """Converts and returns a Unix-style or Windows-style of writing paths to the current operating system.
    If it is a Windows system and the file is a complete path, a '\' will be inserted after the ':' to return a correct full path."""
    splitter = '/' if '/' in originalpath else '\\'
    path = os.path.join(*originalpath.split(splitter))
    # change to indexOf or whatever it is in Python
    if ':' in path:
        path = str_insert_after(path, '\\', ':')
    return path

def ensure_reletional_path(callerpath, filepath):
    """Combines and returns the relative from the path of the calling folder to the path of the file. Used to ensure a file can be run from any folder in the project."""
    return os.path.join(callerpath, get_os_path(filepath))

def get_file_path_from_user_input():
    """Takes input from the user in the form of either just the assignment letter, the assignment filename including file extension, assignment filename excluding exteinsion and the full filepath.
    Returns a clean version to the path depending on input."""

    print('Input one of the following:\n- letter for the file (a, b or c),\n- the filename (e.g. 3328505a or 3328505b.csv) or\n- the complete file path.')
    userinput = input('Letter, filename or filepath: ')

    return get_file_by(userinput)

def get_file_by(userInput):
    """Takes a string in the form of either just the assignment letter, the assignment filename including file extension, assignment filename excluding exteinsion and the full filepath.
    Returns a clean version to the path depending on input."""


    if userInput is '':
        return ''

    if userInput in [ 'a', 'b', 'c' ]:
        return combine_relational_path_and_letter(userInput)


    print(get_scenario_path_by_name(userInput))

    scenariofile = get_scenario_path_by_name(userInput)
    return scenariofile if scenariofile != '' else get_os_path(userInput)

def combine_relational_path_and_letter(letter):
    """Returns the relational path to the scenariofile of *letter* (a, b or c) or whatevr is input."""
    return ensure_reletional_path(os.path.dirname(__file__), '../../assets/3328505{}.csv'.format(letter))

def get_scenario_filepaths():
    """Finds and returns the filepahts to the scenario files from the assets folder."""
    arr = []
    for letter in [ 'a', 'b', 'c' ]:
        arr.append(combine_relational_path_and_letter(letter))
    return arr

def get_scenario_path_by_name(userinput):
    """Returns the path to the *userinput* if it is correct, otherwise it returs a blank string ('')."""
    scenariofiles = get_scenario_filepaths()
    if not userinput.endswith('.csv'):
        userinput = str_insert_after(userinput, '.csv', '.csv')
    userInputArr = [x for x in scenariofiles if x.endswith(userinput)]
    return userInputArr[0] if len(userInputArr) > 0 else ''


def str_insert_after(originalstr, addstr, findstr):
    """Inserts *addstr* to *originalstr* after *findstr* if *findstr* is in the file.
    If it's not, it appends *addstr* onto *originalstr* and returns it."""
    index = originalstr.find(findstr)
    if index == -1:
        return ''.join([originalstr, addstr])

    index += 1 # inserts are made after *findstr*
    return ''.join([originalstr[:index], addstr, originalstr[index:]])
