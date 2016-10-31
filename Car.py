import random

ENGINE_TYPE_DIESEL = 'diesel'
ENGINE_TYPE_PETROL = 'petrol'

PETROL_PRICE = 2.4
DIESEL_PRICE = 1.8

KM_PULL_MONEY = 1000
MONEY_FOR_KM_DIESEL = 10.5
MONEY_FOR_KM_PETROL = 9.5

def define_engine_type(number):
    if (number+1) % 3 == 0:
        engine = ENGINE_TYPE_DIESEL
    else:
        engine = ENGINE_TYPE_PETROL
    return engine

def define_fuel_tank(number):
    if (number+1) % 5 == 0:
        fuel_tank = 75
    else:
        fuel_tank = 60
    return fuel_tank

def define_fuel_flow():
    if define_engine_type(len(Cars.all_cars)) == ENGINE_TYPE_DIESEL:
        fuel_flow = 6
    else:
        fuel_flow = 8
    return fuel_flow

def define_max_mileage():
    if define_engine_type(len(Cars.all_cars)) == ENGINE_TYPE_DIESEL:
        max_mileage = 150000
    else:
        max_mileage = 100000
    return max_mileage

def define_repair_price():
    if define_engine_type(len(Cars.all_cars)) == ENGINE_TYPE_DIESEL:
        repair_price = 700
    else:
        repair_price = 500
    return repair_price

def define_route_lengt():
    route = random.randint(55000, 286000)
    return route


class Cars:
    all_cars = []

    def __init__(self, price=10000):
        self.engine = define_engine_type(len(Cars.all_cars))
        self.fuel_tank = define_fuel_tank(len(Cars.all_cars))
        self.price = price
        self.max_mileage = define_max_mileage()
        self.fuel_flow = define_fuel_flow()
        self.repair_price = define_repair_price()
        self.route_lenght = define_route_lengt()
        self.money_spent = 0 #денег потрачено
        self.start_tachometer = 0 # пробег
        self.remaining_value = 0 # остаточная стоимость
        self.fuel_count = 0 #потрачено топлива
        self.count_filling_car = 0  # кол-во заправок
        self.mileage_utilisation = 0 #осталось пробега до утилизации
        self.count_repair = 0
        self.km_on_one_tank = 0
        self.temp_param_fuel = 0


        Cars.all_cars.append(self)

    # def param_for_fuel(self, procent=0.01):
    #     temp_list = []
    #     for elem in range(self.route_lenght):
    #         if elem != 0 and elem % 2 == 0:
    #             temp = self.fuel_flow * procent
    #             self.fuel_flow += temp


    def capremont(self):
        self.count_repair = self.route_lenght // self.max_mileage

    def money_for_repair(self):
        self.money_spent += self.count_repair * self.repair_price

    def km_on_tank(self, lenght_km=100):
        self.km_on_one_tank = (self.fuel_tank / self.fuel_flow) * lenght_km

    def filling_car(self):
        self.count_filling_car = self.route_lenght // self.km_on_one_tank

    def money_for_filling_car(self):
        if self.engine == ENGINE_TYPE_DIESEL:
            self.money_spent += self.count_filling_car * self.fuel_tank * DIESEL_PRICE
        else:
            self.money_spent += self.count_filling_car * self.fuel_tank * PETROL_PRICE

    def price_vs_km(self):
        if self.engine == ENGINE_TYPE_DIESEL:
            self.remaining_value = self.price - (self.route_lenght // KM_PULL_MONEY * MONEY_FOR_KM_DIESEL)
        else:
            self.remaining_value = self.price - (self.route_lenght // KM_PULL_MONEY * MONEY_FOR_KM_PETROL)

    # def __str__(self):
    #     print(self.start_tachometer)


for car in range(100):
    car_obj = Cars()

for elem in Cars.all_cars:
     elem.capremont()
     elem.money_for_repair()
     elem.km_on_tank()
     elem.filling_car()
     elem.money_for_filling_car()
     elem.price_vs_km()
     # elem.param_for_fuel()

for i in Cars.all_cars:
    print(i.__dict__)
    # print(i.count_repair, end=", ")













