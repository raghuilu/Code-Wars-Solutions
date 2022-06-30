import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def step(g, m, n):
    primes = []
    for i in range(m, n):
        iprime = isPrime(i)
        primes.append(iprime)
        if iprime:
            if len(primes) > g:
                if primes[i-g-m]:
                    return [i-g, i]