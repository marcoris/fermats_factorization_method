#!/usr/bin/env python3

from Crypto.PublicKey import RSA

from gmpy2 import isqrt, invert, lcm

def factorize(n):
    # since even nos. are always divisible by 2, one of the factors will
    # always be 2
    if (n & 1) == 0:
        return (n/2, 2)

    # isqrt returns the integer square root of n
    a = isqrt(n)

    # if n is a perfect square the factors will be ( sqrt(n), sqrt(n) )
    if a * a == n:
        return a, a

    while True:
        a = a + 1
        bsq = a * a - n
        b = isqrt(bsq)
        if b * b == bsq:
            break

    return a + b, a - b


def get_private_key(e, p, q):
    return invert(e, lcm(p - 1, q - 1))



with open('id_rsa.pub', 'r') as file:
    public_key = key = RSA.import_key(file.read())

n = key.n
e = key.e

bit_size = public_key.size_in_bits()

x = str(n)[-10:]

p, q = factorize(n)

d = get_private_key(e, p, q)

private_key = RSA.construct((n ,e , int(d)))

with open('id_rsa', 'wb') as file:
    file.write(private_key.export_key('PEM'))

print(f"The size in bits of the public key is: {bit_size}")
print()
print(f"The last 10 digits of the public key are: {x}")
print()
print(f"The difference between p and q is: {p - q}")
print()
print(f"Primenumber of p is: {p}")
print()
print(f"Primenumber of q is: {q}")
print()
print(f"n is: {n}")
print()
print(f"e is: {e}")
print()
print(f"The value of the private key is {d}")
print()
print("You can find your key in this directory.")
