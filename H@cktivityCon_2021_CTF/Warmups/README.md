# Warmup
---
## Six Four Over Two
Category: Cryptography
Difficulty: Easy

Description:
I wanted to cover all the bases so I asked my friends what they thought, but they said this challenge was too basic...

Cipher in the file:
`
EBTGYYLHPNQTINLEGRSTOMDCMZRTIMBXGY2DKMJYGVSGIOJRGE2GMOLDGBSWM7IK
`
### Solution
The challenge is the a hint. 64/2 = 32. Thus it is encoded by base32.  

**flag{a45d4e70bfc407645185dd9114f9c0ef}**

---

## Bass64
Category: Cryptography
Difficulty: Easy

Description:
It, uh... looks like someone bass-boosted this? Can you make any sense of it?


### Solution
When we opent the given file with notepad, we can see characters in it.
Don't open it using wordpad!
All we need to do is recognizing them one by one and decode it using base64.

---

## 2EZ
Category: Steganography
Difficulty: Easy

Description:
These warmups are just too easy! This one definitely starts that way, at least!

### Solution
Open the file in hexadecimal.
We can find `JFFI`there. It means the file is a jpeg picture instead of 2ez file.
Chanage fisrt four hex of file to `FF 08 FF 00` which is the feature code of the jpeg file.
Change the file suffix to `.jpeg`.

**flag{812a2ca65f334ea1ab234d8af3c64d19}**
