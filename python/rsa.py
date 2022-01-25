from Crypto import Cipher
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import time

start_time1=time.time()
# privKEY,pubKey
private_key = RSA.generate(2048) # shortened for testing
public_key = private_key.publickey()
# 'convert' really store
with open('keys/private.pem','w') as pr:
  pr.write(private_key.exportKey().decode())
with open('keys/public.pem','w') as pu:
  pu.write(public_key.exportKey().decode())


#convert binary to string
file_in = open('encrypted/aes_encrypted.bin', "rb")
with file_in as file:
  data = file.read()
  with open("encrypted/aes_out.txt", "w") as f:
    f.write(" ".join(map(str,data)))
    f.write("\n")

# encrypt
with open('encrypted/aes_out.txt', 'r') as file:
  data = file.read().replace('\n', '')
  message = bytes(data,'utf-8')
  pu_key = RSA.importKey(open('keys/public.pem','r').read())
  ciphertext = PKCS1_OAEP.new(pu_key).encrypt(message)

  #write encrypted
  with open('encrypted/rsa_encrypted.txt','wb') as f:
    f.write(ciphertext)

  end_time1=time.time()
  start_time2=time.time()
  # decrypt
  ciphertext = open('encrypted/rsa_encrypted.txt','rb').read()
  pr_key = RSA.importKey(open('keys/private.pem','r').read())
  decrypted = PKCS1_OAEP.new(pr_key).decrypt(ciphertext)

  #save decrypted file
  f = open('decrypted/rsa_decrypted.txt', 'w' )
  f.write(decrypted.decode('UTF-8'))
  f.close()
  end_time2=time.time()
    
print("RSA Encryption time is : ", end_time1-start_time1)
print("RSA Decryption time is : ", end_time2-start_time1)