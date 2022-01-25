from curses import keyname
import numpy as np
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import cv2
import time
import os.path


key = ""
cipher =""
nonce =""
ciphertext =""
tag = ""

def aes_text_enc(msg,destination) :
    start1 = time.time()
    data=bytes(msg, encoding='utf-8')
    message=data
    global key
    key = get_random_bytes(16) #must be 16, 24 or 32 bytes long
    global cipher
    cipher = AES.new(key, AES.MODE_EAX)
    global ciphertext, tag 
    ciphertext, tag = cipher.encrypt_and_digest(message)

    #check file existence
    if os.path.isfile(destination) and os.access(destination, os.R_OK):
        print("File exists,Deleting and recreating")
        os.remove(destination)
    else:
       print("File doesnot exist, Creating")
    
    #write encrypted binary file
    file_out = open(destination, "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
    file_out.close()
    end1 = time.time()
    print('Aes encryption done in :', end1-start1)


def aes_text_dec(src,destination) :
    start2 = time.time()
    file_in = open(src, "rb")
    global nonce, tag, ciphertext
    nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
    #check file existence
    if os.path.isfile(destination) and os.access(destination, os.R_OK):
        print("File exists,Deleting and recreating")
        os.remove(destination)
    else:
       print("File doesnot exist, Creating")
    # the person decrypting the message will need access to the key
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    dec_txt = data.decode('UTF-8')

    path = os.path.abspath(destination)

    with open(path, 'w') as f:
        f.write(dec_txt)
    end2 = time.time()
    print('Aes decryption done in : ', end2-start2)


aes_text_enc(" Rose Adee encrypted files","encrypted/aes_encrypted.bin")
aes_text_dec("encrypted/aes_encrypted.bin","decrypted/aes_decrypted.txt")




"""------------------------------------------------START OF IMAGE ENCRYPTION--------------------------------------------------------"""


def aes_encrypt(src,dest):
    process1_start_time=time.time()
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


    #check file existence
    if os.path.isfile(dest) and os.access(dest, os.R_OK):
        print("File exists,Deleting and recreating")
        os.remove(dest)
    else:
       print("File doesnot exist, Creating")

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
    end_time = time.time()
    time_elapsed = end_time - process1_start_time
    print(src+" Encryption time :",time_elapsed)  
    return

def aes_decrypt(src,dest):
    process1_start_time=time.time()
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


    #check file existence
    if os.path.isfile(dest) and os.access(dest, os.R_OK):
        print("File exists,Deleting and recreating")
        os.remove(dest)
    else:
       print("File doesnot exist, Creating")

    #aes decrypt
    cipher = AES.new(key, AES.MODE_CFB, iv)
    #new array
    L2=[]
    blue1 = np.array(range(x),int)
    for i in range(x):
        blue1=blue[i,:].tolist()
        blue2=bytes(blue1)
        msg =  cipher.decrypt(blue2)
        for p in msg:
            L2 += [(p)]
        enc_blue[i,:]=L2[:]
        L2=[]
        cv2.imwrite(dest, enc_blue)
    print(" Decryption Successfull")  
    end_time = time.time()
    time_elapsed = end_time - process1_start_time
    print(src+" Decryption time :",time_elapsed)  
    return




"""Image encryption and decryption"""
#aes_encrypt('images/ugflag.jpg','images/ugflag_aes_encoded.jpg')
#aes_encrypt('images/kla.jpeg','images/kla_aes_encoded.jpg')
#aes_encrypt('images/journey.jpg','images/journey_aes_encoded.jpg')
#aes_decrypt('images/journey_aes_encoded.jpg','images/journey_aes_decoded.jpg'

"""----------------------------------------------------End image encryption-------------------------------------------------"""
