#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import ch2_p1

def main():
    f = lambda x: (x - 1.0) * (x - 2.0) * (x - 2.0)
    df = lambda x: (x - 2.0) * (x - 2.0) + 2 * (x - 1.0) * (x - 2.0)
    xs = [0.0, 3.0]
    for x in xs:
        print(f'x_0 = {x:.{2}f}')
        x, n = ch2_p1.newton(f, df, x)
        print(f'            x = {x:.{6}f}')
        print(f'    iteration = {n}')

if __name__ == '__main__':
    main()
