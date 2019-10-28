#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import ch2_p1

def main():
    f = lambda x: (x - 1.0) * (x - 2.0) * (x - 3.0)
    g = lambda x: -f(x)

    r = [[2.5, 1.5], [-2.0, 5.0]]
    for a, b in r:
        print(f'[{a}, {b}]:')
        if f(a) < 0 and f(b) > 0:
            h = f
        else:
            h = g
        x, _ = ch2_p1.bisect(f, a, b)
        print(f'    x = {x:.{6}f}')

if __name__ == '__main__':
    main()
