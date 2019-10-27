import numpy as np
import pandas as pd
from collections import defaultdict


win_count = defaultdict(int)


def rand(n):
    return np.random.randint(1, n + 1)


def game_(n):
    # global switch_count

    # One car behind a door
    car_door = rand(n)

    # Goats behind all other doors
    goat_doors = [i for i in range(1, n + 1) if i != car_door]

    # Open doors
    open_doors = []

    # Player picks a random door, hoping its a car
    chosen_door = rand(n)
    game = {
        "car": car_door,
        "goats": goat_doors,
        "chosen": chosen_door,
        "open_doors": open_doors,
    }

    # Game show host opens n-2 goat doors
    open_doors = np.random.choice(
        [i for i in goat_doors if i != chosen_door], size=n - 2, replace=False
    )

    closed_doors = [i for i in range(1, n + 1) if i not in open_doors]

    # current scenario
    # print("You have chosen : ")
    # if(chosen_door == car_door):
    # 	print("car")
    # else:
    # 	print("goat")

    # Guy always switches
    always_swticher = [i for i in closed_doors if i != chosen_door][0]

    # never switches
    never_switcher = chosen_door

    # random switches
    random_switcher = np.random.choice(
        [chosen_door, [i for i in closed_doors if i != chosen_door][0]]
    )

    if always_swticher == car_door:
        win_count["always_swticher"] += 1
    if never_switcher == car_door:
        win_count["never_switcher"] += 1
    if random_switcher == car_door:
        win_count["random_switcher"] += 1


for i in range(100000):
    game_(100)

print(win_count)
