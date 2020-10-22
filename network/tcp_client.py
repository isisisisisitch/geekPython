import socket

if __name__ == '__main__':
    # 1.创建客户端套接字对象
    #AF_INET:ipv4
    #SOCK_STREAM: tcp
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 和服务端套接字建立连接

    tcp_client_socket.connect(("192.168.1.40", 9090))

    # 发送数据
    send_content = input("jim said:")#input()
    send_data = send_content.encode("utf-8")
    tcp_client_socket.send(send_data)
    # 接收数据
    recv_data = tcp_client_socket.recv(1024)
    recv_content = recv_data.decode("utf-8")
    print(recv_content)
    # 关闭客户端套接字
    tcp_client_socket.close()