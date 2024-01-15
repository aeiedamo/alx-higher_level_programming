#!/usr/bin/python3
"""creating a Class base"""
import json
import unittest


class Base:
    """The goal of it is to manage id attribute in all your future
    classes and to avoid duplicating the same code (by extension, same bugs)"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer for Base Class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [el.to_dictionary() for el in list_objs]
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        import os.path

        filename = "{}.json".format(cls.__name__)
        if not os.path.isfile(filename):
            return []
        with open(filename, "r") as f:
            return [cls.create(**el) for el in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves Rectangles/Squares to csv"""
        from models.rectangle import Rectangle
        from models.square import Square
        import csv

        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[el.id, el.width, el.x, el.y] for el in list_objs]
            elif cls is Square:
                list_objs = [[el.id, el.size, el.x, el.y] for el in list_objs]
        with open(
            "{}.csv".format(cls.__name__),
            "w",
            newline="",
        ) as f:
            writer = csv.writer(f)
            writer.writerow(list_objs)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        import turtle
        import time

        for i in list_rectangles + list_squares:
            el = turtle.Turtle()
            el.color("#800020")
            el.pensize(10)
            for j in range(2):
                el.hideturtle()
                el.forward(i.width)
                el.right(90)
                el.forward(i.height)
                el.right(90)
            el.reset()
            time.sleep(2)
