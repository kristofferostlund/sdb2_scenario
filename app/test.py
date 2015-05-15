# Author: Kristoffer Ostlund
# Website: http://kristofferostlund.com/
# Git Repo: https://github.com/kristofferostlund/sdb2_scenario
# Copyright (C) 2015 Kristoffer Ostlund. All rights reserved.

import unittest

from helpers import stringformathelper as SFormat

class TestStringFormatHelper(unittest.TestCase):

    def setUp(self):
        pass

    def test_match_not_same_lengt(self):
        self.assertFalse(SFormat.matches('abc', 'abcabc'), 'Strings of different lengths should not match')

    def test_match_same_length(self):
        self.assertTrue(SFormat.matches('abc', 'abc'), 'Strings of same lengths should match')

    def test_match_not_letter_num(self):
        self.assertFalse(SFormat.matches('a', '1'), 'Letters and numbers should not match')

    def test_match_letters(self):
        self.assertTrue(SFormat.matches('a', 'q'), 'Letters should match')

    def test_match_not_letter_chars(self):
        self.assertFalse(SFormat.matches('a', '!'), 'Letters and symbols should not match')

    def test_match_nums(self):
        self.assertTrue(SFormat.matches('1', '6'), 'Numbers should match')

    def test_match_chars(self):
        self.assertTrue(SFormat.matches('!', '#'), 'Carahcters should match')

    def test_match_not_same_curlybracket(self):
        self.assertFalse(SFormat.matches('{', '}'), 'Mismatching curly brackets should not match')

    def test_match_same_curlybracket(self):
        self.assertTrue(SFormat.matches('{', '{'), 'Curly brackets should be the same')

    def test_match_not_curlybracket_char(self):
        self.assertFalse(SFormat.matches('{', '!'), 'Curly brackets and characters should not match')

    def test_match_equal_string(self):
        string_abc = 'kyfi86tliugasd876asd'
        self.assertTrue(SFormat.matches(string_abc, string_abc), 'String matches itself')

    def test_match_different_strings(self):
        self.assertTrue(SFormat.matches('abc123{!aa', 'oye868{#iu'), 'Different strings matches formatically')

unittest.main()
