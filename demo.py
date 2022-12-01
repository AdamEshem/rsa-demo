from RSAFunctions import *


primes = get_primes()

n = calculate_N(primes)

phi = calculate_phi(primes)

e = get_e(phi)

d = calculate_d(phi, e)

print(d)

blockSize = int.bit_length(n) // 8

m = input('Enter secret message: ')

blocks = breakup(m, blockSize)

encoded = encode(blocks)

encrypted = encrypt(encoded, e, n)

decrypted = decrypt(encrypted, d, n)

decoded = decode(decrypted)
print(decoded)
print(listToString(decoded))