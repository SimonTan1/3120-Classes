class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)

    def talk(self):
        print("hi")

    def gender(self,gen):
        self.gender = gen
        print("gender is", self.gender)

    def diet(self, food):
        self.diet = food
        print("animal eats", self.diet)
