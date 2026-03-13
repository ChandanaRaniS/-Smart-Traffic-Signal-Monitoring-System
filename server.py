import socket
import threading
import ssl

HOST = "0.0.0.0" #accept any connections from any ip address 
PORT = 5000

# create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp protocol

# create SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

server.bind((HOST, PORT))
server.listen()

print("Secure Server started...")
print("Waiting for signal clients...")

def handle_client(conn, addr):#communiication with connected client
    print(f"Connected to {addr}")

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            print(f"Signal Data from {addr}: {data}")

        except:
            break

    conn.close()
    print(f"Connection closed: {addr}")

while True:
    client_socket, addr = server.accept()

    # wrap socket with SSL
    secure_conn = context.wrap_socket(client_socket, server_side=True)

    thread = threading.Thread(target=handle_client, args=(secure_conn, addr))
    thread.start()