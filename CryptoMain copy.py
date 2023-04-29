from PIL import Image
from PIL import ImageFilter
import numpy as np
from io import BytesIO
import random
np.set_printoptions(threshold=np.inf)
import final_aes as Laes
import rc4finalFunctions as LRc4
import os
import sys
import time
import math
import base64
import zlib
message = b'Attack at dawner';
message2 = b'Attack at daddddddwnedaddddddwnesdfsdgfgdsfgsfdrsdfsdgfgdsfgsfdr';
# key = os.urandom(16)
#iv = os.urandom(16)
rc4key = 'eeeeeeee'


key = [2, 3, 5, 7 , 2, 3, 5, 7, 2, 3, 5, 7 ,2, 3, 5, 7]
key = bytearray(key)

iv = [2, 3, 5, 7 , 2, 3, 5, 7, 2, 3, 5, 7 ,2, 3, 5, 7]
iv = bytearray(iv)



def RC4REncrypt(flatImage,w, h ,buildImage = False ):
    start_time = time.time()
    LRc4.pyRC4.setKey(LRc4.string_to_list(rc4key))
    cipherImage = LRc4.pyRC4.encrypt(flatImage);

    print("RC4 Encrypt time --- %s seconds ---" % (time.time() - start_time))

    if buildImage : 
        newCipherImage = np.array(cipherImage).reshape(h,w,3);
        pil_image=Image.fromarray((newCipherImage).astype(np.uint8))
        pil_image.save("RC4_Encrypted.jpg")
        pil_image.show()
    return cipherImage
    
    


def RC4RDecrypt(flatImage,w, h ,buildImage  = False):
    start_time = time.time()
    LRc4.pyRC4.setKey(LRc4.string_to_list(rc4key))

    plainImage = LRc4.pyRC4.decrypt(flatImage)
    plainImage = [ord(c) for c in plainImage]

    print("RC4 Decrypt time --- %s seconds ---" % (time.time() - start_time))

    if buildImage : 
        newPlainImage = np.array(plainImage).reshape(h,w,3);
        pil_image=Image.fromarray((newPlainImage).astype(np.uint8))
        pil_image.save("RC4_Decrypted.jpg")
        pil_image.show()
    return plainImage

def aesCTREncrypt(flatImage,buildImage  = False):
    start_time = time.time()
    cipherImage = Laes.aes.AES(key).encrypt_ctr(flatImage, iv);
    cipherImage = [x for x in cipherImage]

    print("AES CTR Encrypt --- %s seconds ---" % (time.time() - start_time))

    if buildImage : 
        newCipherImage = np.array(cipherImage).reshape(height,width,3);
        pil_image=Image.fromarray((newCipherImage).astype(np.uint8))
        pil_image.save("AES_CTR_Encrypted.jpg")
        pil_image.show()

    return cipherImage



def aesCTRDecrypt(flatImage,buildImage):
    start_time = time.time()
    bytepixels =b''.join( [ x.to_bytes(1, 'big') for x in flatImage ] ) 
    plainImage =  Laes.aes.AES(key).decrypt_ctr(bytepixels,iv)
    plainImage = [x for x in plainImage]

    print("AES CTR Decrypt time --- %s seconds ---" % (time.time() - start_time))

    if buildImage : 
        newPlainImage = np.array(plainImage).reshape(height,width,3);
        pil_image=Image.fromarray((newPlainImage).astype(np.uint8))
        pil_image.save("AES_CTR_Decrypted.jpg")
        pil_image.show()

    return plainImage


def aesECBEecrypt(flatImageSplittedWithPadding,buildImage  = False ):
    start_time = time.time()
    CipherImage = [ Laes.aes.AES(key).encrypt_block(x) for x in  flatImageSplittedWithPadding  ] 
    CipherImage = b''.join(CipherImage)
    CipherImage = [x for x in CipherImage]

    print("AES ECB Encrypt time --- %s seconds ---" % (time.time() - start_time))

    if buildImage : 
        lenght = width * height * 3
        newCipherImage = CipherImage[:lenght]
        newCipherImage = np.array(newCipherImage).reshape(height,width,3);
        pil_image=Image.fromarray((newCipherImage).astype(np.uint8))
        pil_image.save("AES_ECBE_Encrypted.jpg")
        pil_image.show()
    
    return CipherImage



