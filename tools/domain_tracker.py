import socket #module for gethostbyname
website = input ("web>")
ip = socket.gethostbyname(website)
print(ip)

input('')