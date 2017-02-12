import _socket,time,uuid,win32con,win32api,json
import message
import binascii


header = message.frameheader(msg_id=12, message='hello world')

print message.wrapptobinary(header)


class logelement():
    def __init__(self):
        pass

isotimeformat = '%Y-%m-%d %X'


# element = logelement()
# element.msg = 'hello libuv tcp'
# element.des = "python"
# element.uuid = id.__str__()
# element.id  = i
# element.timestap = time.strftime(isotimeformat)

def tcpClient():
    clisock = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)
    clisock.connect(('localhost', 3491))
    suuid = uuid.uuid1().__str__()
    for i in range(1, 1000):
        header = message.frameheader(msg_id=i, message= suuid)
        (_, buf) = message.wrapptobinary(header)
#        print binascii.hexlify(buf)
        clisock.send(buf)
        time.sleep(0.5)
    clisock.close()
    print "---------------------------------------------"


if __name__ == '__main__':
    start = time.time()
    tcpClient()
    print 'total time ', time.time() - start