
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color

# creating a subclass of the superclass, Plant

class Flower(Plant):
    def __init__(self,color, petals):

        # the init method of the subclass calls the init method from the superclass FIRST
        # the attributes of the subclass cannot be set until the attributes of the superclass are set
        Plant.__init__(self,color)
        self.__petals = petals

    def get_petals(self):
        return self.__petals
    
