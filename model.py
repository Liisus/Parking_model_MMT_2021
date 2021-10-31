from classes import *
from functions import *
from random import randint, choice, random


cap = randint(15, 30)
parking_length = 6.5 * cap
car_len = [3.7, 4.8]
car_wid = [1.5, 1.8]

behavior = [park_to_target, timeless_park_to_target,
            optimal_timeless_park_to_target, optimal_park_to_target][0:-2:-1]
behavior_dist = [0, 1][0:0]
behavior_start = [0, 1][0:0]

times = []
# (440, 500, 500, 600, 0.05)
# (660, 1230, 30, 60, 0.08)
# (1260, 360, 30, 150, 0.01)
# (440, 500, 3, 7, 0.10)
# (940, 1100, 3, 7, 0.10)

lot = ParkingLot(parking_length)

