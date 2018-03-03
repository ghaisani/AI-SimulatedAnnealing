import math
import random

# Initial State
x1 = random.uniform(-10, 10)
x2 = random.uniform(-10, 10)
fs = ((4 - (2.1 * (x1 ** 2)) + ((x1 ** 4) / 3))*(x1 ** 2)) + (x1 * x2) + ((-4 + (4 * (x2 ** 2))) * (x2 ** 2))

# inisialisasi IS, CS, BSF dan T
InS = fs
CS = InS
BSF = CS
T = 0.001
i = 1
while (i <= 100000):
    x1 = random.uniform(-10, 10)
    x2 = random.uniform(-10, 10)
    NS = ((4 - (2.1 * (x1 ** 2)) + ((x1 ** 4) / 3))*(x1 ** 2)) + (x1 * x2) + ((-4 + (4 * (x2 ** 2))) * (x2 ** 2))
    E = NS - CS

    if (E < 0):
        CS = NS
        BSF = NS
    else:
        PE = math.exp(-E / T)
        BilRan = random.random() * 1
        if (PE > BilRan):
            CS = NS
    i = i + 1
print "BSF : " + str(BSF)