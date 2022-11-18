import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 15555))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print("{} connected".format( address ))

        response = client.recv(255)
        print(response)
        if response[-3:] == b"EOF":
                break

print("Close")
client.close()
socket.close()