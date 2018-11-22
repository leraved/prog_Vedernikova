class Animal:
    def print_name(self):
        print(self.name())

    def print_age(self):
        print(self.age())

    def name():
        return "Name"

    def age():
        return "Age"


class Zebra(Animal):
    def name(self):
        return "Zebra"

    def age(self):
        return "10"


class Dolphin(Animal):
    def name(self):
        return "Dolphin"

    def age(self):
        return "15"


z = Zebra()
z.print_name()
z.print_age()

d = Dolphin()
d.print_name()
d.print_age()




    
