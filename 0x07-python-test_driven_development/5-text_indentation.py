#!/usr/bin/python3
"""
text_indentation: Write a function that prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: text to process
    Returns:
        Nothing
    Raises:
        TypeError: exception with the message text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimit = ".?:"
    for item in delimit:
        text = (item + "\n\n").join([line.strip(" ") for line in text.split(item)])

    print(text, end="")
