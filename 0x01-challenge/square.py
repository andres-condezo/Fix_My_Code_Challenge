#!/usr/bin/python3
""" Area of the square """


class Square():
    """ square class that define a square """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ constructor method"""
        if kwargs:
            for key, value in kwargs.items():
                if (key == 'width' or key == 'height'):
                    setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Permiter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ dictionary representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
