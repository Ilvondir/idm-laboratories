from math import sqrt
def is_prime(a):
    prime = True
    for x in range(2, round(sqrt(a)) + 1):
        if a % x == 0:
            prime = False
            break
    return prime