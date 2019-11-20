#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reference: Shamir, Adi (1979), "How to share a secret",
#            Communications of the ACM, 22 (11): 612-6,
#            doi:10.1145/359168.359176.

import math
import random
import functools

def generate_pieces(k, n, p):
    print(f'p = {p}')
    print(f'k = {k}')
    print(f'n = {n}')
    print()

    # D = a[0]
    print(f'Generating {k} coefficients...')
    a = [random.randrange(p) for i in range(k - 1)]
    # a[k - 1] != 0
    a.append(random.randrange(1, p))

    for i, e in enumerate(a):
        print(f'a[{i}]: {e}')
    print()
    print(f'Secret has been generated: D = a[0] = {a[0]}')
    print()
    print(f'Generating {n} pieces...')
    Di =  [(x, functools.reduce(lambda s, t: (s * x + t) % p, reversed(a)))
           for x in range(1, n + 1)]
    for i, (x, y) in enumerate(Di):
        print(f'D[{i + 1}] = ({x}, {y})')
    return Di

# Lagrange intereplation q(0) on a finite field Z/p
def q(p, xs, ys):
    y = 0
    for i, (xi, yi) in enumerate(zip(xs, ys)):
        l = 1
        m = 1
        for j, xj in enumerate(xs):
            if j == i:
                continue
            l *= p - xj
            l %= p
            m *= xi + (p - xj)
            m %= p
        l *= yi
        l %= p
        # We want to perform l /= m.
        # In order to do this, we need to find the inverse element of m.
        # Since p is prime, m and p are relatively prime,
        # and thus there exists an integer x such that
        #         mx \equiv 1 (mod p)
        # We can find x that is the inverse element of m which we want
        # by using Fermat's little theorem.
        x = pow(m, p - 2, p)
        l *= x
        l %= p
        y += l
        y %= p
    return y

def main():
    print("Shamir's Secret Sharing")
    print('A simple (k, n) Threshold Scheme based on polynomial interploation')
    print('on a finite field Z/p, where p is prime')
    print()
    # Prime number (2^127 - 1)
    p = 170141183460469231731687303715884105727
    # The number of given points
    k = 5
    # The number of pieces
    n = 6

    Di = generate_pieces(k, n, p)
    Dj = random.sample(Di, k)
    print()
    print(f'Get the secret from {k} pieces.')
    for i, (x, y) in enumerate(Dj):
        print(f'{i + 1}: ({x}, {y})')
    print()
    xs, ys = zip(*Dj)
    print(f'D = q(0) = {q(p, xs, ys)}')

if __name__ == '__main__':
    main()
