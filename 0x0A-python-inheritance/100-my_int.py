#!/usr/bin/python3
"""MyInt class that inherits from int"""


class MyInt(int):
    """MyInt is class that inherits from int"""

    def __init__(self, my_int) -> None:
        self.__my_int = my_int

    @property
    def my_int(self):
        """retrieve an object"""
        return self.__my_int

    @my_int.setter
    def my_int(self, my_int):
        if isinstance(my_int, int):
            raise TypeError("my_int should be an integer")
        self.__my_int = my_int

    def __eq__(self, value) -> bool:
        """method to invert == sign"""
        if self.__my_int == value:
            return False
        else:
            return True

    def __ne__(self, __value: object) -> bool:
        """method to invert != sign"""
        if self.__my_int != __value:
            return False
        else:
            return True
