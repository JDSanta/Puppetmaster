import socket
import sys

host = '192.168.42.1'
port = 9999
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)

#print "Listening for client . . ."
#conn, address = server_socket.accept()
#print "Connected to client at ", address
#pick a large output buffer size because i dont necessarily know how big the incoming packet is

while True:
    conn, address = server_socket.accept()
    x=1
    
    while x==1:
        
        output = conn.recv(2048);
        if output.strip() == "disconnect":
            #conn.send("dack")
            conn.close()
            #sys.exit("Received disconnect message.  Shutting down.")
            x=0
            
        elif output:
            #print "Message received from client:"
            #print output
            conn.send("ack")

#server_socket.close()
