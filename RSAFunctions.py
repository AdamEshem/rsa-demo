import math

"""Gets user input for prime numbers p and q

Assumes the user will enter prime numbers and doesn't check

returns: a list of the users two entered values [p, q]
"""
def get_primes():
    p = int(input('p value: '))
    q = int(input('q value: '))

    return [p, q]


"""Calculates the public key N value

Arguments:
    primes - the list containing p and q

returns: N value equal to q * p
"""
def calculate_N(primes):
    return primes[0] * primes[1]

def calculate_phi(primes):
    return (primes[0] - 1) * (primes[1] - 1)

def get_e(phi):
    e = int(input('Enter a value for e: '))

    while math.gcd(phi, e) != 1:
        print('e and phi are not co-prime')
        e = int(input('Enter a value for e: '))
    
    return e