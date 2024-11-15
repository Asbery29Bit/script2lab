import socket

HOST = "127.0.0.1" 
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    message = b"it's working!!!"
    s.sendto(message, (HOST, PORT))
    data, addr = s.recvfrom(1024)
    print(f"Received {data} from {addr}")

print("Complete")