import socket

# TCP->クライアントの投げたデータを確かめる
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 50007))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("data:{}, addr:{}".format(data, addr))
                conn.sendall(b"Received: " + data)


# UDP>クライアントの投げたデータを確かめない
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr = s.recvfrom(1024)
        print("data: {}, addr: {}".format(data, addr))

# WEB Server
import http.server
import socketserver

with socketserver.TCPServer(('127.0.0.1', 8000),
        http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()