# Code by 6icada
# Please do not copy code

# Tring to import libraries
try:
    import socket
except:
    # ERROR MSG
    print(f'[ERROR]: Can\'t import libraries...')
    exit()

# MakeSocket function
def MakeSocket():
    # Adding vars
    HOST = '0.0.0.0'
    PORT = 4444
    Receiver_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clients = []

    # Binding Receiver_Socket
    Receiver_Socket.bind((HOST, PORT))
    Receiver_Socket.listen()

    # MSG when Receiver starts
    print(f'[START]: Receiver started on {HOST}:{PORT}')

    # Handle function (To handle clients)
    def Handle():
        while True:
            # Adding vars
            client, address = Receiver_Socket.accept()

            # Adding client's address to clients list
            clients.append(address)
            
            # MSG when client connects
            print(f'[INFO]: Connection from {address}')
            
            while True:
                # Receiving data
                receivedData = client.recv(9999999)
                
                if len(receivedData.decode('utf-8')) > 0:
                    # MSG when data receives
                    print(f'[INFO]: Received data from {address}')

                    # Decoding receivedData
                    decodedReceivedData = receivedData.decode('utf-8')

                    # Writing decodedReceivedData to the file
                    file = open('receivedData.txt', 'a')
                    file.write(f'{decodedReceivedData}\n\n\n\n\n\n\n\n\n\n')
                    file.close()
                else:
                    pass

    # Calling functions
    Handle()

# Calling functions
MakeSocket()
