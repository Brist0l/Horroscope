import socket

REMOTE_SERVER = "one.one.one.one"


def is_connected(hostname):
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except Exception as e:
        print(e)
        print("[-]Not Connected To Internet!")
        return False
