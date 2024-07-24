class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number}'

    def __len__(self):
        return self.number

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number == other
        else:
            return (f'Ошибка!\n'
                    f'Вы пытаетесь сравнить {type(self.number)} и {type(other)}.')

    def __add__(self, value):
        if isinstance(value, int) or isinstance(value, House):
            self.number += value
            return self
        else:
            return (f'Ошибка!\n'
                    f'Вы пытаетесь сложить {type(self.number)} и {type(value)}.')

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number > other
        else:
            return (f'Ошибка!\n'
                    f'Вы пытаетесь сравнить {type(self.number)} и {type(other)}.')

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number >= other
        else:
            return (f'Ошибка!\n'
                    f'Вы пытаетесь сравнить {type(self.number)} и {type(other)}.')

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number < other
        else:
            return (f'Ошибка!\n'
                    f'Вы пытаетесь сравнить {type(self.number)} и {type(other)}.')

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number <= other
        else:
            return (f'Ошибка!\n'
                    f'Вы пытаетесь сравнить {type(self.number)} и {type(other)}.')

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number != other
        else:
            return (f'Ошибка!\n'
                    f'Вы пытаетесь сравнить {type(self.number)} и {type(other)}.')

    def go_to(self, new_floor):

        if not(new_floor < 1 or new_floor > self.number):
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print(f'В доме "{self.name}" этажа с номером "{new_floor}" не существует!')

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#h1.go_to(5)
#h2.go_to(10)

# __str__
print(h1)
print(h2)

# __len__
#print(len(h1))
#print(len(h2))

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__