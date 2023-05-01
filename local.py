# 本地端

import serial,os,time
import serial.tools.list_ports

print("自动解密程序")
print("在输入之前，请确保设备拔出\n")
print("请输入密文:")
en_text=input(">>>")

port_list_old=list(serial.tools.list_ports.comports())
print("请插入设备")
os.system("pause")
port_list_new=list(serial.tools.list_ports.comports())

portx=None

for i in port_list_new:
    if i not in port_list_old:
        portx=i

if not portx:
    print("没有检测到新的设备")
    raise SystemExit

portx=portx.usb_description()
bps=9600
timex=None
print("打开的串口:",portx)
print("  bps:",bps)
print("  timeout:",timex,"\n")

ser=serial.Serial(portx,bps,timeout=timex)
time.sleep(2)

result=ser.write(en_text.encode())
# print("Write:",result,"K")

result=ser.readline().decode()
# print("Read:",result)
print(result)

ser.close()