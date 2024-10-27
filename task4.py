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

    def make_sound(self):
        pass  # Базовый метод, который будет переопределен в подклассах

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print("Птица чирикает")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("Млекопитающее издает звук")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print("Рептилия шипит")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name}, {self.position}"

class Zoo:
    def __init__(self):
        self.animals = []  # Список для хранения животных
        self.employees = []  # Список для хранения сотрудников

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное: {animal.get_name()}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник: {employee}")

    def show_all_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal.get_name()}")

    def show_all_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee}")

# Пример использования
zoo = Zoo()

# Создание и добавление животных
sparrow = Bird("Воробей", 1, 25)
mammal = Mammal("Млекопитающее", 2, "Черный")
snake = Reptile("Змея", 2, "гладкая")

zoo.add_animal(sparrow)
zoo.add_animal(mammal)
zoo.add_animal(snake)

# Создание и добавление сотрудников
keeper = Employee("Иван Иванов", "Уход за животными")
guide = Employee("Мария Петрова", "Экскурсовод")

zoo.add_employee(keeper)
zoo.add_employee(guide)

# Показ информации
zoo.show_all_animals()
zoo.show_all_employees()