import socket
import sys
import time

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
        # data_utf8 = data.encode('utf-8')
        # self.udpClntSock.sendto(data_utf8,self.DstAddr)


        data_size = sys.getsizeof(data)
        print('datasize:{}'.format(data_size))
        send_num = int(data_size/60000 + 1)
        print('send_num.{}'.format(send_num))
        for i in range(send_num):
            start = i * 60000
            end = start + 60000
            send_data = ''
            if i == 0:
                send_data = 's' + str(send_num) + str(i) + data[start:end]
            else:
                send_data = str(i) + data[start:end]
            send_data = send_data.encode('utf-8')
            self.udpClntSock.sendto(send_data,self.DstAddr)
            time.sleep(0.005)
