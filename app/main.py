# Author: Kristoffer Ostlund
# Website: http://kristofferostlund.com/
# Git Repo: https://github.com/kristofferostlund/sdb2_scenario
# Copyright (C) 2015 Kristoffer Ostlund. All rights reserved.

import os
from models.csvfile import CsvFile
from questions import Questions
from helpers import filepathhelper as PathHelper

def main():
    path = PathHelper.get_file_path_from_user_input()
    file = CsvFile.init_by(path)
    questions = Questions(file.coloumns)

    display_answers(questions, file)

def display_answers(questions, file):
    """Displays the answers to each question unless the file is not valid."""
    if not file.iscorrect:
        return print('\nI regret to inform you that the selected file not is of the right format.\nRun the script again and input a valid file.\nEnsure the points at a valid 3328505x.csv file where x is either a, b, or c.\nThanks for your patience.')

    print('\n---- Answers ----\n')
    print('- Answer 1: There are {} entries with a capacity between 2880.0 (units) and 3326.6 (units) (inclusive)\n'.format(questions.get_ans_1()))
    print('- Answer 2: {} of entries state is set to open.\n'.format(questions.get_ans_2()))
    print(''.join(['- Answer 3: There are {} entries which does not match the format '.format(questions.get_ans_3()), '9!99{9X}XX\n']))
    print('- Answer 4: The least common herb appears {} times.\n'.format(questions.get_ans_4()))
    print('- Answer 5: There are {} entries which has a height of at least 16 (units) and maximum 29 (units) (inclusive)\n'.format(questions.get_ans_5()))
    print('- Answer 6: There are {} entries weighing at least 7171 tonnes and maximum 10478 tones (inclusive)\n'.format(questions.get_ans_6()))
    print('- Answer 7: There are {} entries whch has a capacity of more than 683.0 (units) or less than 44 (units)\n'.format(questions.get_ans_7()))

if __name__ == '__main__':
    main()
