import random
import math

def generate_primes():
    """
    Generate prime numbers using the Sieve of Eratosthenes method
    """
    sieve = [True] * 250
    sieve[0] = False
    sieve[1] = False

    for i in range(2, 250):
        for j in range(i * 2, 250, i):
            sieve[j] = False

    primes = set()
    for i in range(len(sieve)):
        if sieve[i]:
            primes.add(i)

    return primes

def generate_random_prime(primes):
    """
    Select a random prime number and remove it from the set
    """
    k = random.randint(0, len(primes) - 1)
    it = iter(primes)
    for _ in range(k):
        next(it)

    prime_num = next(it)
    primes.remove(prime_num)

    return prime_num

def generate_keys():
    """
    Generate public and private keys using random prime numbers
    """
    primes = generate_primes()

    prime1 = generate_random_prime(primes)
    prime2 = generate_random_prime(primes)

    n = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)

    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1

    public_key = e

    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1

    private_key = d

    return ((public_key, n), (private_key, n))

def encrypt_plaintext(msg_plaintext, public_key):
    """
    Encrypt a given text using the public key
    """
    e, n = public_key

    # pow(x, y, z): x is the base, y is the exponent and z the modulus
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    
    return msg_ciphertext


def decrypt_ciphertext(msg_ciphertext, private_key):
    """
    Decrypt a given ciphertext using the private key
    """
    d, n = private_key

    # pow(x, y, z): x is the base, y is the exponent and z the modulus
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]

    return (''.join(msg_plaintext))


# Testing the RSA Algorithm

# public, private = generate_keys()

# print("Public Key: ", public)
# print("Private Key: ", private)

# msg = input("Write your message: ")
# print([ord(c) for c in msg])

# encrypted_msg = encrypt_plaintext(msg, public)
# print("Encrypted Message: " + ''.join(map(lambda x: str(x), encrypted_msg)))

# print(f"Decrypted Message : {decrypt_ciphertext(encrypted_msg, private)}")
