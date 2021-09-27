# Crypto

## Substitution Cipher I
Difficulty: beginner

Description:  
Just a simple substitution cipher to get started...

Output is [here](substitutioncipher1/output.txt)  
Encryption file is [here](substitutioncipher1/substitution-cipher-i.sage)



### Solve

When we analyse the encryption file, there is a polynomial ring `f = 13*x^2 + 3*x + 7`. Thus we can brute force and get x.  

Script is [here](substitutioncipher1/Solve.py).


## Substitution Cipher II
Difficulty: easy

Description:  
That's an interesting looking substitution cipher...

Output is [here](substitutioncipher2/output2.txt)  
Encryption file is [here](substitutioncipher2/substitution-cipher-ii.sage)



### Solve

When we analyse the encryption file, there is a polynomial ring and random_element(6). After googling what is random_element(6), we know what it will create a random polynomial ring with max degree is 6. For instance: `5*x^6 - 3*x^5 + 5*x^4 - 6*x^3 + 2*x^2 - 4*x^1 - 5`.  

I used from `fsolve` from `scipy.optimize` to slove this polynomial ring.  

In order to get coefficient of this polynomial ring, we need to input some known results. Since the flag is started by `DUCTF{` and end by `}`, those 7 results can help us get coefficients.  

At last, we can brute force whole flag.  

Script is [here](substitutioncipher2/Solve.py).

## Break Me!
Difficulty: beginner

Description:  
AES encryption challenge.

Source code: [here](breakme/aes-ecb.py)


### Solve
The message is divided into blocks, and each block is encrypted separately. All blocks are encrypted by the same key.  

![AES ECB](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d6/ECB_encryption.svg/601px-ECB_encryption.svg.png)

Thus, we can make up `msg` payload to brute force key one by one.  


Script is [here](breakme/crackme.py).
