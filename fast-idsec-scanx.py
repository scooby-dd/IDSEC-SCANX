from scapy.all import ARP, Ether, srp
import socket
import pyfiglet
import re
import nmap


ascii_banner=pyfiglet.figlet_format(""" İDSEC
HACK    
TOOL""")



print(ascii_banner)

def menü():
    print("[1] Network Scanner")
    print("[2] Port Scanner")
    print("[3] Full Scanner")
    print("[0] Exit")
menü()

options=int(input(">> "))
while options != 0:
    if options == 1:
    
        target_ip = "192.168.1.1/24"
            
       




        arp = ARP(pdst=target_ip)

        ether = Ether(dst="ff:ff:ff:ff:ff:ff")

        packet = ether/arp

        result = srp(packet, timeout=3, verbose=0)[0]


        clients = []

        for sent, received in result:

            clients.append({'ip': received.psrc, 'mac': received.hwsrc})


        print("Available devices in the network:")
        print("IP" + " "*18+"MAC")
        for client in clients:
            print("{:16}    {}".format(client['ip'], client['mac']))
        print("-----------------------------------------------------")    
        menü()

        options=int(input(">> "))                
                
                
    elif options == 2:
        ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
        port_min = 0
        port_max = 65535
        open_ports = []
        while True:
            ip_add_entered = input("\nLütfen Hedefin IP Adresini Girin: ")
            if ip_add_pattern.search(ip_add_entered):
                print(f"{ip_add_entered} is a valid ip address")
                break
        while True:
            print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
            port_range = input("Taranması İstenen Port Aralığı giriniz ör(20-25): ")
            print("-----------------------------------------------------")
            port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
            if port_range_valid:
                port_min = int(port_range_valid.group(1))
                port_max = int(port_range_valid.group(2))
                break
        for port in range(port_min, port_max + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    s.connect((ip_add_entered, port))
                    open_ports.append(port)
            except:
                pass
        for port in open_ports:
            print(f"Port {port} is open on {ip_add_entered}.")
                

            print("-----------------------------------------------------")
            menü()

            options=int(input(">> "))       
                    
    elif options == 3:
        
            target_ip = "192.168.1.1/24"




            arp = ARP(pdst=target_ip)

            ether = Ether(dst="ff:ff:ff:ff:ff:ff")

            packet = ether/arp

            result = srp(packet, timeout=3, verbose=0)[0]


            clients = []

            for sent, received in result:

                clients.append({'ip': received.psrc, 'mac': received.hwsrc})


            print("Available devices in the network:")
            print("IP" + " "*18+"MAC")
            for client in clients:
                print("{:16}    {}".format(client['ip'], client['mac']))
            print("---------- PORT TARAMA ----------")
            ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
            port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
            port_min = 0
            port_max = 65535
            open_ports = []
            while True:
                ip_add_entered = input("\nLütfen Hedefin IP Adresini Girin: ")
                if ip_add_pattern.search(ip_add_entered):
                    print(f"{ip_add_entered} is a valid ip address")
                    break
            while True:
                print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
                port_range = input("Taranması İstenen Port Aralığı giriniz ör(20-25): ")
                print("-----------------------------------------------------")
                port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
                if port_range_valid:
                    port_min = int(port_range_valid.group(1))
                    port_max = int(port_range_valid.group(2))
                    break
            for port in range(port_min, port_max + 1):
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                        s.settimeout(0.5)
                        s.connect((ip_add_entered, port))
                        open_ports.append(port)
                except:
                    pass
            for port in open_ports:
                print(f"Port {port} is open on {ip_add_entered}.")
            
            print("-----------------------------------------------------")
        
            menü()

            options=int(input(">> "))    
                
    else:
        print("Görüşürüz :)")
