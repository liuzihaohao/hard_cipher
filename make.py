# 生成新数据

# 依赖:pycryptodome
mods='''#include <AESLib.h>

byte key[N_BLOCK]={{{}}};
byte iv[N_BLOCK]={{{}}};

int hex_to_dec(String hex) {{
    int dec = 0;
    int base = 1;
    int len = hex.length();
    for (int i = len - 1; i >= 0; i--) {{
        if (hex[i] >= '0' && hex[i] <= '9') {{
            dec += (hex[i] - '0') * base;
        }}
        else if (hex[i] >= 'a' && hex[i] <= 'f') {{
            dec += (hex[i] - 'a' + 10) * base;
        }}
        else if (hex[i] >= 'A' && hex[i] <= 'F') {{
            dec += (hex[i] - 'A' + 10) * base;
        }}
        base *= 16;
    }}
    return dec;
}}

void setup() {{
  Serial.begin(9600);
}}

void loop() {{
  AESLib aesLib;

  if(Serial.available()){{
    byte iv_t[N_BLOCK];
    for(uint16_t i=0;i<16;i++){{
      iv_t[i]=iv[i];
    }}
    
    String serialData=Serial.readString();
    byte data[serialData.length()/2];
    
    for(uint16_t i=0;i<serialData.length();i+=2){{
      String temp_str;
      temp_str=temp_str+serialData[i];
      temp_str=temp_str+serialData[i+1];
      data[i/2]=hex_to_dec(temp_str);
    }}
    byte plain[serialData.length()*2];

    uint16_t plainlen=aesLib.decrypt(data,serialData.length()/2,plain,key,16,iv_t);
    
    String output=plain;
    Serial.println(output);
  }}
}}
'''
import secrets
from Crypto.Cipher import AES

data="test".encode(encoding="ascii")
passworld=secrets.token_bytes(16)
iv=secrets.token_bytes(16)
# passworld=b'\xaf\xbf\x03\xda\x94\xec1G\xfc\xca\xa6X\xb9u\xcap'
# iv=b'd\rU\xc9\xd6Jlh-\xb1\xb8ng\xee\x8f\xbd'
print("PassWorld:",passworld.hex())
print("Iv:",iv.hex())

aes=AES.new(passworld,AES.MODE_CBC,iv)

while len(data)%16!=0:
    data+=b'\x00'

en_text=aes.encrypt(data)
print("en_text:",en_text.hex())

aes=AES.new(passworld,AES.MODE_CBC,iv)
den_text=aes.decrypt(en_text)

# print(den_text.hex())
print(den_text.decode(encoding="ascii"))

m_passworld=""
h_passworld=passworld.hex()
for i in range(0,len(h_passworld),2):
    m_passworld=m_passworld+'0x'+h_passworld[i:i+2]+','
m_passworld=m_passworld[:-1]
    
m_iv=""
h_iv=iv.hex()
for i in range(0,len(h_iv),2):
    m_iv=m_iv+'0x'+h_iv[i:i+2]+','
m_iv=m_iv[:-1]

print(mods.format(m_passworld,m_iv))