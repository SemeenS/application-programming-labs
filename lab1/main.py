import argparse
import os
import re

def parser_() -> str:
    """
    Parses the name of file
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', type=str, help='name of your file')
        args = parser.parse_args().filename
        return args
    except:
        raise SyntaxError("path to file can't be empty")


def read_file(filename: str)-> str:
    """
    Read file and get text
    :param filename: the name of file
    :return: a string consists a data from file
    """
    if not os.path.exists(filename):
        raise FileNotFoundError('file not found')

    if not filename.endswith('.txt'):
        raise ValueError('this file is not txt file')

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        return text

def get_date(text: str)->list:
    """
    Get birthday date from data
    :param text: text that we got from file
    :return: list of birthday date
    """
    date_pattern = r'\d\d.\d\d.\d\d\d\d'
    date_list = re.findall(date_pattern, text)
    return date_list

def date_count(date_list: list) -> int:
    """
    Count the number of people who was born in the 21st century.
    :param date_list: List of birthday dates in the format 'DD.MM.YYYY'
    :return: The count of people born in the 21st century
    """
    count = 0
    for date in date_list:
        year = date[6:]
        if 2000 < int(year):
            count+=1
    return count

def main():
    filename = parser_()
    try:
        text = read_file(filename)
        date_list = get_date(text)
        print(date_count(date_list))

    except FileNotFoundError as f:
        print(f)
    except ValueError as v:
        print(v)

if __name__ == "__main__":
    main()
