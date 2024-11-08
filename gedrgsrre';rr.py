import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.food = 50

    def get_home(self):
        self.home = House()

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    
    def get_car(self):
        self.car = Auto(brands_of_car)
    
    def eat(self):
        if self.home.food_amount <= 0:
            self.shopping('food')
        else:
            if self.food >= 100:
                self.food = 100
            self.food += 5
            self.home.food_amount -= 5
    
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.food -= 4
    
    def shopping(self, action):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                action = 'fuel'
            else:
                self.to_repair()
                return
        if action == 'fuel':
            print("I bought fuel.")
            self.money -= 100
            self.car.fuel += 80
        elif action == 'food':
            print("I bought food.")
            self.money -= 50
            self.home.food_amount += 50

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    
    def clean_home(self):
        self.gladness -= 5
        self.home.mess -= 8
    
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.food < 0:
            print("Starvation…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False
        return True

    def days_indexes(self, day):
        day_info = f"--- Day {day} ---\n"
        status_info = (
            f"{self.name}'s stats:\n"
            f"Money: {self.money}\n"
            f"Gladness: {self.gladness}\n"
            f"Food: {self.food}\n"
            f"Home mess: {self.home.mess}\n"
            f"Car fuel: {self.car.fuel}\n"
            f"Car strength: {self.car.strength}\n"
        )
        print(day_info + status_info)

    def live(self, day):
        self.days_indexes(day)
        if not self.is_alive():
            print("Game over!")
            return False

        action = random.choice(['work', 'chill', 'clean_home', 'eat'])
        if action == 'work':
            self.work()
        elif action == 'chill':
            self.chill()
        elif action == 'clean_home':
            self.clean_home()
        elif action == 'eat':
            self.eat()

        return True

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Tesla": {"fuel": 80, "strength": 150, "consumption": 4},
    "Volvo": {"fuel": 120, "strength": 130, "consumption": 7}
}

job_list = {
    "Developer": {"salary": 50, "gladness_less": 10},
    "Designer": {"salary": 40, "gladness_less": 8},
    "Manager": {"salary": 70, "gladness_less": 15}
}

class Auto:
    def __init__(self, brands_list):
        self.brand = random.choice(list(brands_list))
        self.fuel = brands_list[self.brand]['fuel']
        self.strength = brands_list[self.brand]['strength']
        self.consumption = brands_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Car cannot move.")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food_amount = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

person = Human(name="John")
person.get_home()
person.get_car()
person.get_job()

for day in range(1, 366):
    if not person.live(day):
        break
