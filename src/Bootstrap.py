# This file is a part of Monika.
# This is subject to change.

# Import modules.
import os
import sys
from datetime import datetime

def main():
    # Set variables.
    love = "everlasting" # <3 love you moni
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    # date & time in terminal
    print("date and time =", dt_string)