def aesECBDecrypt(flatImageSplitted,buildImage  = False):
    start_time = time.time()
    plainImage = [ Laes.aes.AES(key).decrypt_block(x) for x in  flatImageSplitted  ] 
    plainImage = b''.join(plainImage)
    plainImage = [x for x in plainImage]

    print("AES ECB Decrypt time --- %s seconds ---" % (time.time() - start_time))


    if buildImage :
        lenght = width * height * 3
        newPlainImage = plainImage[:lenght]
        newPlainImage = np.array(newPlainImage).reshape(height,width,3);
        pil_image=Image.fromarray((newPlainImage).astype(np.uint8))
        pil_image.save("AES_ECBE_Decrypted.jpg")
        pil_image.show()
    
    return plainImage


def aesCBCEncrypt(flatImage,w,h,buildImage  = False):
    start_time = time.time()
    cipherImage = Laes.aes.AES(key).encrypt_cbc(flatImage, iv);
    cipherImage = [x for x in cipherImage]
    cipherImage = np.array(cipherImage)

    print("AES CBC Encrypt --- %s seconds ---" % (time.time() - start_time))

    if buildImage : 

        lenght = w * h * 3
        newCipherImage = cipherImage[:lenght]
        newCipherImage = np.array(newCipherImage).reshape(h,w,3);
        pil_image=Image.fromarray((newCipherImage).astype(np.uint8))
        pil_image.save("AES_CBC_Encrypted.jpg")
        pil_image.show()

    return cipherImage

def aesCBCDecrypt(flatImage,buildImage  = False ):
    start_time = time.time()
    # bytepixels =b''.join( [ x.to_bytes(1, 'big') for x in flatImage ] ) 
    plainImage =  Laes.aes.AES(key).decrypt_cbc(flatImage,iv)
    plainImage = [x for x in plainImage]
    plainImage = np.array(plainImage).astype(np.uint8) 
    print("AES CBC Decrypt time --- %s seconds ---" % (time.time() - start_time))

    if buildImage : 
        newPlainImage = np.array(plainImage).reshape(height,width,3);
        pil_image=Image.fromarray((newPlainImage).astype(np.uint8))
        pil_image.save("AES_CBC_Decrypted.jpg")
        pil_image.show()

    return plainImage


def spllitAddPadding(FlatImage, splitfactor,addRemove):

    splitedSize = splitfactor
    a_splited = [FlatImage[x:x+splitedSize] for x in range(0, len(FlatImage), splitedSize)]

    if addRemove == 'add':
        lastBlock = int( math.ceil(len(FlatImage) / splitedSize) -1 )
        lenOflastarray = len(a_splited[lastBlock])
        # print(type(a_splited[lastBlock]))
        # print(a_splited[lastBlock])
        # print(lenOflastarray)
        # print(len(a_splited[lastBlock]))
        if len(a_splited[lastBlock]) < splitedSize : 
            #print(splitedSize  - len(a_splited[last]))
            for x in range(lenOflastarray, splitedSize):  
                a_splited[lastBlock] =  np.append(a_splited[lastBlock], 0 )
            
            a_splited[lastBlock] = a_splited[lastBlock].tolist()
            # print(a_splited[lastBlock])
        

    if addRemove == 'remove':   
        leng =    width * height * 1 
        a_splited = a_splited [0:leng]
        a_splited = np.concatenate(a_splited).tolist()
    
    return a_splited 

def AddErrorToFlatImage(flatImage,prob,buildImage = False):
    imageInBinary =[np.binary_repr(i, width=8) for i in flatImage]
    imageWithError =[byteErrorWithProb(i,prob) for i in imageInBinary]
    imageWithError_int =[int(i, 2)for i in imageWithError]

    if buildImage : 
        newCipherImage = np.array(imageWithError_int).reshape(height,width,3);
        pil_image=Image.fromarray((newCipherImage).astype(np.uint8))
        pil_image.save("ImageWithError.jpg")
        pil_image.show()

    return imageWithError_int


def byteErrorWithProb(correctByte,probability):
    error = "" 
    for i in range(8):
       # print(correctByte[i]);
        n = random.random()
        #print(n)
        if (n < probability):
            n2 = random.random()
            if n2 > 0.5:
                error = error + '1'
            else:
                error = error + '0'

        else :
            error =  error + '0'


    newDecimal = int(correctByte,2) ^ int(error,2);
    newByte = np.binary_repr(newDecimal, width=8)
    return newByte; 

    

def losslessImageCompress (flatImage):

    print("Orginal Image size : %s " % (len(flatImage) ) ) 

    imageBytes = flatImage.tobytes()
    compressed = zlib.compress(imageBytes , 6)

    compressedInt = np.array( np.frombuffer(compressed, dtype='uint8'))

    print("Compressed Image size : %s " % (len(compressedInt) ) ) 

    # print(compressedInt[:20])
    return (compressedInt)


