import random

KM_PULL_MONEY = 1000


class Petrol:
    """to do"""
    ENGINE_TYPE = 'petrol'
    PETROL_PRICE = 2.4
    MONEY_FOR_KM = 9.5
    MAX_MILEAGE = 150000
    FUEL_FLOW = 8
    REPAIR_PRICE = 500


class Diesel:
    """to do"""
    ENGINE_TYPE = 'diesel'
    DIESEL_PRICE = 1.8
    MONEY_FOR_KM = 10.5
    MAX_MILEAGE = 100000
    FUEL_FLOW = 6
    REPAIR_PRICE = 700


class Car_Settings:

    @staticmethod
    def engine_type(number):
        if (number + 1) % 3 == 0:
            engine = Diesel.ENGINE_TYPE
        else:
            engine = Petrol.ENGINE_TYPE
        return engine

    @staticmethod
    def fuel_tank(number):
        if (number + 1) % 5 == 0:
            fuel_tank = 75
        else:
            fuel_tank = 60
        return fuel_tank

    def max_mileage(self):
        if self.engine_type(len(Cars.all_cars)) == Diesel.ENGINE_TYPE:
            max_mileage = Diesel.MAX_MILEAGE
        else:
            max_mileage = Petrol.MAX_MILEAGE
        return max_mileage

    def fuel_flow(self):
        if self.engine_type(len(Cars.all_cars)) == Diesel.ENGINE_TYPE:
            fuel_flow = Diesel.FUEL_FLOW
        else:
            fuel_flow = Petrol.FUEL_FLOW
        return fuel_flow

    def repair_price(self):
        if self.engine_type(len(Cars.all_cars)) == Diesel.ENGINE_TYPE:
            repair_price = Diesel.REPAIR_PRICE
        else:
            repair_price = Petrol.REPAIR_PRICE
        return repair_price

    @staticmethod
    def route_length():
        route = random.randint(55000, 286000)
        return route

    @property
    def tachograph(self):
        return self.route_length


class Cars(Car_Settings):
    all_cars = []

    def __init__(self, price=10000):
        self.engine = Car_Settings.engine_type(len(Cars.all_cars))
        self.fuel_tank = Car_Settings.fuel_tank(len(Cars.all_cars))
        self.price = price
        self.max_mileage = Car_Settings.max_mileage(self)
        self.fuel_flow = Car_Settings.fuel_flow(self)
        self.repair_price = Car_Settings.repair_price(self)
        self.route_length = Car_Settings.route_length()
        self.money_spent = 0  # денег потрачено
        self.tachometer = Car_Settings().tachograph  # пробег
        self.remaining_value = 0  # остаточная стоимость
        self.fuel_count = 0  # потрачено топлива
        self.count_filling_car = 0  # кол-во заправок
        self.mileage_utilisation = 0  # осталось пробега до утилизации
        self.count_repair = 0
        self.km_on_one_tank = 0
        self.temp_fuel_flow = 0

        Cars.all_cars.append(self)

    # def param_for_fuel(self, percent=0.01):
    #     temp_list = []
    #     for elem in self.route_length:
    #         if elem != 0 and elem % 1000 == 0:
    #             temp = self.fuel_flow * percent
    #             self.fuel_flow += temp
    #             temp_list.append(self.fuel_flow)
    #     last = temp_list[-1]
    #     self.temp_fuel_flow = last


    def full_repair(self):
        self.count_repair = self.route_length // self.max_mileage
        return self.count_repair

    def money_for_repair(self):
        self.money_spent += self.count_repair * self.repair_price
        return round(self.money_spent, 2)

    def km_on_tank(self, lenght_km=100):
        self.km_on_one_tank = (self.fuel_tank / self.fuel_flow) * lenght_km
        return round(self.km_on_one_tank, 2)

    def filling_car(self):
        self.count_filling_car = self.route_length // self.km_on_one_tank
        return round(self.count_filling_car, 2)

    def money_for_filling_car(self):
        if self.engine == Diesel.ENGINE_TYPE:
            self.money_spent += self.count_filling_car * self.fuel_tank * Diesel.DIESEL_PRICE
        else:
            self.money_spent += self.count_filling_car * self.fuel_tank * Petrol.PETROL_PRICE
        return round(self.money_spent, 2)

    def price_vs_km(self):
        if self.engine == Diesel.ENGINE_TYPE:
            self.remaining_value = self.price - (self.route_length // KM_PULL_MONEY * Diesel.MONEY_FOR_KM)
        else:
            self.remaining_value = self.price - (self.route_length // KM_PULL_MONEY * Petrol.MONEY_FOR_KM)
        return round(self.remaining_value, 2)

        # def __str__(self):
        #     print(self.start_tachometer)


for car in range(1):
    car_obj = Cars()


for elem in Cars.all_cars:
    print(elem.tachometer)
    print(elem.full_repair())
    print(elem.money_for_repair())
    print(elem.km_on_tank())
    print(elem.filling_car())
    print(elem.money_for_filling_car())
    print(elem.price_vs_km())
    # elem.param_for_fuel()

# for i in Cars.all_cars:
#     print(i.temp_fuel_flow)
#     # print(i.count_repair, end=", ")
