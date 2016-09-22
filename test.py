from elgamal import elgamal
from signature import signature
from verification import verification


######## give keys to alice, bob################
alice = elgamal()
alice.create_key(10)

bob = elgamal(10)
#print alice
#print bob
######### alice have a text #######
text = "hello bob"

### alice encrypt this text then send to bob
cipher = bob.encrypt(text)
#print "CIPHER: \n", cipher

### give alice a pen
alice_pen = signature(alice.private_key)
#print alice_pen
sig = alice_pen.sign(text)
#print "SIGNATURE: \n", sig

### alice send a pair contain cipher and her signature to bob
pair = [cipher, sig]

###########bob receive the pair. bob take a accuracy of alice's signature
ca_alice = verification(alice.public_key)
t_text = bob.decrypt(cipher)
print "TEXT: ", t_text
print "VERIFY: " ,ca_alice.verify(t_text,pair[1])
