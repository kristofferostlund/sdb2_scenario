# Author: Kristoffer Ostlund
# Website: http://kristofferostlund.com/
# Git Repo: https://github.com/kristofferostlund/sdb2_scenario
# Copyright (C) 2015 Kristoffer Ostlund. All rights reserved.

import os

def get_os_path(originalPath):
    """Converts and returns a Unix-style or Windows-style of writing paths to the current operating system."""
    splitter = '/' if '/' in originalPath else '\\'
    return os.path.join(*originalPath.split(splitter))

def ensure_reletional_path(callerPath, filePath):
    """Combines and returns the relative from the path of the calling folder to the path of the file. Used to ensure a file can be run from any folder in the project."""
    return os.path.join(callerPath, get_os_path(filePath))
