from pwn import *
import re
import urllib.parse
import base64
import codecs

conn = remote('pwn-2021.duc.tf', 31905)

s = conn.recvuntil(b'...')
print(s)
s = conn.send(b'\r\n')
# print(s)

s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.sendline(b'2')

s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

num = re.findall(r': (.*)\n', s.decode())[0]
print(num)
num = int(num,16)
s = conn.sendline(str(num).encode())

#2
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

num = re.findall(r': (.*)\n', s.decode())[0]
print(num)
num = bytes.fromhex(num).decode('utf-8')
s = conn.sendline(num.encode())

#3
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

num = re.findall(r': (.*)\n', s.decode())[0]
print(num)
num = urllib.parse.unquote(num)
s = conn.sendline(num.encode())


#4
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

num = re.findall(r': (.*)\n', s.decode())[0]
print(num)
num = base64.b64decode(num)
s = conn.sendline(num)


#5
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

num = re.findall(r': (.*)\n', s.decode())[0]
print(num)
num = base64.b64encode(num.encode())
s = conn.sendline(num)


#6
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

num = re.findall(r': (.*)\n', s.decode())[0]
print(num.encode('ascii'))
num = codecs.encode(num, "rot-13")
s = conn.sendline(num.encode())


#7
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

num = re.findall(r': (.*)\n', s.decode())[0]
print(num.encode('ascii'))
num = codecs.encode(num, "rot-13")
s = conn.sendline(num.encode())

#8
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

num = re.findall(r': (.*)\n', s.decode())[0]
print(num)
num = int(num,2)
print(num)
s = conn.sendline(str(num).encode())

#9
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

num = re.findall(r': (.*)\n', s.decode())[0]
print(num)
num = bin(int(num))
print(num)
s = conn.sendline(str(num).encode())


#9
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.sendline(b'DUCTF')


s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)
s = conn.recvline()
print(s)

conn.close()
