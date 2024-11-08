import random

class Pet:
    def __init__(self, name="Pet", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.gladness = 50

    def play(self):
        self.gladness += 10
        self.hunger += 5
        self.energy -= 10
        print(f"{self.name} is happy after playing!")

    def eat(self):
        self.hunger -= 10
        self.energy += 5
        print(f"{self.name} ate some food!")

    def sleep(self):
        self.energy += 15
        self.hunger += 5
        print(f"{self.name} is well-rested.")

    def is_alive(self):
        if self.hunger > 100:
            print(f"{self.name} is too hungry and feels unwell.")
            return False
        if self.energy < 0:
            print(f"{self.name} is too tired to continue.")
            return False
        return True


class Human:
    def __init__(self, name="Human", pet=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.money = 100
        self.gladness = 50
        self.food = 50
        self.pet = pet

    def adopt_pet(self, pet_name, *args, **kwargs):
        self.pet = Pet(name=pet_name, *args, **kwargs)
        print(f"{self.name} adopted a pet named {self.pet.name}!")

    def play_with_pet(self):
        if self.pet:
            self.pet.play()
            self.gladness += 5
            print(f"{self.name} is happy playing with {self.pet.name}.")
        else:
            print(f"{self.name} has no pet to play with.")

    def feed_pet(self):
        if self.pet:
            self.pet.eat()
            self.food -= 5
            print(f"{self.name} fed {self.pet.name}.")
        else:
            print(f"{self.name} has no pet to feed.")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.food < 0:
            print("Starvation…")
            return False
        return True

    def live(self, day):
        print(f"--- Day {day} ---")
        if not self.is_alive():
            print("Game over!")
            return False
        if self.pet and not self.pet.is_alive():
            print(f"{self.pet.name} has passed away.")
            return False

        action = random.choice(['play_with_pet', 'feed_pet', 'do_nothing'])
        if action == 'play_with_pet':
            self.play_with_pet()
        elif action == 'feed_pet':
            self.feed_pet()
        elif action == 'do_nothing':
            print(f"{self.name} is resting.")
        
        return True


human = Human(name="Human")
human.adopt_pet("Sharik")

for day in range(1, 15):
    if not human.live(day):
        break
