import socket
# pc_name = socket.gethostname()
# ipv4 = socket.gethostbyname(pc_name)
# print(pc_name, ipv4)
# host = "localhost"
# port = 4444
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #هنا بقوله اعمل كونكشن علي السوكت الي جوه السوكت                                                         #واختار منها ايبي فيرجن فور والبورت
# s.connect((host, port)) # هنا بقا بقلوه اعمل كونشن بالايبي والبورت الي مدهوملك فوق
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
