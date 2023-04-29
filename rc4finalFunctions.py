import sys
import pyRC4
 

def intToList(inputNumber):
    """Convert a number into a byte list"""
    inputString = "{:02x}".format(inputNumber)
    return [int(inputString[i:i + 2], 16) for i in range(0, len(inputString), 2)]

def string_to_list(inputString):
    """Convert a string into a byte list"""
    return [ord(c) for c in inputString]

def test(key, plaintext, ciphertext, testNumber):
    success = True
    pyRC4.setKey(string_to_list(key))

    try:
        encrypted = pyRC4.encrypt(plaintext) 
        assert encrypted == intToList(ciphertext)

        print('-----encrypt------')
        print(plaintext)
        print(encrypted)
        print(intToList(ciphertext))
        print(ciphertext)
        
        print('------------------')
        
        print("RC4 encryption test #{:d} ok!".format(testNumber))
    except AssertionError:
        print("RC4 encryption test #{:d} failed".format(testNumber))
        success = False


    #pyRC4.setKey(string_to_list(key))
    try:
        evt = pyRC4.encrypt(plaintext);

        decrypted =pyRC4.decrypt(intToList(ciphertext))
        print('-----decryp-------')
        print(ciphertext)
        print(intToList(ciphertext))
        print(decrypted)
        print('------------------')
        

        assert decrypted == plaintext
        print("RC4 decryption test #{:d} ok!".format(testNumber))
    except AssertionError:
        print("RC4 decryption test #{:d} failed".format(testNumber))
        success = False
    return success

 
# pyRC4.setKey(string_to_list('iii'))
# ciphertet = pyRC4.encrypt('Plaintext')
# pyRC4.setKey(string_to_list('iii'))
# plaintext = pyRC4.decrypt(ciphertet)

# print(ciphertet)
# print(plaintext)




    # pyRC4.setKey(string_to_list('111'))
    # ciphertet = pyRC4.encrypt('Plaintext');
    # ciphertet2 = pyRC4.encrypt('layth');


    # pyRC4.setKey(string_to_list('111'))
    # plaintext = pyRC4.decrypt(ciphertet)
    # laintext2 = pyRC4.decrypt(ciphertet2)

  

   
 
    
