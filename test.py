from classes import *
from functions import *
from random import randint, choice, random

lot = TaggedLot(24)

for i in range(5):
    timeless_park_to_target(Car(4, 1.5), lot, 0)


print(lot.get_places())