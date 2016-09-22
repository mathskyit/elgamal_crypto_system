import random
import hashlib
from fractions import gcd

"""
MAIN CLASS
"""

class signature:

    def __init__(self,key=[]):
        self.private_key = key

    def __str__(self):
        return "PEN's key is %s" % (self.private_key)

    def set_key(self,key=[]):
        self.private_key = key

    def sign(self, text):
        p, q, k = self.private_key[0], self.private_key[1], self.private_key[2] 
        H = int(hashlib.md5(text).hexdigest(), 16)

        s = 0
        while s == 0:
            while True:                
                t = random.randint(1, p - 1)
                if gcd(t, p-1) == 1:
                    break
                
            r = pow(q, t, p)
            it = modular_inverse(t, p - 1)          
            s = (H - k*r)*it % (p - 1)

        return r, s



################
"""
BEGIN TEMP FUNCTIONS
"""
################
"""
def gcd(a, b):
    while b!= 0:
        a, b = b, a%b
    return a
"""

def modular_inverse(a, n):
    """
    at = 1 mod n . .. find t
    at + ns = 1
    a = a.1 + n.0
    n = a.0 + n.1
    """
    n0 = n
    t0, s0 = 1, 0
    t1, s1 = 0, 1
    while n != 0:
        q = a / n
        a, n = n, a%n
        t0, t1 = t1, t0 - q*t1
        s0, s1 = s1, s0 - q*s1
    if t0 < 0:
        return t0 + n0
    return t0
###################################
"""
END TEMP FUNCTIONS
"""



def main():
    #########  alice job ######
    pen = signature()
    print pen
    
    


if __name__ == '__main__':
    main()
