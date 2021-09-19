import gmpy2
from Crypto.Util.number import bytes_to_long, long_to_bytes
cipher = '0x10652cdfaa6a6f6f688b98219cd32ce42c4d4df94afaea31cd94dfac50678b1f50f3ab1fd389f9998b6727ffd1a2c06ee6bde21ae85daef63fd0fa694a93f3674dc3f9ea0f2e3283a3d9897137aea12458aa3b8f96c61f3bf74a510bab7e7d8b7af52290d2621f1e06e52e6a7be4896c6465'
num = int(cipher, 0)
n = gmpy2.iroot(num,3)[0]
print(long_to_bytes(n).decode())