import json

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

class Zoo:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_file(self, filename):
        data = {
            "employees": [{"type": type(e).__name__, "name": e.name} for e in self.employees]
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.employees = []
            for item in data["employees"]:
                if item["type"] == "ZooKeeper":
                    self.employees.append(ZooKeeper(item["name"]))
                elif item["type"] == "Veterinarian":
                    self.employees.append(Veterinarian(item["name"]))

# Примеры использования
zoo = Zoo()
zookeeper = ZooKeeper("Джон")
veterinarian = Veterinarian("Эмили")

zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

# Сохранение информации о зоопарке в файл
zoo.save_to_file("zoo_data.json")

# Загрузка информации о зоопарке из файла
zoo.load_from_file("zoo_data.json")

# Проверка загруженных данных
for employee in zoo.employees:
    print(employee)