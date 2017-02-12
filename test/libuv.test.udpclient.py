import _socket
import  time
import  uuid
import  win32api
import  win32con

host = "10.2.95.15"

port = 3490

print "python udp echo server test"

s = _socket.socket(_socket.AF_INET,_socket.SOCK_DGRAM)

s.setsockopt(_socket.SOL_SOCKET,_socket.SO_REUSEADDR,1)

msg = ""

id = uuid.uuid1()

for i in range(1,100000):
    if i % 2 == 0:
        msg = "ID:%s,NO:%d hello libuv udp" % (id,i)
    else:
        msg = "ID:%s,NO:%d I am here" %(id,i)

    s.sendto(msg,(host,port))

    message,address = s.recvfrom(1024)

    print "Got data from ",address,":",message

    if message != msg:
        win32api.MessageBox(0,'uuid is not match','error',win32con.MB_OK)

    time.sleep(0.1)