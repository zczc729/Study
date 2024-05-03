class Figure:

    def __init__(self, height, ch):
        self.__height = height
        self.__ch = ch
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def ch(self):
        return self.__ch

    @ch.setter
    def ch(self, value):
        self.__ch = value

    def draw(self):
        pass