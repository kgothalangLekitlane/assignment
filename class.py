
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, and I protect {self.city} with my power: {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, power, city, wingspan):
        super().__init__(name, power, city)
        self.wingspan = wingspan

    def introduce(self):
        print(f"I am {self.name}, I soar through the skies over {self.city} with my {self.wingspan}ft wings!")


class TechHero(Superhero):
    def __init__(self, name, power, city, gadget):
        super().__init__(name, power, city)
        self.gadget = gadget

    def introduce(self):
        print(f"{self.name} here – fighting crime in {self.city} using my {self.gadget}!")


hero1 = Superhero("ShadowStrike", "Invisibility", "Night City")
hero2 = FlyingHero("SkyWing", "Flight", "Cloud City", 15)
hero3 = TechHero("ByteBlade", "Tech Mastery", "Cyber Town", "AI Drone Suit")


hero1.introduce()
hero2.introduce()
hero3.introduce()
