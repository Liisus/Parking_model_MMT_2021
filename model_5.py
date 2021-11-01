from classes import *
from functions import *
from random import randint, choice, shuffle


div, l_div = 0, 0
counter = 0


for k in range(1000):
    cap = randint(15, 35)
    parking_length = 6.5 * cap
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

    intervals = [(940, 1100, 3, 7, 0.10), (440, 500, 3, 7, 0.10),
                 (1230, 660, 30, 150, 0.01), (660, 1230, 30, 60, 0.65),
                 (440, 500, 500, 600, 0.10), (1200, 1260, 600, 660, 0.012),
                 (1200, 1260, 3, 7, 0.012), (330, 390, 3, 7, 0.012)]
    i1 = randint(0, len(intervals) - 1)
    shuffle(intervals)
    intervals = intervals[0:i1 + 1]

    days = 365

    lot = ParkingLot(parking_length)
    tagged = TaggedLot(cap)

    limit_0, limit_1 = 540, 1260
    l_caps, l_t_caps = caps, t_caps = 0, 0
    l_counts, l_t_counts = counts, t_counts = 0, 0

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
                            l_counts += 1
                            l_caps += len(lot.get_cars())

                        if not temp_beh(temp_car, tagged, temp_targ, same_dist=temp_st):
                            l_t_counts += 1
                            l_t_caps += len(tagged.get_cars())

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

        div += (caps / counts) / (t_caps / t_counts)
        if l_counts and l_t_counts:
            l_div += (l_caps / l_counts) / (l_t_caps / l_t_counts)
        counter += 0


print(div / counter, '- average increase of car for 1m')
print(l_div / counter, '- average limited increase of car for 1m')
