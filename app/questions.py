# Author: Kristoffer Ostlund
# Website: http://kristofferostlund.com/
# Git Repo: https://github.com/kristofferostlund/sdb2_scenario
# Copyright (C) 2015 Kristoffer Ostlund. All rights reserved.

from collections import OrderedDict, Counter
from .helpers import stringformathelper as SFormat

class Questions(object):
    """Class for answering questions. QuestionAnswerers has the following property:

    errors: A list representing caught errors raised by the class.
    dic: A dictionary representing the coloumns of the scenario files given.
    keys: A list representing the keys of dic"""

    def __init__(self, dic):
        """Returns the basemodel for Questions"""
        self.errors = []
        self.dic = dic
        self.keys = [key for key in self.dic] if type(dic) is dict or type(dic) is OrderedDict else []

    def get_ans_1(self):
        """Returns an integer holding the number of fields from dic['capacity'] where the value of the fields are between 2880.8 and 3326.6 (inclusive)."""
        if 'capacity' not in self.keys:
            return -1
        return len([x for x in self.dic['capacity'] if 2880.8 <= x and x <= 3326.6])

    def get_ans_2(self):
        """Returns a string holding the percentage of fields which are open in dic['state']."""
        if 'state' not in self.keys:
            return 'Not applicable'
        return '{} %'.format(len([x for x in self.dic['state'] if x == 'open']) / len(self.dic['state']) * 100)

    def get_ans_3(self):
        """Returns an integer holding the value of how many fields which aren't 9!99{9X}XX in dic['code']"""
        if 'code' not in self.keys:
            return -1
        return len([x for x in self.dic['code'] if not SFormat.matches(x,'9!99{9X}XX')])

    def get_ans_4(self):
        """Returns an integer holding the amout of times the least common string in dic['herb'] appears."""
        if 'herb' not in self.keys:
            return -1
        return Counter(self.dic['herb'])[min(Counter(self.dic['herb']), key=Counter(self.dic['herb']).get)]

    def get_ans_5(self):
        """Returns an integer holding the amount of numbers which are between 16 and 29 in dic['height'] (inclusive)"""
        if 'height' not in self.keys:
            return -1
        return len([x for x in self.dic['height'] if 16 <= x and x <= 29])

    def get_ans_6(self):
        """Returns an integer holding the sum of the numbers between 7171 and 10478 in dic['tonnes'] (inclusive)"""
        if 'tonnes' not in self.keys:
            return -1
        return sum([x for x in self.dic['tonnes'] if 7171 <= x and x <= 10478])

    def get_ans_7(self):
        """Returns an integer holding the amount of numbers where dic['height'] is less than 44 *or* dic['capacity'] is more than 683.0."""
        if 'height' not in self.keys or 'capacity' not in self.keys:
            return -1
        number = 0
        for i in range(0, len(self.dic['height'])):
            number += 1 if self.dic['height'][i] < 44 or self.dic['capacity'][i] > 683.0 else 0
        return number

    def get_list_of_answers_and_strings(self):
        arr = [ ]
        arr.append('- Answer 1: There are {} entries with a capacity between 2880.0 (units) and 3326.6 (units) (inclusive)\n'.format(self.get_ans_1()))
        arr.append('- Answer 2: {} of entries state is set to open.\n'.format(self.get_ans_2()))
        arr.append(''.join(['- Answer 3: There are {} entries which does not match the format '.format(self.get_ans_3()), '9!99{9X}XX\n']))
        arr.append('- Answer 4: The least common herb appears {} times.\n'.format(self.get_ans_4()))
        arr.append('- Answer 5: There are {} entries which has a height of at least 16 (units) and maximum 29 (units) (inclusive)\n'.format(self.get_ans_5()))
        arr.append('- Answer 6: There are {} entries weighing at least 7171 tonnes and maximum 10478 tones (inclusive)\n'.format(self.get_ans_6()))
        arr.append('- Answer 7: There are {} entries whch has a capacity of more than 683.0 (units) or less than 44 (units)\n'.format(self.get_ans_7()))
        return arr
