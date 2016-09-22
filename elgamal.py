import random


"""
Class Elgamal
_________
attributes:
    + private_key [p, q, k]
    + public_key [p, q, d]
methods:
    + create_key(bits)
    + encrypt(text)
    + decrypt(cipher)
"""
class elgamal:
    def __init__(self, bits=30):
        # size : number of digits of key
        self.create_key(30)

    def __str__(self):
        return "public key: %s\nprivate key: %s" % (self.public_key, self.private_key)

    ##############
    def create_key(self,bits=30):
        p = get_prime(bits)
        q = random.randint(1,p-1)
        k = random.randint(2,p-2)
        d = pow(q,k,p)

        self.public_key = [p, q, d]
        self.private_key = [p, q, k]

    ###############
    def encrypt(self, text):
        p, q, d = self.public_key[0], self.public_key[1], self.public_key[2]

        blockSize = p.bit_length() / 8
        arrayPlainTextNumber = []
        for i in xrange( len(text)/ blockSize + 1):
            arrayPlainTextNumber.append(textToNum(text[:blockSize]))
            text = text[blockSize:]

        c1, c2 = [], []
        for i in arrayPlainTextNumber:
            k1 = random.randrange(2, p - 2)
            c1.append(pow(q,k1,p))
            c2.append((pow(d,k1,p)*i)%p)   
        return c1,c2

    ################
    def decrypt(self,cipher):
        p, k = self.private_key[0], self.private_key[2]
        c1, c2 = cipher[0], cipher[1]
        text = ""
        for i in xrange(len(c1)):
            decryptedNumber = ( pow(c1[i], p-1-k, p) * c2[i]) % p
            text += numToText(decryptedNumber)
        return text



"""
BEGIN TEMP FUNCTIONS
"""

def isPrime(n, times = 50):
    if n < 5:
        if n in [2, 3]:
            return True
        else:
            return False
    if (n & 1 != 0):

        # Miller-Rabbin
        # n - 1 = 2 ^ s * m
        m, s = n - 1, 0
        while m & 1 == 0:
            m, s = m >> 1, s + 1
        # Loop k time (error bound 4 ^ -k)
        for i in xrange(times):
            a = random.randint(2, n - 2)
            if not strong_pseudoprime(n, a, s, m):
                return False
        return True


def strong_pseudoprime(n, a, s, m):
    # Odd composite number n = m * 2 ^ s + 1 is called a strong (Fermat) pseudoprime when one of the following conditions holds:
    #   a ^ m % n = 1
    # or a ^ (d * 2 ^ r) = n - 1 for 0 <= r < s
    b = pow(a, m, n)
    if b == 1:
        return True
    for i in xrange(s):
        if b == n - 1:
            return True
        b = b * b % n

    return False


def get_prime(k):
    # Random number then check primality
    if k <=1:
        return None
    n = random.randint(2**(k-1), 2**k - 1)
    while not isPrime(n):
        n = random.randint(2**(k-1), 2**k - 1)
    return n


#print get_prime(30)
###############################3
#############  convert####################
def textToNum(textString):
#ASCII as base 256 number
    number = 0
    for character in textString:
        number = (number << 8) + ord(character)
    return number

def numToText(number):
#ASCII as base 256 number
    textString = ''
    while number:
        textString = chr(number % 256) + textString
        number >>= 8
    return textString


###########################################
##########################################
"""
END TEMP FUNCTIONS
"""


def main():
    bob = elgamal()
    bob.create_key(8)
    #print bob.public_key
    text = "hello"
    
    cipher = bob.encrypt(text)
    print cipher
    
    de_text = bob.decrypt(cipher)
    print de_text

if __name__ == '__main__':
    main()




