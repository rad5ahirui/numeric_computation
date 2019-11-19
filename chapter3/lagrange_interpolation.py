#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def L(x, xs, ys):
    y = 0.0
    for i, (xi, yi) in enumerate(zip(xs, ys)):
        l = 1.0
        m = 1.0
        for j, xj in enumerate(xs):
            if j == i:
                continue
            l *= (x - xj)
            m *= (xi - xj)
        l *= yi
        l /= m
        y += l
    return y

def main():
    from matplotlib import pyplot as plt

    points_x = [0.5 + x for x in range(7)]
    points_y = [math.sin(0.5 + x) for x in points_x]

    xs = [x / 10 for x in range(70)]
    ys = [math.sin(0.5 + x) for x in xs]
    iy = [L(x, points_x, points_y) for x in xs]

    plt.plot(xs, ys, label="sin(0.5 + x)")
    plt.plot(xs, iy, label=f"Lagrange interpolation (N = {len(points_x) - 1})")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
