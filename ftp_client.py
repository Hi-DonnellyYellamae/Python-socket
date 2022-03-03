import os
import json
import socket
import struct
sk = socket.socket()
sk.connect(('127.0.0.1',8090))
buffer = 1024 #读取文件的时候，每次读取的大小
head = {
            'filepath':r'C:\Users\Aaron\Desktop\新建文件夹', #需要下载的文件路径，文件所在的文件夹
            'filename':'config',  #改成上面filepath下的一个文件
            'filesize':None,
        }

file_path = os.path.join(head['filepath'],head['filename'])
filesize = os.path.getsize(file_path)
head['filesize'] = filesize
# json_head = json.dumps(head,ensure_ascii=False)  #字典转换成字符串
json_head = json.dumps(head)  #字典转换成字符串
bytes_head = json_head.encode('utf-8') #字符串转换成bytes类型
print(json_head)
print(bytes_head)

#计算head的长度
head_len = len(bytes_head) #报头长度
pack_len = struct.pack('i',head_len)
print(head_len)
print(pack_len)
sk.send(pack_len)  #先发送报头长度
sk.send(bytes_head) #再发送bytes类型的报头


with open(file_path,'rb') as f:
    while filesize:
        if filesize >= buffer:
            content = f.read(buffer) #每次读取出来的内容
            sk.send(content)
            filesize -= buffer #每次减去读取的大小
        else: #剩余的不够一次读取的大小了，只要把剩下的读取出来发送过去就行了
            content = f.read(filesize)
            sk.send(content)
            break

sk.close()