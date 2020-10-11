import socket

class udpsend():
    def __init__(self):
        SrcIP = '127.0.0.1'
        SrcPort = 8080
        self.SrcAddr = (SrcIP,SrcPort)

        DstIP = '127.0.0.1'
        DstPort = 3000
        self.DstAddr = (DstIP,DstPort)

        self.udpClntSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.udpClntSock.bind(self.SrcAddr)


    def send(self,data):
        data_utf8 = data.encode('utf-8')
        self.udpClntSock.sendto(data_utf8,self.DstAddr)
