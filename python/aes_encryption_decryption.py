import numpy as np
import random
from Cryptodome.Cipher import AES
from Cryptodome import Random
import cv2
import time

def aes_encrypt(src,dest):
    #open and read the image
    img=cv2.imread(src,1)

    #convert to array
    na = np.array(img)

    #Make it 3D 
    x, y ,pp= img.shape[:3]
    #gray image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #reshape encrypted image
    blue= np.array(range(x*y), int).reshape((x, y))
    enc_blue= np.array(range(x*y), int).reshape((x, y))
    blue[:,:]=gray[:, :]

    #encrytpion key
    key = b'Sixteen byte key'

    #initial vector
    iv=b'0000000000000000'

    #aes encrypt
    cipher = AES.new(key, AES.MODE_CFB, iv)
    #new array
    L2=[]
    blue1 = np.array(range(x),int)
    for i in range(x):
        blue1=blue[i,:].tolist()
        blue2=bytes(blue1)
        msg =  cipher.encrypt(blue2)
        for p in msg:
            L2 += [(p)]
        enc_blue[i,:]=L2[:]
        L2=[]
        cv2.imwrite(dest, enc_blue)
    print("Encryption Successfull")    
    return

start = time.process_time()    
aes_encrypt('images/ugflag.jpg','images/ugflag_aes_encoded.jpg')
print(time.process_time() - start)
start2 = time.process_time() 
aes_encrypt('images/kla.jpeg','images/kla_aes_encoded.jpg')
print(time.process_time() - start2)
start3= time.process_time() 
aes_encrypt('images/journey.jpg','images/journey_aes_encoded.jpg')
print(time.process_time() - start3)