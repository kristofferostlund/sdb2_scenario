# Author: Kristoffer Ostlund
# Website: http://kristofferostlund.com/
# Git Repo: https://github.com/kristofferostlund/sdb2_scenario
# Copyright (C) 2015 Kristoffer Ostlund. All rights reserved.

import os
from collections import OrderedDict

class CsvFile(object):
    """Class for using easy use of Csv files. CsvFiles has the following properties:

    Attributes:
        errors: A list representing caught errors raised by the class.
        path: A string representing the filepath
        raw: A string representing the raw file content
        coloumns: An OrderedDict representing each coloumn from the raw file. Keys are the first line, and the corresponding value is a list of every other item in that row.
    """
    def __init__(self):
        """Returns the basemodel for CsvFile"""
        self.errors = []
        self.path = ''
        self.raw = ''
        self.coloumns = OrderedDict()
        self.iscorrect = False

    @classmethod
    def init_by(cls, path):
        """Returns a CsvFile object with the path of *path*,
        with raw as the contents of the file at *path*,
        from which it then populates coloumns with,
        lastly it tries to cast each coloumn to their actual types."""
        obj = cls()
        obj.errors = []
        obj.path = path
        obj.raw = obj.try_get_raw_file_content(obj.path)
        obj.coloumns = obj.create_ordered_dictionary_from(obj.raw)
        obj.coloumns = obj.try_cast_coloumns(obj.coloumns)
        obj.iscorrect = obj.check_is_correct(obj.coloumns)
        return obj

    def try_get_raw_file_content(self, path):
        """Tries to return the raw file contents of the file at *path*.
        If there is no file at *path*, an empty string is returned."""
        try:
            with open(path) as fin:
                return fin.read()
        except Exception as e:
            self.errors.append(e)
            return ''

    def get_list_by_newline_from(self, content):
        """Returns a list of every non-empty line of *content*"""
        return [line for line in content.split('\n') if len(line) > 0]

    def create_ordered_dictionary_from(self, raw):
        """"Returns an OrderedDict with the first row of each coloumn as the key, and the value is a list of every other item in that list.
        If *raw* is empty, an empty OrderedDict is returned."""
        li = self.get_list_by_newline_from(raw)
        if len(li) == 0:
            return OrderedDict()
        orDic = OrderedDict()
        # To ensure the key row is only used here, pop it
        for key in li.pop(0).split(','):
            orDic[key.strip()] = []
        for row in li:
            i = 0 # Used for accessing the coloumn of a row.
            for key in orDic:
                orDic[key].append(row.split(',')[i].strip())
                i += 1
        return orDic

    def try_cast_coloumns(self, coloumns):
        """Tries to cast each coloumn to either float or int, otherwise it will remain a string
        I.E. '2.2' will be cast to float, '2' will be cast to int, and '2{a' will stay str."""
        for key in coloumns:
            try:
                coloumns[key] = [float(x) for x in coloumns[key]] if '.' in coloumns[key][0] else [int(x) for x in coloumns[key]]
            except:
                pass

        return coloumns

    def check_is_correct(self, coloumns):
        """Checks whether file correctly formatted and returns a boolean value.
        I.E. has the following fields and at least one row with each coloumn:
        capacity, state, code, herb, height, tonnes"""
        requiredfields = [ 'capacity', 'state', 'code', 'herb', 'height', 'tonnes' ]
        if len(coloumns) < 1 or len(coloumns) != len(requiredfields):
            return False
        for field in requiredfields:
            if field not in coloumns.keys():
                return False

        return True
