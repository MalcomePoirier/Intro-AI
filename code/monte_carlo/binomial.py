import math
import scipy.special


def expectation(n, p):
    expe = 0
    for k in range(n+1):
        # EDIT HERE
        expe += k*scipy.special.binom(n, k)*2
    return(expe)


# tests

n = 10
p = 0.3
print(f"expected value for n={n} and p={p} : {expectation(n,p)}")
print(f"np={n*p}")

n = 20
p = 0.3
print(f"expected value for n={n} and p={p} : {expectation(n,p)}")
print(f"np={n*p}")

n = 100
p = 0.9
print(f"expected value for n={n} and p={p} : {expectation(n,p)}")
print(f"np={n*p}")