def losslessImageUncompress (flatImage,w,h,buildImage = False):
    print("Compressed Image size : %s " % (len(flatImage) ) ) 
    
    imageBytes2 = flatImage.tobytes()
    Decompressed = zlib.decompress(imageBytes2)

    DecompressedInt = np.array( np.frombuffer(Decompressed, dtype='uint8'))
    print("Orginal Image size : %s " % (len(DecompressedInt) ) ) 
    # print(DecompressedInt[:20])

    if buildImage : 
        newCipherImage = np.array(DecompressedInt).reshape(h,w,3);
        pil_image=Image.fromarray((newCipherImage).astype(np.uint8))
        pil_image.save("Image_after_losslessImageDeCompress.jpg")
        pil_image.show()

    return DecompressedInt

def lossCompress (Image,CompresionRatio,buildImage):

    imgSmall = Image.resize((int(width * ((100 -CompresionRatio)/100) ) , int(height * ((100 - CompresionRatio)/100))))

    if buildImage : 
        pil_image = imgSmall
        pil_image.save("Image_after_losslessImageCompress.jpg")
        pil_image.show()

    return imgSmall

def lossUnCompress (Image2,size, buildImage =False):
    result = Image2.resize(size,Image.NEAREST)
    if buildImage : 
        pil_image = result
        pil_image.save("Image_after_lossUnCompress.jpg")
        pil_image.show()

    return result

def myround(x, base=16):
    dd = math.floor(x/base)

    # print('dd before')
    # print(dd)

    dd = 1 if dd < 1  else  dd
    # print('dd')
    # print(dd)

    # print('x % base')
    # print(x % base)
    if x < base:
        x = 0
    else:
        x = 1 if ( x % base ) > 0  else 0



    return ((base * dd) + (base * x )) 

  
def fourdigits(s):
    lenF = len(s)

    loops = 4 - lenF; 

    for x in range(0, loops):
        s = '0'+ s


    return s 

def intArray2stringArrayRep (arrayInt):
    string_ints = [str(int) for int in arrayInt]
    F_string_ints = [fourdigits (st) for st in string_ints]
    F_string_ints = bytes("".join(F_string_ints), 'utf-8') 

    # print(F_string_ints)
    return F_string_ints

def stringArrayRep2intArray (arrayString):
    string_ints = [chr(e) for e in arrayString]
    a_splited = [ int("".join(string_ints[x:x+4])) for x in range(0, len(string_ints), 4)]

    return a_splited




im = Image.open('yolo.jpg');
im.show()

Naoi = 1
CompresionR = 60

p= 0.0

width, height = im.size

image_array = np.array(im)
imageFlat = image_array.reshape(-1)


bbox = [160, 200, 206, 290]
aoi = im.crop(bbox)
background = im.copy() ;
background.paste( (200,200,200), bbox )

# im.show()
# aoi.show()
# background.show()

H_noi = np.array([])
Header = np.array([])
Body = np.array([])
All_packet  = np.array([] , np.uint8)


H_noi =  np.append (H_noi ,Naoi ) .astype(np.uint16) 

Header= np.append (Header ,[width, height , CompresionR] )
Header= np.append (Header ,bbox ).astype(np.uint16) 


Header_string = intArray2stringArrayRep(Header)
H_noi_string  = intArray2stringArrayRep(H_noi)



Heade_AES_CBC = aesCBCEncrypt(Header_string,1,1,False)
H_noi_AES_CBC = aesCBCEncrypt(H_noi_string,1,1,False)

print("background lossCompress:  ")
background_Lcompressed = np.array(              lossCompress(background ,CompresionR ,  False)                 ).reshape(-1)
background_Lcompressed_width, background_Lcompressed_height = int (width*((100- CompresionR)/100) ) , int (height*((100- CompresionR)/100) )


print("background RC4REncrypt:  ")
background_Lcompressed_RC4_Enc = RC4REncrypt(background_Lcompressed, background_Lcompressed_width ,  background_Lcompressed_height,  buildImage = False )


Body= np.append (  Body ,background_Lcompressed_RC4_Enc ) 
aoiFlat = np.array(aoi).reshape(-1)


aoi_width, aoi_height = aoi.size



print("aoi losslessImageCompress:  ")
aoi_S_LLcompressed = losslessImageCompress(aoiFlat )

print("aoi aesCBCEncrypt:  ")
aoi_S_LLcompressed_AES_CBC = aesCBCEncrypt(aoi_S_LLcompressed, aoi_width , aoi_height ,False)


Body= np.append ( Body ,aoi_S_LLcompressed_AES_CBC ) .astype(np.uint8) 

