import win32api
import time
for i in range(1,40):
    win32api.ShellExecute(0,'open',"python","libuv.test.tcpclient.py","",1)
    time.sleep(2)
