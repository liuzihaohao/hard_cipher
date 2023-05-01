# 服务端

import getpass
from Crypto.Cipher import AES

# 填写对应信息
passworld=bytes.fromhex("4246a708551aa131602f529331132b06")
iv=bytes.fromhex("815c789158ced329869104616a2ca4e8")

aes=AES.new(passworld,AES.MODE_CBC,iv)
data=getpass.getpass(">>>").encode()

while len(data)%16!=0:
    data+=b'\x00'

en_text=aes.encrypt(data)
print("en_text:",en_text.hex())