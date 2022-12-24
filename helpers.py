import os


def read_txt_file(txt_file):
    with open(txt_file, "r") as f:
        # Read the contents of the text file and strip any leading or trailing whitespace
        path = f.read().strip()

    return path


def greetings(first, last):
    return f'hi {first} {last}'