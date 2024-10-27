class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

# Подкласс Bird
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print("Птица чирикает")

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Млекопитающее издает звук")

# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print("Рептилия шипит")

# Функция демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Создание объектов
sparrow = Bird("Воробей", 1, 25)
mammal = Mammal("Млекопитающее", 2, "Черный")
snake = Reptile("Змея", 2, "гладкая")

# Список животных
animals = [sparrow, mammal, snake]

# Вызов функции для каждого животного в списке
animal_sound(animals)