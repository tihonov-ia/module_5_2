class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return title


lowtower = House('ЖК Эльбрус', 10)
hightower = House('ЖК Акация', 20)
print(lowtower)
print(hightower)
print(len(lowtower))
print(len(hightower))
