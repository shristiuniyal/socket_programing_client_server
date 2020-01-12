#import socket module
import socket
def server():
    #host and the port to be connected is specified
    host = socket.gethostname()
    port = 6000
    #socket object is created
    ser_soc = socket.socket()
    print("socket is successfully created!")
    ser_soc.bind((host,port))
    print "socket binded to %s"%(port)
    ser_soc.listen(2)
    print("socket is listening.....")
    con, address = ser_soc.accept()
    print("connected to the server with ip address: "+str(address))
    while(2):
        #server starts receiving data sent by client
        data = con.recv(1024).decode()
        if not data:
            print("enter valid data")
            break
        print("message received from client:"+str(data))
        data = input('==>')
        #response is sent to the client
        con.send(data.encode())
    #connection closed
    con.close()
server()

