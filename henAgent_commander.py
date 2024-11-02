import socket
import argparse

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='Send a UDP packet to a specified IP and port.')
    parser.add_argument('ip', type=str, help='The IP address to send the packet to.')
    parser.add_argument('port', type=int, help='The port number to send the packet to.')
    parser.add_argument('message', type=str, help='The message to send.')

    # 解析命令行参数
    args = parser.parse_args()

    # 创建UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送数据
    sock.sendto(args.message.encode('utf-8'), (args.ip, args.port))
    print(f"Sent message: {args.message} to {args.ip}:{args.port}")

    # 接收回信
    data, addr = sock.recvfrom(4096)  # buffer size is 4096 bytes
    response = data.decode('utf-8')
    print(f"Received response: {response} from {addr}")

if __name__ == '__main__':
    main()