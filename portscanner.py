import pyfiglet
import sys
import socket

ascci_banner = pyfiglet.figlet_format("PORT SCANNER LITE")
print(ascci_banner)

target = input(str(" TARGET IP ADDRESS:"))

print("scanning target..." + target)


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
  sys.exit()

except socket.error:
  print("\n Host not responding")
  sys.exit()
