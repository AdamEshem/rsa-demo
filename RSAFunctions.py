"""Gets user input for prime numbers p and q

Assumes the user will enter prime numbers and doesn't check

returns: a list of the users two entered values [p, q]
"""
def get_primes():
    p = input('p value: ')
    q = input('q value: ')

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