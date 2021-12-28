# test Fermata
# www.algorytm.org
#
# tested with Python 3.3

import random

def fermat(k, p):
    i = 0

    while i < k:
        a = random.randint(1, p - 1)
        if pow(a, (p - 1), p) == 1:
            i = i + 1
        else:
            return False

    return True