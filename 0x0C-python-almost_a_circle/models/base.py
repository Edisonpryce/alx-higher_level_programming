class Base:
    """Base model.

    This Represent the "base" for all other classes in this project(0x0C)

    Private Class Attributes:
        __nb_objects (int): Represents number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
