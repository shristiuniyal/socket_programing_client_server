#import the socket module
import socket
def client():
    #get the name of host name and the port number
    host = socket.gethostname()
    port = 6000
    #a socket object is created
    cli_soc = socket.socket()
    #client's socket is connected with the host and por of the server
    cli_soc.connect((host,port))
    message = input("==>")
    while message.lower().strip()!='break the connection':
        #send the data to the connected server
        cli_soc.send(message.encode())
        #data recived from the server is decoded
        data = cli_soc.recv(1024).decode()
        print('data received from the server is:'+data)
        message = input("==>")
    #connection with the server is disabled
    cli_soc.close()
client()
