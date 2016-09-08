#PuppetMaster Client Sensor Testing
#Taylor Michel
#Josh Santarelli
#Daniel Edwards
#
#This code is to test data streaming through socket

import socket
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #connect to socket
client_socket.connect(("192.168.42.1", 9999))

x = 1
try:
    while x==1:

        client_socket.send("go") #sends go message to initiate server data being read

        sensordata = client_socket.recv(2048)  #recieves sensor data 
    
        if sensordata != "close client":
    
            unpacked_data = sensordata.split (',')
        
            print (unpacked_data[0]) #prints first sensor data value as string
         
        else :
    
            x=0

except KeyboardInterrupt:

    #client_socket.send("stop") #sends stop message when it is done doing whatever with data
    print "keyboard interrupt"
    
    
finally:
    client_socket.close()