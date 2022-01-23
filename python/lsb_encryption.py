from PIL import Image
import time
import os
import os.path

def lsb_encode(src,dest):

    i=0
    data = "011011000110010101100100011001110110010101110010" #ledger 
    with Image.open(src) as img:
        width, height = img.size
        if os.path.isfile(dest) and os.access(dest, os.R_OK):
            print("File exists and is readable/there")
            os.remove(dest)
        else:
            print("File doesnot exist")
            
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0,3):
                    if(i < len(data)):
                        pixel[n] = pixel[n] & ~1 | int(data[i])
                        i+=1
                img.putpixel((x,y), tuple(pixel))
        img.save(dest, "PNG")

    print("Encoding successful")
    return

start1 = time.process_time()   
lsb_encode("images/ugflag.jpg","images/ugflag_lsb_encoded.png")
print(time.process_time() - start1)
start2 = time.process_time()  
lsb_encode("images/kla.jpeg","images/kla_lsb_encoded.png")
print(time.process_time() - start2)
start3 = time.process_time()  
lsb_encode("images/journey.jpg","images/journey_lsb_encoded.png")
print(time.process_time() - start3)
