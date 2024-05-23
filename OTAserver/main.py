# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import socket

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # 创建TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP地址和端口
    server_socket.bind(('127.0.0.1', 9000))
    # 监听端口
    server_socket.listen(5)
    print("TCP server is listening on port 9000...")
    while True:
        # 等待客户端连接
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        # 接收客户端发送的数据
        data = client_socket.recv(1024)
        if data:
            print(f"Received data: {data.decode()}")
            # 发送响应数据
            response = "Hello from server"
            client_socket.send(response.encode())
            # 关闭客户端连接
            # client_socket.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
