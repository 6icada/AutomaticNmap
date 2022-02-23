# Code by 6icada
# Please do not copy code

# Tring to import libraries
try:
    import socket
    import os
except:
    # ERROR MSG
    print(f'[ERROR]: Can\'t import libraries...')
    exit()

# Scan function
def Scan(targetList, RHOST, RPORT):
    # Adding vars
    Scanner_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connecting to the Receiver
    Scanner_Socket.connect((RHOST, int(RPORT)))
    # Loop
    for target in targetList:
        # Scanning target
        toSave = os.system(f'nmap -sC -sV -A {target} > {target}.txt')

        # Opening file
        file = open(f'{target}.txt', 'r')
        dataToSend = file.read()
        file.close()

        # Sending data to the Receiver
        Scanner_Socket.send(dataToSend.encode('utf-8'))

    # Closing connection
    Scanner_Socket.close()

# Adding vars
counter1 = 1
targets = []
receiverHost = input('Enter RHOST: ')
receiverPort = input('Enter RPORT: ')
maxTarget = input('How many targets to you want? :  ')

while counter1 <= int(maxTarget):
    # Adding vars
    userInput = input('Enter Target: ')

    # Adding target in targets list
    targets.append(userInput)

    counter1 = counter1 + 1

# Calling functions
Scan(targets, receiverHost, receiverPort)
