import pygame
from classes import *
from functions import *
from random import randint

length, c = 100, 10
lot = ParkingLot(length * c)
time = 0

if __name__ == '__main__':
    pygame.init()
    size = width, height = length * c, 5 + round(2.5 * c)
    screen = pygame.display.set_mode(size)

    running = True
    v = 64
    clock = pygame.time.Clock()
    point = 0

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    point = randint(5, length * c - 5)
                    optimal_timeless_park_to_target(Car(randint(round(3.8 * c), round(4.7 * c)),
                                                        1.6 * c,
                                                        time=time + randint(100, 500)),
                                                    lot, point, 1, c)
                elif event.key == pygame.K_r:
                    if len(lot.get_cars()):
                        lot.remove_car(randint(-1, len(lot.get_cars()) - 1))

        screen.fill((255, 255, 255))

        pygame.draw.line(screen, 'black', (0, 5), (width, 5))
        pygame.draw.rect(screen, 'red', (point, 2, 5, 5))
        i = 0
        while i < len(lot.get_cars()):
            car = lot.get_cars()[i]
            if 0 <= car.get_time() < time:
                lot.remove_car(i)
                continue
            pygame.draw.rect(screen, 'blue', (round(car.get_start()),
                                              6, round(car.get_len()),
                                              round(car.get_width())),
                             c // 3)
            i += 1

        pygame.display.flip()
        clock.tick(v)
        time += 1

    pygame.quit()
