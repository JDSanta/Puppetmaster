import socket
import sys

host = '192.168.42.1'
port = 9999
address = (host, port)

# make server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)

#print "Listening for client . . ."
# pick a large output buffer size because i dont necessarily know how big the incoming packet is

while True:
    # establish client socket
    conn, address = server_socket.accept()
    #print "Connected to client at ", address
    
    x=1
    while x==1:

        # receive go message
        go_message = conn.recv(2048);
        
        if go_message.strip() == "stop":
            #conn.send("dack")
            conn.close()
            #sys.exit("Received disconnect message.  Shutting down.")
            x=0
            
        elif output:
            #print "Message received from client:"
            #print output
            conn.send("ack")

#server_socket.close()
