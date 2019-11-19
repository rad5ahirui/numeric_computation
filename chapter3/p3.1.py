#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from lagrange_interpolation import L

def main():
    from matplotlib import pyplot as plt

    points_x = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1.5, 2]]
    points_y = [[0, 0, 0], [0, 1, 2], [0, 1, 0], [0, 1, 0]]

    xs = [(x - 50) / 100 for x in range(300)]
    ys = [[L(x, px, py) for x in xs] for px, py in zip(points_x, points_y)]

    for i, y in enumerate(ys):
        plt.plot(xs, y, label=f"({i + 1})")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
