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

# Пример подклассов, наследующих от Animal:
class Dog(Animal):
    def make_sound(self):
        print("Собака говорит гав")

class Cat(Animal):
    def make_sound(self):
        print("Кошка говорит мяу")

# Создание объектов Dog и Cat:
dog = Dog("Рекс", 3)
cat = Cat("Мурка", 2)

# Использование методов:
dog.make_sound()  # Вывод: Собака говорит гав
cat.make_sound()  # Вывод: Кошка говорит мяу