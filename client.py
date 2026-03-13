import socket
import ssl
import time

SERVER_IP = "127.0.0.1"
PORT = 5000

signals = ["RED", "GREEN", "YELLOW"]

# ignore certificate verification
context = ssl._create_unverified_context()

for i in range(101, 104):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_client = context.wrap_socket(client)

    secure_client.connect((SERVER_IP, PORT))

    signal_id = f"Signal_{i}"

    for status in signals:
        message = f"{signal_id} : {status}"
        secure_client.send(message.encode())
        print("Sent:", message)
        time.sleep(2)   #delay for 2seconds to simulate real traffic signal timing 

    secure_client.close()