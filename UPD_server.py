import socket

HOST = "127.0.0.1"
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        print(f"Received {data} from {addr}")
        s.sendto(data, addr)

print("Complete")