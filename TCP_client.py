import socket

HOST = "127.0.0.1"
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = b"it's working!!!"
    s.sendall(message)
    data = s.recv(1024)
    print(f"Received {data}")

print("Complete")