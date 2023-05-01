# hard_cipher

## 简介

使用 AES 加密方式来保护数据,因为 AES 为对称加密,

密钥在加解密过程中都是相同的,所以很容易破解,

所以可以将 PassWorld 和 Iv 数组刷入 Arduino Uno,并在解密时将 Arduino Uno 使用串口的方式进行通信,

解密过程在 Arduino Uno 内进行,不会泄露 PassWorld 和 Iv 数组,以达到安全的加密。


## 代码

1. make.py 可以生成密钥和写进 Arduino Uno 的代码

2. newdata.py 可以根据 PassWorld 和 Iv 加密数据

3. local.py 可以使用串口与 Arduino Uno 进行通信以解密文本

