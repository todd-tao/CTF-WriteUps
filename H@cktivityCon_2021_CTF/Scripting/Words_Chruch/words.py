from pwn import *
import re

def find_around(string_list, x, y, word):
    direct = []
    for i in range(-1,2):
        for j in range(-1,2):
            if x+i >= 0 and y+j >= 0 and x+i < 16 and y+j < 16 and string_list[x+i][y+j] == word:
                direct.append([i,j])
    return direct

def rec(string_list, w):
    record = []
    for i in range(16):
        for j in range(16):
            if string_list[i][j] == w[0]:
                record.append((i,j))
                direct = find_around(string_list, i, j, word[1])
                if direct:
                    for d in direct:
                        di = d[0]
                        dj = d[1]
                        for z in range(1,len(word)):
                            x = i+z*di
                            y = j+z*dj
                            if x > 15: x -= 16
                            if x < 0: x += 16
                            if y > 15: y -= 16
                            if y < 0: y += 16
                            if string_list[x][y] != word[z]:
                                break
                            else:
                                record.append((i+z*di,j+z*dj))
                        if len(record) == len(w):
                            return record
                        record = [(i,j)]
                record = []

def reverse(l):
    record = []
    for i in l:
        record.append((i[1],i[0]))
    return record


conn = remote('challenge.ctf.games', 30959)
sen = conn.recvuntil(b'>', drop=True)
conn.send(b'play')

for _ in range(30):
    word = conn.recvuntil(b'30:').decode()
    print(word)
    s1 = conn.recvline()
    # print(s1)
    s2 = conn.recvline()
    # print(s2)
    s3 = conn.recvline()
    # print(s3)

    string_list = []
    for i in range(16):
        s = conn.recvline()
        list = re.findall(r'\t(.*)\n',s.decode())[0].split()
        string_list.append(list)
        print(list)

    for _ in range(5):
        word = conn.recvuntil(b'> ').decode()
        print(word)
        word = re.findall(r'(\w*): ',word)[0]
        # print(word)
        record = rec(string_list,word)
        if record:
            record = reverse(record)
        # print(record)
        conn.send(str(record).encode())

while 1:
    flag = conn.recvline()
    print(flag.decode())

conn.close()


                            


# print(record)