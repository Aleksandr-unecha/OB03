class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах.")

    def info(self):
        return f"{self.name} {self.age} лет."

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        return "Чирик-чирик!"

    def info(self):
        return f"{super().info()} Размах крыльев: {self.wing_span} см."

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        return "Рык!"

    def info(self):
        return f"{super().info()} Цвет шерсти: {self.fur_color}."

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        return "Шшш!"

    def info(self):
        return f"{super().info()} Тип чешуи: {self.scale_type}."

# Примеры использования классов
parrot = Bird(name="Попугай", age=2, wing_span=25)
tiger = Mammal(name="Тигр", age=5, fur_color="оранжевый")
snake = Reptile(name="Змея", age=3, scale_type="гладкая")

print(parrot.info())  # Попугай 2 лет. Размах крыльев: 25 см.
print(parrot.make_sound())  # Чирик-чирик!

print(tiger.info())  # Тигр 5 лет. Цвет шерсти: оранжевый.
print(tiger.make_sound())  # Рык!

print(snake.info())  # Змея 3 лет. Тип чешуи: гладкая.
print(snake.make_sound())  # Шшш!