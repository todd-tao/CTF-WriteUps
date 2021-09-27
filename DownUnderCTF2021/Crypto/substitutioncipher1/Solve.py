def equation(x):
    x = int(x)
    return 13*x**2 + 3*x + 7

f = open("DownUnderCTF2021/Crypto/substitutioncipher1/output.txt", "r")
for i in f.read():
    # print(ord(i))
    for j in range(0,255):
        # print(equation(j))
        if equation(j) == ord(i):
            print(chr(j),end='')

print()
f.close()