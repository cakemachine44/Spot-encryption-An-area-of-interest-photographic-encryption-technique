import aes, os
key = os.urandom(16)
iv = os.urandom(16)
message = b'Attack at dawner';
message2 = b'Attack at daddddddwnedaddddddwnesdfsdgfgdsfgsfdrsdfsdgfgdsfgsfdr';


# print("EBC");
# encrypted = aes.AES(key).encrypt_block(message)
# print(aes.AES(key).decrypt_block (encrypted))


# print("CTR");

 #ciphertext = aes.AES(key).encrypt_ctr(message2, iv);
# print(aes.AES(key).decrypt_ctr(ciphertext,iv))


# print("CBC");
# ciphertext = aes.AES(key).encrypt_cbc(message2, iv);
# print(aes.AES(key).decrypt_cbc(ciphertext,iv))


   





# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

# message = b'aaaaaaaaaaaaaaaa' 

# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_CBC)
# ciphertext = cipher.encrypt(message)

# cipher2 = AES.new(key, AES.MODE_CBC)
# palintext = cipher2.decrypt(ciphertext)


# print(type(palintext));
# print(ciphertext);
# print(palintext );



# file_in = open("encrypted.bin", "rb")
# nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

# # let's assume that the key is somehow available again
# cipher = AES.new(key, AES.MODE_EAX, nonce)
# data = cipher.decrypt_and_verify(ciphertext, tag)
