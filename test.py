from elgamal import elgamal
from signature import signature
from verification import verification
from attack import attack

def main():
    """
    DISTRIBUTE KEY
    """
    print "########## DISTRIBUTE KEY #################"
    # GIVE ALICE A KEY ... init with none key
    alice = elgamal()
    alice.create_key(10)
    # GIVE BOB KEY . .other  init with 10 bits key
    bob = elgamal(10)
    print "ALICE:\n", alice
    print "BOB:\n", bob
    print "################################"
    """
    END DISTRIBUTE KEY
    """
##########################################################################################################
    """
    ALICE'S TASK
    """
    print "########## ALICE's task ###########"
    # ALICE have a text
    text = "hello bob"
    print "TEXT: ", text
    # ALICE use public_key of BOB to encrypt that text
    cipher = bob.encrypt(text)
    #print "CIPHER: \n", cipher
    # give ALICE a pen
    alice_pen = signature(alice.private_key)
    #print alice_pen
    # create signature with ALICE's pen
    sig_of_alice = alice_pen.sign(text)
    #print "SIGNATURE: \n", sig
    ### alice send a pair contain cipher and her signature to bob
    pair = [cipher, sig_of_alice]
    print "PAIR[cipher, signature]: \n", pair    
    print "################################"
    """
    END ALICE'S TASK
    """
############################################################################################################
    """
    DARTH'S TASK
    """
    print "###### DARTH's task ###################"
    # DARTH have public_key of bob. He find private key
    darth = attack()
    k = darth.find_private_key(bob.public_key)
    print "DARTH found private key is: ", k
    pr = [bob.public_key[0], bob.public_key[1], k] # pr = [p, q, k]
    darth_crypto = elgamal()
    darth_crypto.set_key([],pr) ### darth only need private key to decrypt cipher
    print "Darth try to decrypt: ", darth_crypto.decrypt(pair[0])
    print "HAHAHAHAHAHAHA :)"
    print "################################"
    """
    DARTH'S TASK
    """
############################################################################################################
    """
    BOB'S TASK
    """
    print "########### BOB's task ###############"
    ###########bob receive the pair. bob take a accuracy of alice's signature
    ca_alice = verification(alice.public_key)
    t_text = bob.decrypt(cipher)
    print "BOB decrypt: ", t_text
    print "VERIFY: " ,ca_alice.verify(t_text,pair[1])
    """
    END BOB'S TASK
    """

if __name__ == "__main__":
    main()