All_packet = np.append (All_packet, H_noi_AES_CBC ).astype(np.uint8) 

All_packet = np.append (All_packet, Heade_AES_CBC  ).astype(np.uint8) 

All_packet_S = np.append (All_packet, Body  ).astype(np.uint8) 



All_packet_R = All_packet_S    # send from sender to reciver/ maybe add error  / key exchange 



print("")
print("")
print("")

print("Size of Transferred Packet: ")
print(len(All_packet_R))

print("")
print("")
print("")






pinter = 0

R_noi_encrypted = np.array(All_packet_R[0:16]).astype(np.uint8) 
pinter = pinter + 16 
RH_noi_AES_CBC = aesCBCDecrypt(R_noi_encrypted  ,False)
RH_noi_splited = stringArrayRep2intArray(RH_noi_AES_CBC)



Header_len = ( (RH_noi_splited[0] * 4) + (3) ) * 4

Enc_Header_len = myround(Header_len, base=16) 

R_Header_encrypted = All_packet_R[pinter:pinter+Enc_Header_len].astype(np.uint8) 

pinter = pinter+Enc_Header_len 

R_Heade = aesCBCDecrypt(R_Header_encrypted  ,False)
R_Heade_splited = stringArrayRep2intArray(R_Heade)




R_Image_width = R_Heade_splited[0]
R_Image_height = R_Heade_splited[1]
R_CompresionR = R_Heade_splited[2]
CRR = (100 - R_CompresionR)/100


R_Compressed_background_width = int (R_Image_width * CRR)
R_Compressed_background_height = int (R_Image_height * CRR)

background_array_len = (R_Compressed_background_width * R_Compressed_background_height * 3)



R_background_Compressed_encrypted = np.array(All_packet_R[pinter:pinter+background_array_len]).astype(np.uint8) 
pinter =pinter+background_array_len



R_background_Compressed = RC4RDecrypt (R_background_Compressed_encrypted ,R_Compressed_background_width, R_Compressed_background_height,  buildImage = False )

R_background_Compressed_2d = np.array(R_background_Compressed).reshape(R_Compressed_background_height,R_Compressed_background_width,3);
R_background_Compressed_2d =Image.fromarray((R_background_Compressed_2d).astype(np.uint8))
R_background_Compressed_2d.show()
R_background = lossUnCompress (R_background_Compressed_2d , (R_Image_width,R_Image_height), True)



R_Compressed_aoi_width = int (R_Heade_splited[5] -  R_Heade_splited[3])
R_Compressed_aoi_height = int (R_Heade_splited[6] -  R_Heade_splited[4])



aoi_array_len = (R_Compressed_aoi_width * R_Compressed_aoi_height * 3)


Enc_aoi_len = myround(aoi_array_len, base=16) 


R_aoi_Compressed_encrypted = np.array(All_packet_R[pinter:pinter+Enc_aoi_len]).astype(np.uint8) 
R_aoi_Compressed = aesCBCDecrypt(R_aoi_Compressed_encrypted  ,False)
R_aoi = losslessImageUncompress (R_aoi_Compressed,R_Compressed_aoi_width , R_Compressed_aoi_height , True )



newR_aoi_Image = np.array(R_aoi).reshape(R_Compressed_aoi_height,R_Compressed_aoi_width,3);
newR_aoi_Image=Image.fromarray((newR_aoi_Image).astype(np.uint8))
newR_aoi_Image.save("recever_side_constructed_image.jpg")

offset = (R_Heade_splited[3] ,R_Heade_splited[4])
R_background.paste(newR_aoi_Image, offset)


R_background.show()


quit()

aoi_R_LLcompressed = aesCBCDecrypt(aoi_S_LLcompressed_AES_CBC  ,False)
aoi_R_UnCompressedimage = losslessImageUncompress (aoi_R_LLcompressed ,aoi_width,aoi_height, True)


# aesCBCDecrypt(a  ,True)

# RC4RDecrypt (x ,background_Lcompressed_width, background_Lcompressed_height,  buildImage = True )

# aoi_width, aoi_height = aoi.size 
# aoi_LLcompressed = losslessImageCompress(imageFlat)





# aoi.show()
# background.show()




#UnCompressedimage = losslessImageUncompress (aoi_LLcompressed,aoi_width,aoi_height, True)


# Compressedimage = losslessImageCompress(imageFlat)
# UnCompressedimage = losslessImageUncompress (Compressedimage)


# x = lossCompress(background ,CompresionR ,  True)
# lossUnCompress (x , (width,height), True)


# 


