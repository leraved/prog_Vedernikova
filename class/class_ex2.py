class Mother:
    def year(self):
        return "Мне 35 лет"

    def print(self):
        print(self.year())
        

class Daughter(Mother):
    def year(self):
        return "А мне 10"


m = Mother()
m.print()
    
d = Daughter()
d.print()
