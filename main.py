# class Human:
#    def __init__(self, name = 'Human'):
#        self.name = name
#
# class Auto:
#    def __init__(self, brand):
#        self.brand = brand
#        self.passengers = []
#
#
#    def add_passengers(self,human):
#        self.passengers.append(human)
#
#    def print_passengers_names(self):
#        if self.passengers != []:
#            print(f"Names of {self.brand} passengers")
#            for passenger in self.passengers:
#                print(passenger.name)
#        else:
#            print(f"There are no passengers in {self.brand}")
#
#
# petya = Human('Petya')
# mari = Human('Mari')
# car = Auto('Mercedes')
#
# car.add_passengers(petya)
# car.add_passengers(mari)
# car.print_passengers_names()
import random


class Human:
    def __init__(self, name='Human', home=None, job=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.home = Auto(brands_of_car)

    def job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('I bought delicacies')
            self.money -= 15
            self.gladness += 10
            self.satiety += 2

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strangth += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f"Today the {day} of {self.name}'s life"
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", '\n')
        print(f"Money - {self.money}")
        print(f"Satiety - {self.satiety}")
        print(f"Gladness - {self.gladness}")
        home_indexes = "Home indexes"
        print(f"{human_indexes:^50}", '\n')
        print(f"Food - {self.food}")
        print(f"Mess - {self.mess}")
        car_indexes = f"{self.car.brand}"
        print(f"{car_indexes:^50}", '\n')
        print(f"Fuel - {self.car.fuel}")
        print(f"Strangth - {self.strangth}")


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __int__(self):
        self.mess = 0
        self.food = 0


job_list = {
    'Java developer': {'salery': 50, 'gladness_less': 10},
    'Pyton developer': {'salery': 40, 'gladness_less': 3},
    'C++ developer': {'salery': 45, 'gladness_less': 25},
    'Rust developer': {'salery': 70, 'gladness_less': 1},
}
brands_of_car = {
    'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
    'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
    'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
    'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
}


class Job:
    def __int__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

class Friends:
     def make_friends(self):
            friend_name = input("Enter friend's name: ")
            self.friends
# print(list(job_list))

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
