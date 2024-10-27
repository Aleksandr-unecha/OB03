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
        self.wing_span = wing_span  # размах крыльев, специфический атрибут для птиц

    def make_sound(self):
        print("Птица чирикает")

# Подкласс Mammal
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color  # цвет шерсти, специфический атрибут для млекопитающих

    def make_sound(self):
        print("Млекопитающее издает звук")

# Подкласс Reptile
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type  # тип чешуи, специфический атрибут для рептилий

    def make_sound(self):
        print("Рептилия шипит")

# Создание объектов
sparrow = Bird("Воробей", 1, 25)
mammal = Mammal("Млекопитающее", 2, "Черный")
snake = Reptile("Змея", 2, "гладкая")

# Использование методов
sparrow.make_sound()  # Вывод: Птица чирикает

mammal.make_sound()  # Вывод: Млекопитающее издает звук

snake.make_sound()  # Вывод: Рептилия шипит