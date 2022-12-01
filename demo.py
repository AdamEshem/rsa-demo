from RSAFunctions import *

print('Select Mode')
print('1. Presentation Mode')
print('2. Experimental Mode')
mode = int(input())

if mode == 1:
    print()
    print('First off we need two (preferably large) prime numbers p and q')
    primes = get_primes()

    print()
    print('We use these values to calculate N by multiplying p and q')
    input()
    print('N = 7741 * 7753')
    print('N = 60,015,973')
    input()
    n = calculate_N(primes)

    print("Using p and q we also need to calculate our phi value (Euler's Totient)")
    input()
    print('phi = (p - 1) * (q - 1)')
    input()
    print('phi = (7741 - 1) * (7753 - 1)')
    print('phi = (7740) * (7752)')
    print('phi = 60,000,480')
    input()
    phi = calculate_phi(primes)

    print('Now we choose our e value for the second part of our public key')
    print('Can really pick any value as long as e is co-prime with phi, and less than N')
    e = get_e(phi)

    print()
    print('We now have our complete public key made up of our N value and e value')
    input()

    print("When we decrypt our message the last operation we'll use is mod N")
    input()
    print('So if the message being encrypted were to have more bits than N, data would be lost')
    input()
    print('In our current example, the bit length of N is 26')
    print('Since each ASCII character is 8 bits, we can encipher a max of 3 characters at a time')
    input()
    blockSize = int.bit_length(n) // 8

    m = input('Enter message: ')

    blocks = breakup(m, blockSize)

    print(blocks)
    print()
    print("As you can see here, we've broken down our whole message into manageable blocks")
    input()

    print('Next we encode the message')
    print('This is done by concatenating all the binary ASCII values of each block into one binary value we treat as a single decimal')
    input()
    print('In this case the first block to be encoded contains (Whe)')
    print('W = 0b01010111')
    print('h = 0b01101000')
    print('e = 0b01100101')
    input()
    print('Put together 0b010101110110100001100101 is equivalent to 5,728,357')
    print()
    encoded = encode(blocks)

    print(encoded)

    print()
    input()
    print('Next up is to encrypt our coded representation')
    print('This is done using the equation C = (M ** e) % N')
    input()
    print('Using our example from above of the first block')
    print('C = (5,728,357 ** 11) % 60,015,973')
    print('C = 43,995,402')
    input()
    encrypted = encrypt(encoded, e, n)
    print(encrypted)

    print()
    input()
    print('At this point if you intercepted the message you could decode it and put it back together and get this')
    copy = encrypted.copy()
    print(listToString(decode(copy)))
    input()
    
    print('In order to retrieve the original message, you now need the private decryption key')
    print('In order to get that you need to solve: e * d = 1 (% phi)')
    input()
    print("We already have some of these values so we'll plug them in")
    print('11 * d = 1 (% 60,000,480)')
    print("Now we just have to solve for d, but it's not as straight forward as it seems")
    input()
    print('That is a linear congruence, whose solution is a modular multiplicative inverse')
    print('Thankfully there is the Extended Euclidean Algorithm to help find the solution')
    d = calculate_d(phi, e)
    print()

    print('Using that algorithm, we are able to calculate our decryption key value which is: e = 54545891')
    print()

    print('Now with d calculated, we can retrieve the original message')
    print('We just need to solve for M in the equation M = (C ** d) % N')
    input()
    decrypted = decrypt(encrypted, d, n)
    print(decrypted)
    print()
    print("If this looks familiar, it's because it was our encoded list of blocks from earlier")
    print('That leads us to our final step of decoding the message and combining it back to its original form')
    input()
    decoded = decode(decrypted)
    print(decoded)
    input()
    print(listToString(decoded))

if mode == 2:
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