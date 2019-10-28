#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import ch2_p1

def main():
    f = lambda x: (x - 1.0) * (x - 2.0) * (x - 3.0)
    df = lambda x: (
        (x - 2.0) * (x - 3.0) +
        (x - 1.0) * (x - 3.0) +
        (x - 1.0) * (x - 2.0)
    )
    xs = [x / 100.0 for x in range(153, 157)]
    for x in xs:
        print(f'x = {x:.{2}f}')
        x, _ = ch2_p1.newton(f, df, x)
        print(f'    x = {x:.{6}f}')

if __name__ == '__main__':
    main()
