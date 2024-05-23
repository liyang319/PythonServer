import socket


if __name__ == '__main__':
    print("hello server")
    # 创建socket对象
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP和端口
    server_socket.bind(('127.0.0.1', 8001))
    # 监听连接
    server_socket.listen(5)
    print("Server is listening on port 8001...")
    while True:
        # 接受客户端连接
        client_socket, addr = server_socket.accept()
        print("Connected to client:", addr)
        while True:
            # 接收数据
            data = client_socket.recv(1024)
            if not data:
                break
            print("Received from client:", data.decode())
            # 原样返回数据
            client_socket.send(data)
        client_socket.close()
    server_socket.close()


