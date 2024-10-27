class Employee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Сотрудник: {self.name}"

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name)

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal}.")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name)

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal}.")

# Примеры использования
zookeeper = ZooKeeper("Джон")
veterinarian = Veterinarian("Эмили")

zookeeper.feed_animal("льва")
veterinarian.heal_animal("слона")