import time, socket, optparse

parser = optparse.OptionParser()
parser.add_option('-i', dest='ip', default='')
parser.add_option('-p', dest='port', type='int', default=12345)
(options, args) = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((options.ip, options.port))
s.listen(5)

f = open('foo.txt','w')
f.write("Waiting for the connection\r\n")
f.flush()
while True:
    sock, addr = s.accept()
    f.write("Accept new connection\r\n")
    f.flush()
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        f.write(('Hello, %s!\r\n' % data))
        f.flush()
    sock.close()
    print('Connection from %s:%s closed.' % addr)
