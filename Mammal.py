class Mammal:
    def __init__(self,name:str,type:str,sound:str):
        self.__name=name
        self.__type=type
        self.__sound=sound
    def make_sound(self):
        return f'{self.__name} makes {self.__sound}'
    def get_kingdom(self):
        return f'animals'
    def info(self):
        return f'{self.__name} is of type {self.__type}'

mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
    