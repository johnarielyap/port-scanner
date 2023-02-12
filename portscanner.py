import pyfiglet
import sys
import socket

ascci_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascci_banner)

target = input(str("TARGET IP ADDRESS:"))

print("\n SCANNING ON " + target)
print("GRAB SOME COFFEE WHILE WAITING")
print("\n GOT YOUR COFFEE?")

try:

  for port in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target,port))
    if result == 0:
      print("[*] Port {} is open".format(port))
      s.close()

except KeyboardInterrupt:
  print("\n Exiting...")
  print("\n Exiting Please Wait...")
  sys.exit()

except socket.error:
  print("\n Host not responding")
  print("\n not responding")
  sys.exit()
