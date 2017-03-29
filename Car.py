import random


class Fuel: # выноси в отдельный модуль
    class Petrol:
        ENGINE_TYPE = 'petrol'
        PETROL_PRICE = 2.4
        MAX_MILEAGE = 100000
        FUEL_FLOW = 8
        REPAIR_PRICE = 500
        PRICE_DECREASE = 9.5
        FUEL_FLOW_INCREASE = 0.01

    class Diesel:
        ENGINE_TYPE = 'diesel'
        DIESEL_PRICE = 1.8
        MAX_MILEAGE = 150000
        FUEL_FLOW = 6
        REPAIR_PRICE = 700
        PRICE_DECREASE = 10.5
        FUEL_FLOW_INCREASE = 0.01


class CarSettings:
    @staticmethod
    def engine_type(number, num=3):
        if (number + 1) % num == 0:
            engine = Fuel.Diesel.ENGINE_TYPE
        else:
            engine = Fuel.Petrol.ENGINE_TYPE
        return engine

    @staticmethod
    def fuel_tank(number, num=5):
        if (number + 1) % num == 0:
            fuel_tank = 75
        else:
            fuel_tank = 60
        return fuel_tank

    def max_mileage(self):
        if self.engine_type(len(Cars.all_cars)) == Fuel.Diesel.ENGINE_TYPE:
            max_mileage = Fuel.Diesel.MAX_MILEAGE
        else:
            max_mileage = Fuel.Petrol.MAX_MILEAGE
        return max_mileage

    def fuel_flow(self):
        if self.engine_type(len(Cars.all_cars)) == Fuel.Diesel.ENGINE_TYPE:
            fuel_flow = Fuel.Diesel.FUEL_FLOW
        else:
            fuel_flow = Fuel.Petrol.FUEL_FLOW
        return fuel_flow

    def repair_price(self):
        if self.engine_type(len(Cars.all_cars)) == Fuel.Diesel.ENGINE_TYPE:
            price = Fuel.Diesel.REPAIR_PRICE
        else:
            price = Fuel.Petrol.REPAIR_PRICE
        return price

    @staticmethod
    def route_length():
        route = random.randint(55000, 286000)
        return route


class Cars(CarSettings):
    all_cars = []

    def __init__(self, price=10000):
        # super для инициализации CarSettings, иначе наследоване лишнее
        self.engine = CarSettings.engine_type(len(Cars.all_cars))
        self.fuel_tank = CarSettings.fuel_tank(len(Cars.all_cars))
        self.price = price
        self.max_mileage = CarSettings.max_mileage(self)
        self.fuel_flow = CarSettings.fuel_flow(self)
        self.repair_price = CarSettings.repair_price(self)
        self.route_length = CarSettings.route_length()
        self.km_on_one_tank = self.km_on_tank()
        self.count_filling_car = 0  # кол-во заправок
        self.count_repair = 0  # кол-во капремонтов
        self.money_spent = 0  # денег потрачено
        self.tachograph = self.run_km  # пробег
        self.remaining_value = 10000  # остаточная стоимость
        self.mileage_utilisation = 0  # осталось пробега до утилизации
        Cars.all_cars.append(self)

    def money_for_repair(self):
        if self.engine == Fuel.Diesel.ENGINE_TYPE:
            money = Fuel.Diesel.REPAIR_PRICE
        else:
            money = Fuel.Petrol.REPAIR_PRICE
        return money

    def km_on_tank(self, length_km=100):
        km = (self.fuel_tank / self.fuel_flow) * length_km
        return km

    def money_for_filling_car(self):
        if self.engine == Fuel.Diesel.ENGINE_TYPE:
            money = self.fuel_tank * Fuel.Diesel.DIESEL_PRICE
        else:
            money = self.fuel_tank * Fuel.Petrol.PETROL_PRICE
        return money

    def run(self):
        km = 0
        while km < self.route_length:
            km += 1
            if km % 1000 == 0:
                if self.engine == Fuel.Diesel.ENGINE_TYPE:
                    self.remaining_value -= Fuel.Diesel.PRICE_DECREASE
                    self.fuel_flow += self.fuel_flow * Fuel.Diesel.FUEL_FLOW_INCREASE
                else:
                    self.remaining_value -= Fuel.Petrol.PRICE_DECREASE
                    self.fuel_flow += self.fuel_flow * Fuel.Petrol.FUEL_FLOW_INCREASE
            if km % self.km_on_one_tank == 0:
                self.count_filling_car += 1
                self.money_spent += self.money_for_filling_car()
            if km % self.max_mileage == 0:
                self.count_repair += 1
                self.money_spent += self.repair_price
        return km

    @property
    def run_km(self):
        return self.run

    def money_for_fuel(self):
        if self.engine == Fuel.Diesel.ENGINE_TYPE:
            money = Fuel.Diesel.DIESEL_PRICE
        else:
            money = Fuel.Petrol.PETROL_PRICE # getattr(fuel_type)... завтра напомни раскажу
        return money * self.fuel_tank * self.count_filling_car


def out_and_sort():
    for car in range(100):
        car_obj = Cars()
    diesel_after_run = [] # sort или filter для всех машин - и нужен только один массив
    petrol_after_run = []
    
    for n, elem in enumerate(Cars.all_cars):
        elem.run()
        print("I'm the {} car".format(n + 1))
        print("my path is {} km".format(elem.tachograph()))
        print("my remaining value is {} dollars".format(elem.remaining_value))
        print("spending money for fuel = {}".format(elem.money_for_fuel()))
        if elem.engine == Fuel.Diesel.ENGINE_TYPE:
            diesel_after_run.append(elem)
        else:
            petrol_after_run.append(elem)
    diesel_after_run.sort(key=lambda element: element.remaining_value)

out_and_sort()
