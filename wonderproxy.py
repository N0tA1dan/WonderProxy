import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# binds ip to socket
s.bind(("localhost", 4782))
s.listen()
conn, addr = s.accept()

# If the user is using this as a proxy, we will receive all data coming from the client.
usrdata = conn.recv()
