# you can enter input as "{ip} {from port} {to port}"
#you dont need curvy brackets or quotation marks...



import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_port_range = input()
inlist = ip_port_range.split()
ip = inlist[0]

print("open ports within range:")
for port in range(int(inlist[1]), int(inlist[2])):
    if s.connect_ex((ip, port)) == 0:
        print(port)
    s.close()

print("open ports printed")