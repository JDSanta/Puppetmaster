import socket
import sys
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import RPi.GPIO as GPIO

host = '192.168.42.1'
port = 9999
address = (host, port)

# make server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)

SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#print "Listening for client . . ."
# pick a large output buffer size because i dont necessarily know how big the incoming packet is


try:
    while True:
    
        conn, address = server_socket.accept() #waits for client to connect
        print "Connected to client at ", address
    
        x=1
        while x==1:

            go_message = conn.recv(2048); #server has found client and recieves go message
            
            if go_message.strip() == "go":
                values = [0]*8
                for i in range(8):
                    values[i] = mcp.read_adc(i)
                conn.send(str(values[0])+","+ str(values[1])+"," + str(values[2])+"," + str(values[3])+"," + str(values[4])+"," + str(values[5])+"," + str(values[6])+"," + str(values[7]))            
                #time.sleep(.25) #WAIT SO WE CAN SEE SENSOR CHANGE
                
            elif go_message.strip() == "stop":
                conn.close()
                #sys.exit("Received disconnect message.  Shutting down.")
                x=0
                        
            else:    #If server receives something other than stop or go, then it will close both client and server
                print "Invalid input from client"
                conn.send("close client") 
                conn.close()
                x=0
                
                




except KeyboardInterrupt: #exits program when keyboard interrupt is present
    print "keyboard interrupt" 
    conn.close()
    x=0
    
    
   
finally: #this ensures a clean exit for the GPIO pins after we change them
    GPIO.cleanup() #will need this eventually for the server
    server_socket.close()
