from scapy.all import ARP, Ether, srp
import socket
import pyfiglet

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
        Server = input("Lütfen IP Adresi Giriniz: ")
        ServerIp = socket.gethostbyname(Server)

        for port in range(1,10000):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result = sock.connect_ex((ServerIp,port))
            if result == 0:
                print("Port {}: Açık".format(port))
            else:
                print("Port {}: Kapalı".format(port))
            sock.close()
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
            Server = input("Lütfen IP Adresi Giriniz: ")
            ServerIp = socket.gethostbyname(Server)

            for port in range(1,10000):
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                result = sock.connect_ex((ServerIp,port))
                if result == 0:
                    print("Port {}: Open".format(port))
                else:
                    print("Port {}: Close".format(port))
                sock.close()
            print("-----------------------------------------------------")
        
            menü()

            options=int(input(">> "))    
                
    else:
        print("Görüşürüz :)")
