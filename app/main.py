# Author: Kristoffer Ostlund
# Website: http://kristofferostlund.com/
# Git Repo: https://github.com/kristofferostlund/sdb2_scenario
# Copyright (C) 2015 Kristoffer Ostlund. All rights reserved.

import os
from models.csvfile import CsvFile
from questions import Questions
from helpers import filehelper as FileHelper

def main():
    for letter in ['a', 'b', 'c']:
        path = FileHelper.ensure_reletional_path(os.path.dirname(__file__), '../assets/3328505{}.csv'.format(letter))
        print('\n{}'.format(path))
        file = CsvFile.init_by(path)
        questions = Questions(file.coloumns)
        print('First question: {}'.format(questions.get_ans_1()))
        print('Second question: {}'.format(questions.get_ans_2()))
        print('Third question: {}'.format(questions.get_ans_3()))
        print('Fourth question: {}'.format(questions.get_ans_4()))
        print('Fifth question: {}'.format(questions.get_ans_5()))
        print('Sixth question: {}'.format(questions.get_ans_6()))
        print('Seventh question: {}'.format(questions.get_ans_7()))

if __name__ == '__main__':
    main()
