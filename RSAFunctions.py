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

def calculate_d(phi, e):
    return pow(e, -1, phi)

def breakup(m, blockSize):
    blocks = ['']
    counter = 0

    for i in m:
        if counter == blockSize:
            counter = 0
            blocks.append('')
        blocks[len(blocks) - 1] += i
        counter += 1
    return blocks

def encode(blocks):
    encoded = []
    count = 0
    for i in blocks:
        encoded.append(0)
        for j in range(len(i)):
            encoded[count] = encoded[count] | ord(i[j])
            if j < len(i) - 1:
                encoded[count] = encoded[count] << 8
        count += 1
    return encoded

def encrypt(m, e, n):
    for i in range(len(m)):
        m[i] = pow(m[i], e, n)
    return m

def decrypt(ct, d, n):
    for i in range(len(ct)):
        ct[i] = pow(ct[i], d, n)
    return ct

def decode(m):
    decoded = []
    for i in range(len(m)):
        decoded.append('')
        while m[i]:
            x = (m[i] & 0b11111111)
            m[i] = m[i] >> 8
            decoded[len(decoded) - 1] = chr(x) + decoded[len(decoded) - 1]
    return decoded

def listToString(list):
    message = ''
    return message.join(list)
