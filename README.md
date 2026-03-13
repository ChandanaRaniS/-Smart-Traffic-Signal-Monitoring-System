# Smart Traffic Signal Monitoring System (Secure Socket Programming)

## Project Overview

This project demonstrates a **secure client–server architecture** using Python socket programming. Multiple traffic signal clients send their signal status (RED, GREEN, YELLOW) to a **central monitoring server**. Communication between clients and the server is **secured using SSL/TLS encryption**.

The system simulates a **traffic signal monitoring network** where each signal device sends its status to a central server for monitoring.

---

## Features

* Client–Server communication using **TCP sockets**
* **Multiple concurrent clients** supported using multithreading
* **Secure communication using SSL/TLS**
* Traffic signal simulation (RED, GREEN, YELLOW)
* Real-time monitoring of signal status
* Self-signed SSL certificate generation

---

## System Architecture

Traffic Signal Clients
(Signal_101, Signal_102, Signal_103)
│
│  Secure TCP Socket (TLS)
▼
Central Monitoring Server
│
▼
Displays Traffic Signal Status

---

## Technologies Used

* Python
* Socket Programming
* SSL/TLS Security
* Multithreading
* Cryptography Library

---

## Project Structure

```
project-folder/
│
├── server.py              # Secure socket server
├── client.py              # Traffic signal client simulation
├── generate_cert.py       # SSL certificate generator
├── cert.pem               # SSL certificate
├── key.pem                # Private key
└── README.md
```

---

## How the System Works

1. The server starts and waits for incoming client connections.
2. Each traffic signal client establishes a **secure TLS connection** with the server.
3. Clients send signal status messages such as:

```
Signal_101 : RED
Signal_101 : GREEN
Signal_101 : YELLOW
```

4. The server receives and displays signal data in real time.
5. Multiple clients can connect simultaneously using **threads**.

---

## Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/traffic-signal-monitoring.git
cd traffic-signal-monitoring
```

### 2. Install required library

```
pip install cryptography
```

---

## Generate SSL Certificates

Run the following command to generate certificates:

```
python generate_cert.py
```

This will create:

```
cert.pem
key.pem
```

These files are used for secure TLS communication.

---

## Running the Project

### Step 1: Start the server

```
python server.py
```

Server output:

```
Secure Server started...
Waiting for signal clients...
```

### Step 2: Run the client

Open another terminal and run:

```
python client.py
```

Client output example:

```
Sent: Signal_101 : RED
Sent: Signal_101 : GREEN
Sent: Signal_101 : YELLOW
```

Server will display received signal data.

---

## Example Output

Server:

```
Connected to ('127.0.0.1', 61983)
Signal Data from ('127.0.0.1', 61983): Signal_101 : RED
Signal Data from ('127.0.0.1', 61983): Signal_101 : GREEN
Signal Data from ('127.0.0.1', 61983): Signal_101 : YELLOW
```

---

## Security Implementation

Secure communication is implemented using **SSL/TLS encryption**.
A self-signed certificate is generated using the **cryptography library**, and the server loads the certificate and private key to establish encrypted connections.

---

## Future Improvements

* Real-time web dashboard
* Database logging of signal data
* Integration with IoT traffic sensors
* Traffic optimization algorithms
* Real-time traffic analytics

---

## Conclusion

This project demonstrates **secure socket communication** between multiple clients and a central server. It highlights concepts such as **TCP networking, concurrent client handling, and TLS encryption** in a traffic signal monitoring scenario.

---
