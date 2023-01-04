# Esimerkki: periyttäminen

class Animal:
    def __init__(self, species="Kala", color="harmaa", sleep=False):
        self._species = species
        self._color = color
        self._sleep = sleep

    def sleep(self, sleep=None):
        if sleep is not None:
            self._sleep = sleep
        return self._sleep

    def move(self):
        if not self._sleep:
            return f"{self._species} liikkuu"
        else:
            return f"{self._species} nukkuu eikä voi liikkua"


class Lion(Animal):
    def __init__(self, subspecies=None, species="Leijona", color="keltainen", sleep=False):
        super().__init__(species, color, sleep)
        self._subspecies = subspecies

    def move(self):
        return f"{super().move()} - alalaji on {self._subspecies}."

    def wake_up(self):
        self._sleep = False

    def eat(self, food):
        if self._sleep:
            return f"Nukkuva {self._subspecies} ei voi syödä."
        return f"Tänään ruokalistalla on '{food}'."


asiatic_lion = Lion("Aasian leijona", "Leijona", "kaneli", True)
print(asiatic_lion.move())
print(asiatic_lion.eat("Antilooppi"))

barbary_lion = Lion("Barbaarileijona", "Leijona", "kellertävänruskea", True)
barbary_lion.wake_up()
print(barbary_lion.move())
print(barbary_lion.eat("Antilooppi"))
