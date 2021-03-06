import socket
import struct
import json
sk = socket.socket()
# buffer = 4096
buffer = 1024 #每次接收数据的大小
sk.bind(('127.0.0.1',8090))
sk.listen()

conn,addr = sk.accept()
#接收
head_len = conn.recv(4)
head_len = struct.unpack('i',head_len)[0] #解包
json_head = conn.recv(head_len).decode('utf-8') #反序列化
head = json.loads(json_head)
filesize = head['filesize']
with open(head['filename'],'wb') as f:
    while filesize:
        if filesize >= buffer: #>=是因为如果刚好等于的情况出现也是可以的。
            content = conn.recv(buffer)
            f.write(content)
            filesize -= buffer
        else:
            content = conn.recv(buffer)
            f.write(content)
            break

conn.close()
sk.close()