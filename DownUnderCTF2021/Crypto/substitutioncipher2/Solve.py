from string import ascii_lowercase, digits
from scipy.optimize import fsolve

CHARSET = "DUCTF{}_!?'" + ascii_lowercase + digits

f = open("DownUnderCTF2021/Crypto/substitutioncipher2/output2.txt", "r")
words = f.read()
f.close()

# print(CHARSET)
index_list = []
for i in words:
    # print(i)
    index_list.append(CHARSET.index(i))

print(index_list)

def equation(a,b,c,d,e,f,g,x):
    return  a*x**6 + b*x**5 + c*x**4 + d*x**3 + e*x**2 + f*x + g

def solve_function(unsolved_value):
    b,c,d,e,f,g=unsolved_value[0],unsolved_value[1],unsolved_value[2],unsolved_value[3],unsolved_value[4],unsolved_value[5]
    unsolved = []
    for i in range(6):
        unsolved.append(equation(b,c,d,e,f,g,i)-index_list[i])
    # print(unsolved)
    return unsolved

from sympy import *

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
d = Symbol('d')
e = Symbol('e')
f = Symbol('f')
g = Symbol('g')
e_list = []
for i in range(6):
    e_list.append(equation(a, b,c,d,e,f,g,i)-index_list[i])
e_list.append(equation(a, b,c,d,e,f,g,6)-index_list[-1])
print(e_list)

r1 = solve(e_list,[a, b,c,d,e,f,g])
print(r1)
for i in index_list:
    for j in range(len(CHARSET)):
        value = equation(r1[a],r1[b],r1[c],r1[d],r1[e],r1[f],1,j)
        value = int(value)
        if value%len(CHARSET) == i:
            print(CHARSET[j],end='')
            break
print()