import socket
host = input("type your ip address ")
try:
    for port in range(1, 1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"the port is open {port}")


except:
    print("the port is close")
