"""
Program: mapping_string_length.py
Author: Daniel Meeker
Date: 9/8/20

This program demonstrates the map object in Python.
"""


def length_of_string(a_string):
    """
    This function finds the length of a string passed into it and returns a list containing the
    original string and the length of the string
    :param a_string: required
    :return: list
    """
    return [a_string, len(a_string)]


def map_length_of_string():
    """
    This function maps some of the lyrics from 'We Didn't Start The Fire' to the length_of_string function
    and creates a list of lists with each string/length_of_string
    :return: a list
    """
    list_of_strings = ["Harry Truman", "Doris Day", "Red China", "Johnnie Ray", "South Pacific",
                       "Walter Winchell", "Joe DiMaggio", "Joe McCarthy", "Richard Nixon", "Studebaker",
                       "Television", "North Korea", "South Korea", "Marilyn Monroe"]
    map_of_list = list(map(length_of_string, list_of_strings))
    return map_of_list


def length_of_each_string(a_list):
    """
    This function takes in a list and returns what is stored at the index of 1 which is its length
    :param a_list: required
    :return: an int (what is stored at index of 1 in the list)
    """
    return a_list[1]


def map_length_of_each_string():
    """
    More practice with mapping. Mapping the list craeted in the map_length_of_string function
    to the length_of_each_string function and creating a list of just the lengths of each string
    :return: a list of just the length of each string
    """
    map_lengths = list(map(length_of_each_string, map_length_of_string()))
    return map_lengths


if __name__ == '__main__':
    print(map_length_of_string())
    print(map_length_of_each_string())
