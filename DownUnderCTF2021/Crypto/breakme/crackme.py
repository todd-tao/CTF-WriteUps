from pwn import *
import base64
from Crypto.Cipher import AES
# def find_payload():



c = remote('pwn-2021.duc.tf', 31914)

# brute force key one by one 

"""
s = c.recvline()
print(s)
s = c.recvline()
print(s)
payload = 16*'a' + 15 * '0'
c.sendline(payload.encode())
s = c.recvline()
s = base64.b64decode(s)
print(s)
state = s[48:64]
print(state)
mark = s[64:80]
print(mark)

array = "mqmwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789{}_-~!@#$%^&*()-=+[]?><'|,./`\"m"
for i in array:
    s = c.recvline()
    # print(s)
    payload = 16*'a' + 15 * '0' + '!_SECRETSOURCE_!' + i
    c.sendline(payload.encode())
    s = c.recvline()
    s = base64.b64decode(s)
    # print(s)
    m = s[64:80]
    if m == mark:
        print('last char', i)
        break
    
"""
key = '!_SECRETSOURCE_!'.encode()
cipher = AES.new(key, AES.MODE_ECB)


s = c.recvline()
print(s)
s = c.recvline()
print(s)
payload = ''
c.sendline(payload.encode())
s = c.recvline()
s = base64.b64decode(s)
print(s)

message = cipher.decrypt(s)
print(message)
s = c.recvline()
print(s)

c.close()
# c.interactive()
