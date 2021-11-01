from classes import *
from functions import *
from random import randint, choice, random

cap = randint(24, 24)
parking_length = 650 * cap
car_len = [3.7, 4.8]
car_wid = [1.5, 1.8]

behavior = [park_to_target, timeless_park_to_target,
            optimal_timeless_park_to_target, optimal_park_to_target][2:3:]
behavior_dist = [0, 1][0:1]
behavior_start = [0, 1][1:]

intervals = [(940, 1100, 3, 7, 0.10), (440, 500, 3, 7, 0.10),
             (1230, 660, 30, 150, 0.01), (660, 1230, 30, 60, 0.65),
             (440, 500, 500, 600, 0.10), (1200, 1260, 600, 660, 0.012),
             (1200, 1260, 3, 7, 0.012), (330, 390, 3, 7, 0.012)]

days = 160

lot = ParkingLot(parking_length)
tagged = TaggedLot(cap)

limit_0, limit_1 = 540, 1260
caps, t_caps = 0, 0
counts, t_counts = 0, 0

for i in range(days):
    for j in range(1440):
        for interval in intervals:
            if interval[0] <= j <= interval[1] or (interval[1] < interval[0] and
                                                   (interval[0] <= j or interval[1] >= j)):
                if randint(0, 100000) / 100000 <= interval[4]:

                    temp_car = Car(randint(round(car_len[0] * 10), round(car_len[1] * 10)) / 10,
                                   randint(round(car_wid[0] * 10), round(car_wid[1] * 10)) / 10,
                                   time=j + randint(interval[2], interval[3]))
                    temp_beh = choice(behavior)
                    temp_targ = choice(behavior_start) * randint(0, round(parking_length * 10)) / 10
                    temp_st = choice(behavior_start)

                    if not temp_beh(temp_car, lot, temp_targ, same_dist=temp_st):
                        pass

                    if not temp_beh(temp_car, tagged, temp_targ, same_dist=temp_st):
                        pass

        car_i = 0
        while car_i < len(lot.get_cars()):
            car = lot.get_cars()[car_i]
            if car.get_time() <= j:
                remove_car(lot, car_i)
                car_i -= 1
            car_i += 1

        while car_i < len(tagged.get_cars()):
            car = tagged.get_cars()[car_i]
            if car.get_time() <= j:
                remove_car(tagged, car_i)
                car_i -= 1
            car_i += 1

        if limit_0 <= j <= limit_1:
            caps += len(lot.get_cars())
            counts += 1

            t_caps += len(tagged.get_cars())
            t_counts += 1

print(caps / counts, t_caps / t_counts)
