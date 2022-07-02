from requests import get
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
with open('local.txt', 'w') as a:
    a.write("local ip=" + s.getsockname()[0])
s.close()
 
hostname = socket.gethostname()  

with open('name.txt', 'w') as a:
    a.write("name=" + hostname)

