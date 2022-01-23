import hashlib
from PIL import Image
import io
import os
import os.path
import time

def rsa_encrypt(src,dest) :

    img = Image.open(src)
    m = hashlib.md5()
    with io.BytesIO() as memf:
        img.save(memf, 'PNG')
        data = memf.getvalue()
        m.update(data)
    print(m.hexdigest())
    if os.path.isfile(dest) and os.access(dest, os.R_OK):
        print("Deleting File")
        os.remove(dest)
    else:
        print("File doesnot exist")
    img.save(dest, 'PNG')
    m = hashlib.md5()
    data = open(dest, 'rb').read()
    m.update(data)
    print(m.hexdigest())
    return
start1 = time.process_time()   
rsa_encrypt('images/ugflag.jpg','images/ugflag_rsa_encoded.jpg')
print(time.process_time() - start1)
start2 = time.process_time() 
rsa_encrypt('images/kla.jpeg','images/kla_rsa_encoded.jpeg')
print(time.process_time() - start2)
start3 = time.process_time() 
rsa_encrypt('images/journey.jpg','images/journey_rsa_encoded.jpg')
print(time.process_time() - start3)