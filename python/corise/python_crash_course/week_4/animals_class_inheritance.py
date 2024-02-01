class Animal:
    species_name = "Animal"
    scientific_name = "Animalia"
    play_multiplier = 2
    interact_increment = 1

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.calories_eaten  = 0
        self.happiness = 0

    def play(self, num_hours):
        self.happiness += (num_hours * self.play_multiplier)
        print("WHEEE PLAY TIME!")

    def eat(self, food):
        self.calories_eaten += food.calories
        print(f"Om nom nom yummy {food.name}")
        if self.calories_eaten > self.calories_needed:
            self.happiness -= 1
            print("Ugh so full")

    def interact_with(self, animal2):
        self.happiness += self.interact_increment
        print(f"Yay happy fun time with {animal2.name}")


class Sloth(Animal):
    """
    >>> Sloth.species_name
    "Hoffmann's two-toed sloth"
    >>> Sloth.scientific_name
    'Choloepus hoffmanni'
    >>> Sloth.calories_needed
    680
    >>> buttercup = Sloth('Buttercup', 27)
    >>> buttercup.name
    'Buttercup'
    >>> buttercup.age
    27
    """
    species_name = "Hoffmann's two-toed sloth"
    scientific_name = 'Choloepus hoffmanni'
    play_multiplier = 2
    interact_increment = 1
    calories_needed = 600


class Cat(Animal):
    """
    >>> Cat.species_name
    'Domestic cat'
    >>> Cat.scientific_name
    'Felis silvestris catus'
    >>> Cat.calories_needed
    200
    >>> jackson = Cat("Jackson", 8)
    >>> jackson.name
    'Jackson'
    >>> jackson.age
    8
    """
    species_name = 'Domestic cat'
    scientific_name = 'Felis silvestris catus'
    play_multiplier = 2
    interact_increment = 1
    calories_needed = 300