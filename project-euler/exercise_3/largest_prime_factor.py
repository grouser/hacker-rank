#!/usr/bin/env python

"""What is the largest prime factor of a given number N?"""


def largest_prime(n):
    i = 2
    # stop when a square number is higher than n to avoid useless iterations
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n = n / i
    return n


if __name__ == '__main__':
    t = raw_input()
    t = int(t or 0)
    if t >= 1 and t <= 10:
        for i in range(0, t):
            a = raw_input()
            n = int(a)

            if n >= 10 and n <= pow(10, 12):
                print largest_prime(n)
