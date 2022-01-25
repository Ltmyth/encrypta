import numpy as np
from PIL import Image
import time

def lsb_crypt(msg_src, img_file) :
    start = time.time()
    encrypted_msg = open("encrypted/"+msg_src, "r")
    message = str(encrypted_msg)

    # Encode the message in a serie of 8-bit values
    b_message = ''.join(["{:08b}".format(ord(x)) for x in message ])
    b_message = [int(x) for x in b_message]

    b_message_length = len(b_message)

    # Get the image pixel arrays 
    with Image.open("images/"+img_file) as img:
        width, height = img.size
        data = np.array(img)
        
    # Flatten the pixel arrays
    data = np.reshape(data, width*height*3)

    # Overwrite pixel LSB
    data[:b_message_length] = data[:b_message_length] & ~1 | b_message

    # Reshape back to an image pixel array
    data = np.reshape(data, (height, width, 3))

    new_img = Image.fromarray(data)
    new_img.save("encrypted/"+img_file)
    end = time.time()
    start1 = time.time()   
    with Image.open("encrypted/"+img_file) as img:
        width, height = img.size
        data = np.array(img)
        
    data = np.reshape(data, width*height*3)
    # extract lsb
    data = data & 1 
    # Packs binary-valued array into 8-bits array.
    data = np.packbits(data)
    # Read and convert integer to Unicode characters until hitting a non-printable character
    for x in data:
        l = chr(x)
        if not l.isprintable():
            break
        #print(l, end='')
    end1 = time.time()
    print("\n"+img_file+" encrypted in : ",end-start)
    print("\n"+img_file+" decrypted in : ",end1-start1,"\n")


lsb_crypt('aes_out.txt','kids.png')
lsb_crypt('aes_out.txt','journey.png')
lsb_crypt('aes_out.txt','girafe.png')