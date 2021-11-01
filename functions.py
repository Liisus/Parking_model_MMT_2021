from classes import *


def park_to_target(car, lot, target, same_dist=0):
    min_dist = -1
    start = None
    for i in range(len(lot.get_places())):
        values = lot.check_place(car, i, same_dist=same_dist)
        if values:
            if values[0] <= target <= values[1]:
                min_dist = 0
                start = target
            elif min_dist == -1:
                if abs(values[0] - target) <= abs(values[1] - target):
                    min_dist = abs(values[0] - target)
                    start = values[0]
                else:
                    min_dist = abs(values[1] - target)
                    start = values[1]
            else:
                if min_dist > abs(values[0] - target):
                    min_dist = abs(values[0] - target)
                    start = values[0]
                if min_dist > abs(values[1] - target):
                    min_dist = abs(values[1] - target)
                    start = values[1]
    if start is not None:
        if lot.take_place(car, start):
            return 1
        else:
            raise BadCodeError
    else:
        return 0


def optimal_park_to_target(car, lot, target, same_dist=0):
    min_dist = -1
    start = None
    for i in range(len(lot.get_places())):
        values = lot.check_place(car, i, same_dist=same_dist)
        if values:
            if min_dist == -1:
                if abs(values[0] - target) <= abs(values[1] - target):
                    min_dist = abs(values[0] - target)
                    start = values[0]
                else:
                    min_dist = abs(values[1] - target)
                    start = values[1]
            else:
                if min_dist > abs(values[0] - target):
                    min_dist = abs(values[0] - target)
                    start = values[0]
                if min_dist > abs(values[1] - target):
                    min_dist = abs(values[1] - target)
                    start = values[1]
    if start is not None:
        if lot.take_place(car, start):
            return 1
        else:
            raise BadCodeError
    else:
        return 0


def timeless_park_to_target(car, lot, target, same_dist=0, c=1):
    min_dist = 0
    start = None
    for i in range(len(lot.get_places())):
        values = lot.check_place(car, i, same_dist=same_dist)
        if values:
            if values[0] <= target <= values[1]:
                start = target
                break
            elif min_dist == 0:
                if abs(values[0] - target) <= abs(values[1] - target):
                    min_dist = values[0] - target
                    start = values[0]
                else:
                    min_dist = values[1] - target
                    start = values[1]
            elif min_dist <= -15 * c:
                if abs(values[0] - target) <= abs(values[1] - target):
                    temp0 = values[0] - target
                    temp1 = values[0]
                else:
                    temp0 = values[1] - target
                    temp1 = values[1]
                if abs(min_dist) + (2 * lot.get_len() - temp1 + start) * 0.4 > abs(temp0):
                    min_dist = temp0
                    start = temp1
            else:
                if abs(min_dist) > abs(values[0] - target):
                    min_dist = values[0] - target
                    start = values[0]
                if abs(min_dist) > abs(values[1] - target):
                    min_dist = values[1] - target
                    start = values[1]
    if start is not None:
        if lot.take_place(car, start):
            return 1
        else:
            raise BadCodeError
    else:
        return 0


def optimal_timeless_park_to_target(car, lot, target, same_dist=0, c=1):
    min_dist = 0
    start = None
    for i in range(len(lot.get_places())):
        values = lot.check_place(car, i, same_dist=same_dist)
        if values:
            if min_dist == 0:
                if abs(values[0] - target) <= abs(values[1] - target):
                    min_dist = values[0] - target
                    start = values[0]
                else:
                    min_dist = values[1] - target
                    start = values[1]
            elif min_dist <= -15 * c:
                if abs(values[0] - target) <= abs(values[1] - target):
                    temp0 = values[0] - target
                    temp1 = values[0]
                else:
                    temp0 = values[1] - target
                    temp1 = values[1]
                if abs(min_dist) + (2 * lot.get_len() - temp1 + start) * 0.4 > abs(temp0):
                    min_dist = temp0
                    start = temp1
            else:
                if abs(min_dist) > abs(values[0] - target):
                    min_dist = values[0] - target
                    start = values[0]
                if abs(min_dist) > abs(values[1] - target):
                    min_dist = values[1] - target
                    start = values[1]
    if start is not None:
        if lot.take_place(car, start):
            return 1
        else:
            raise BadCodeError
    else:
        return 0


def remove_car(lot, index):
    lot.remove_car(index)


def to_minutes(hours, minutes):
    return hours * 60 + minutes
