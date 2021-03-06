class Car:
    def __init__(self, length=4.3, width=1.6, start=0, time=-1):
        self.position = start
        self.length = length
        self.width = width
        self.time = time

    def get_len(self):
        return self.length

    def get_start(self):
        return self.position

    def set_start(self, start):
        self.position = start

    def set_end(self, end):
        self.position = end - self.length

    def get_end(self):
        return self.position + self.length

    def get_width(self):
        return self.width

    def get_space(self):
        return self.length + self.width

    def get_time(self):
        return self.time


def r_2(num):
    return round(num * 100) / 100


class ParkingLot:
    def __init__(self, length):
        self.length = length
        self.cars = []
        self.places = [(0, self.length)]

    def check_place(self, car, place, same_dist=0):
        if self.places[place][1] >= car.get_space():
            if same_dist:
                a = self.places[place][0] + car.get_width() / 2
                b = sum(self.places[place]) - car.get_width() / 2 - car.get_len()
            elif len(self.places) == 1:
                a, b = 0, sum(self.places[place]) - car.get_len()
            elif place == 0:
                a = 0
                b = min(sum(self.places[place]) + self.places[place + 1][1]
                        - self.cars[place].get_width(), self.cars[place].get_start()) - car.get_len()
            elif place == len(self.places) - 1:
                a = self.places[place][0] + max(self.cars[place - 1].get_width() -
                                                self.places[place - 1][1], 0)
                b = self.length - car.get_len()
            else:
                a = self.places[place][0] + max(self.cars[place - 1].get_width() -
                                                self.places[place - 1][1], 0)
                b = min(sum(self.places[place]) + self.places[place + 1][1]
                        - self.cars[place].get_width(), self.cars[place].get_start()) - car.get_len()
            if a <= b:
                return [a, b]
        return []

    def take_place(self, car, position):
        for i in range(len(self.places)):
            if self.places[i][0] <= r_2(position) <= r_2(sum(self.places[i])):
                if self.places[i][1] >= r_2(car.get_space()):
                    if r_2(car.get_len() + position) <= r_2(sum(self.places[i])):
                        self.cars.insert(i, car)
                        car.set_start(position)
                        self.places = self.places[:i:] + \
                                      [(self.places[i][0],
                                        r_2(car.get_start() - self.places[i][0])),
                                       (r_2(car.get_end()), r_2(sum(self.places[i]) -
                                                                car.get_end()))] + \
                                      self.places[i + 1:]
                        return 1
                break
        return 0

    def remove_car(self, car_i):
        if self.places[car_i][1] + self.places[car_i + 1][1] >= \
                r_2(self.cars[car_i].get_width()) or car_i in {0, len(self.cars) - 1}:
            car_i = car_i % len(self.cars)
            self.places = self.places[:car_i] + \
                          [(r_2(self.places[car_i][0]), r_2(self.places[car_i][1] +
                                                            self.places[car_i + 1][1] + self.cars[
                                                                car_i].get_len()))] + \
                          self.places[car_i + 2:]

            self.cars.pop(car_i)
            return 1
        return 0

    def get_places(self):
        return self.places

    def get_cars(self):
        return self.cars

    def get_len(self):
        return self.length


class TaggedLot:
    def __init__(self, num, tag=6.5):
        self.places = [0] * num
        self.cars = []
        self.length = num * tag
        self.tag = tag

    def check_place(self, car, place, same_dist=0):
        if self.places[place]:
            return []
        if ((self.places[place - 1] != 0) and self.places[(place + 1) % len(self.places)] != 0 and
                place not in {0, len(self.places) - 1}):
            if (2 * self.tag - self.places[place - 1].get_len() - self.places[place + 1].get_len() <
                    2 * car.get_width()):
                return []
        return [place * self.tag, place * self.tag]

    def take_place(self, car, position):
        for i in range(len(self.places)):
            if position == i * self.tag:
                if (self.places[i - 1] == 0 or self.places[(i + 1) % len(self.places)] == 0 or
                        i in {0, len(self.places) - 1}):
                    self.places[i] = car
                    self.cars.append(car)
                    car.set_start(i)
                    return 1
                elif (2 * self.tag - self.places[i - 1].get_len()
                      - self.places[i + 1].get_len() >= 2 * car.get_width()):
                    self.places[i] = car
                    self.cars.append(car)
                    car.set_start(i)
                    return 1
        return 0

    def remove_car(self, car_i):
        place = self.cars[car_i].get_start()
        if ((self.places[place - 1] != 0) and self.places[(place + 1) % len(self.places)] != 0 and
                place not in {0, len(self.places) - 1}):
            if (2 * self.tag - self.places[place - 1].get_len() - self.places[place + 1].get_len() <
                    2 * self.cars[car_i].get_width()):
                return 0
        car_i = car_i % len(self.cars)
        self.places[place] = 0
        self.cars.pop(car_i)
        return 1

    def get_places(self):
        return self.places

    def get_cars(self):
        return self.cars

    def get_len(self):
        return self.length


class BadCodeError(Exception):
    def __init__(self):
        pass
