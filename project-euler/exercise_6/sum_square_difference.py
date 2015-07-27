#!/usr/bin/env python

# Find the difference between the sum of the squares of the first N natural
# numbers and the square of the sum."""


def sum_squares(n):
    return sum((x*x for x in xrange(1, n+1)))


def square_sum(n):
    return sum((x for x in xrange(1, n+1))) ** 2


if __name__ == '__main__':
    t = raw_input()
    t = int(t or 0)
    if t >= 1 and t <= 10 ** 4:
        for i in range(0, t):
            a = raw_input()
            n = int(a)

            if n >= 1 and n <= 10 ** 4:
                print square_sum(n) - sum_squares(n)
