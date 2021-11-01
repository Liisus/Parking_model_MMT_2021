from classes import *
from functions import *
from random import randint, choice, shuffle

lens, cars = 0, 0
l_lens, l_cars = 0, 0

f = open('model_4_special_for_Roma.txt', 'w')

for k in range(1):
    count = 0
    s = []
    parking_length = randint(250, 1200)
    car_len = [3.7, 4.8]
    car_wid = [1.5, 1.8]

    behavior = [park_to_target, timeless_park_to_target,
                optimal_timeless_park_to_target, optimal_park_to_target]
    i1 = randint(0, len(behavior) - 1)
    shuffle(behavior)
    behavior = behavior[0:i1 + 1]

    i0 = randint(0, 1)
    i1 = randint(0, 1)
    i0, i1 = min(i0, i1), max(i0, i1)
    behavior_dist = [0, 1][i0:i1 + 1]
    i0 = randint(0, 1)
    i1 = randint(0, 1)
    i0, i1 = min(i0, i1), max(i0, i1)
    behavior_start = [0, 1][i0:i1 + 1]

    timetables = [[
        (to_minutes(8, 0), to_minutes(8, 30), to_minutes(8, 0), to_minutes(9, 0), 0.9),

        (to_minutes(9, 0), to_minutes(19, 0), to_minutes(0, 3), to_minutes(0, 5), 0.2),
        (to_minutes(17, 0), to_minutes(23, 30), to_minutes(0, 30), to_minutes(2, 0), 0.1),
    ], [
        (to_minutes(17, 30), to_minutes(20, 0), to_minutes(11, 0), to_minutes(14, 0), 0.8),

        (to_minutes(10, 0), to_minutes(18, 0), to_minutes(0, 5), to_minutes(0, 15), 0.3),
        (to_minutes(8, 0), to_minutes(19, 0), to_minutes(0, 15), to_minutes(1, 30), 0.1),
        (to_minutes(19, 0), to_minutes(21, 0), to_minutes(0, 30), to_minutes(2, 0), 0.2),
    ], [
        (to_minutes(0, 0), to_minutes(1, 0), to_minutes(11, 0), to_minutes(12, 30), 0.03),
        (to_minutes(12, 0), to_minutes(13, 30), to_minutes(11, 0), to_minutes(13, 0), 0.08),

        # Посетители магазина
        (to_minutes(23, 0), to_minutes(5, 59), to_minutes(0, 5), to_minutes(0, 20), 0.05),
        (to_minutes(6, 0), to_minutes(16, 59), to_minutes(0, 3), to_minutes(0, 30), 0.2),
        (to_minutes(17, 0), to_minutes(18, 59), to_minutes(0, 10), to_minutes(1, 15), 0.3),
        (to_minutes(19, 0), to_minutes(22, 59), to_minutes(0, 5), to_minutes(0, 15), 0.2),
    ]]

    intervals = choice(timetables)

    days = 365

    lot = ParkingLot(parking_length)

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
                        temp_targ = choice(behavior_start) * randint(0,
                                                                     round(parking_length * 10)) / 10
                        temp_st = choice(behavior_start)

                        if not temp_beh(temp_car, lot, temp_targ, same_dist=temp_st):
                            pass

            car_i = 0
            while car_i < len(lot.get_cars()):
                car = lot.get_cars()[car_i]
                if car.get_time() <= j:
                    remove_car(lot, car_i)
                    car_i -= 1
                car_i += 1

            s.append(len(lot.get_cars()))
        count += 1

    print(f'parking_length: {parking_length} - {s}', file=f)