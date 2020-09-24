"""
Program: regex_assignment.py
Author: Daniel Meeker
Date: 9/10/2020

This program demonstrates regex in python.
"""
import re


def multiple_replacements(dictionary, string):
    """
    Adapted from: https://stackoverflow.com/questions/15175142/how-can-i-do-multiple-substitutions-using-regex-in-python
    I used this because it is a more elegant solution than what I initially wanted to do
    which I left up in the main (commented out, of course). I don't have a full grasp on
    everything that is happening in this but I understood it enough to get it implemented.
    :param dictionary: required
    :param string: required
    :return: string
    """
    r = re.compile("(%s)" % "|".join(map(re.escape, dictionary.keys())))
    return r.sub(lambda s: dictionary[s.string[s.start():s.end()]], string)


if __name__ == '__main__':
    search_string = "I must not fear. Fear is the mind-killer. " \
                    "Fear is the little-death that brings total obliteration." \
                    " I will face my fear. I will permit it to pass over me" \
                    " and through me. And when it has gone past I will " \
                    "turn the inner eye to see its path. " \
                    "Where the fear has gone there will be nothing. " \
                    "Only I will remain.” – Frank Herbert, Dune"
    replacement_dictionary = {" I ": " You ",
                              "I ": "You ",
                              " my ": " your ",
                              " me ": " you ",
                              " me. ": " you. "}

    contains_f_list = re.findall("f", search_string, flags=re.IGNORECASE)
    print("Number of words that contain the letter 'f': " + str(len(contains_f_list)))
    begins_f_list = re.findall(" f", search_string, flags=re.IGNORECASE)
    print("Number of words that begin with the letter 'f': " + str(len(begins_f_list)))
    not_list = re.findall(" not ", search_string, flags=re.IGNORECASE)
    print("Number of times the word 'not' appears in the quote: " + str(len(not_list)))
    print(multiple_replacements(replacement_dictionary, search_string))
    # Below is my original solution which was to just keep updating the
    # string until all the replacements were made then print it out.
    # updated_string = re.sub(" I ".strip(), "You", search_string)
    # updated_string = re.sub(" my ".strip(), "your", updated_string)
    # updated_string = re.sub(" me ".strip(), "you", updated_string)
    # updated_string = re.sub(" me. ".strip(), "you.", updated_string)
    # print(updated_string)
