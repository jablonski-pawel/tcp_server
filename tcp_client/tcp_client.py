'''
Created on 07.11.2016

@author: gorian
'''
import socket

def Main():
    #host = 'www.google.com'
    port = 5000 #80
    
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #ip = socket.gethostbyname(host)
    ip = '127.0.0.1'
    address = (ip, port)
    s.connect(address)
    print(ip, address)
    
    message = raw_input("-> ")
    while message != 'q':
        if(message == 'g'):
            message = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
        s.send(message)
        data = s.recv(1024)
        print("Recived from server: "+str(data))
        message = raw_input("-> ")
        s.close()
        
    
if __name__ == '__main__':
    print("TCP Client")
    print("==========")
    Main()
    pass