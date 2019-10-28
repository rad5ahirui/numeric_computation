#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

EPS = 1e-6

def bisect(f, a, b):
    n = 0
    while True:
        n += 1
        c = (a + b) / 2.0
        if abs(a - b) / 2.0 < EPS:
            break
        fc = f(c)
        if fc > EPS: # TODO: ちゃんとやる
            b = c
        elif fc < EPS:
            a = c
        else:
            break
    return c, n

def newton(f, df, a, b):
    n = 0
    x = (a + b) / 2.0
    while True:
        n += 1
        new_x = x - f(x) / df(x)
        if abs(new_x - x) < EPS * abs(new_x):
            break
        x = new_x
    return new_x, n

def main():
    fs = [
        lambda x: x * x - math.cos(x), # -f(x)
        lambda x: math.sin(x) - math.exp(-x * x)
    ]
    dfs = [
        lambda x: 2.0 * x + math.sin(x), # -f'(x)
        lambda x: math.cos(x) + 2.0 * x * math.exp(-x * x)
    ]
    for i, (f, df) in enumerate(zip(fs, dfs)):
        print(f'({i + 1})')
        print('Bisection method:')
        x, n = bisect(f, 0, 1)
        print(f'            x = {x:.{6}f}')
        print(f'    iteration = {n}')
        x, n = newton(f, df, 0, 1)
        print("Newton's method:")
        print(f'            x = {x:.{6}f}')
        print(f'    iteration = {n}')


if __name__ == '__main__':
    main()
