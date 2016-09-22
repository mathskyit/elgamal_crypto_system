import math
import time

class attack:
    def __init__(self):
        return
    def find_private_key(self, pub_key):
        p, q, d = pub_key[0], pub_key[1], pub_key[2]
        return shank(p, q, d)

"""
BEGIN TEMP FUNCTION
"""
def shank(p, q, d): 
    """
    d = q^x mod p .....    find x
    x = im + j ... m = sqrt(p)
    d*q^-m^i = q^j mod p 
    """
    
    m = int(math.sqrt(p)) + 1
    table = {}

    #baby steps
    for j in xrange(0,m):
        table[pow(q,j,p)] = j

    #giant steps
    beta = pow(modular_inverse(q, p), m, p)
    for i in xrange(1,m):
        d = d*beta % p
        if d in table:
            return i*m + table[d]

def modular_inverse(a, n):
    """
    at = 1 mod n ... gcd(a, n) = 1
    .. find t
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
"""
END TEMP FUNCTION
"""


def main():

    begin = time.time()
    #51751742255297
    print shank(182806019700907, 7253258872651, 48982943472108)
    print time.time() - begin
    
if __name__ == "__main__":
    main()







