import random
import hashlib


class verification:
    def __init__(self, key = []):
        self.public_key = key

    def __str__(self):
        return "CA' key is %s" % (self.public_key)

    def set_key(key):
        self.public_key = key

    def verify(self,text, signature):
        H = int(hashlib.md5(text).hexdigest(),16)
        r, s = signature[0], signature[1]
        p, q, d = self.public_key[0], self.public_key[1], self.public_key[2]

        a = pow(q,H,p)
        b = pow(d,r,p)*pow(r,s,p) % p
        
        if a == b:
            return True
        else:
            return False
    

def main():
    ca = verification()
    print ca

if __name__ == '__main__':
    main()

