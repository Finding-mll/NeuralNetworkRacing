"""
-- 14 24 34 --
03          43
02          42
01          41
-- 10 20 30 --
"""

# name, car, handicap (best 1 worst 10), color
drivers_init = [
    ["BOT", "alfaromeo", 7, (133, 25, 30, 200)],
    ["ZHO", "alfaromeo", 7, (133, 25, 30, 200)],
    ["GAS", "alphatauri", 6, (48, 69, 96, 200)],
    ["TSU", "alphatauri", 6, (48, 69, 96, 200)],
    ["OCO", "alpine", 8, (57, 145, 245, 200)],
    ["ALO", "alpine", 8, (57, 145, 245, 200)],
    ["HUL", "astonmartin", 9, (25, 145, 109, 200)],
    ["STR", "astonmartin", 9, (25, 145, 109, 200)],
    ["LEC", "ferrari", 1, (204, 42, 30, 200)],
    ["SAI", "ferrari", 1, (204, 42, 30, 200)],
    ["SCH", "haas", 5, (255, 255, 255, 200)],
    ["MAG", "haas", 5, (255, 255, 255, 200)],
    ["RIC", "mclaren", 9, (242, 156, 57, 200)],
    ["NOR", "mclaren", 9, (242, 156, 57, 200)],
    ["HAM", "mercedes", 3, (95, 207, 191, 200)],
    ["RUS", "mercedes", 3, (95, 207, 191, 200)],
    ["PER", "redbull", 2, (1, 31, 227, 200)],
    ["VER", "redbull", 2, (1, 31, 227, 200)],
    ["LAT", "williams", 10, (25, 95, 245, 200)],
    ["ALB", "williams", 10, (25, 95, 245, 200)]
]
def get_drivers_init():
    return sorted(drivers_init, key=lambda x: x[2], reverse=True)

import numpy as np

australia_track = [
    [[4, 3], [2, 4]],
    [[2, 0], [3, 4]],
    [[3, 0], [4, 1]],
    [[0, 1], [4, 2]],
    [[0, 2], [2, 0]],
    [[2, 4], [4, 2]],
    [[0, 2], [4, 3]],
    [[0, 3], [4, 3]],
    [[0, 3], [4, 1]],
    [[0, 1], [2, 0]],
    [[2, 4], [0, 1]],
    [[4, 1], [1, 0]],
    [[1, 4], [0, 3]],
    # start
    [[4, 3], [0, 3], 1],
    [[4, 3], [1, 4]],
    [[1, 0], [0, 1]],
    [[4, 1], [0, 1]],
    [[4, 1], [0, 3]],
]

