# Python-socket
- 环境配置：python3
- 创建socket对象，绑定ip和端口，开启监听
- 定义每次读取文件大小，使用文件句柄将文件内容定义为二进制后发送
- 使用字典存储fd和socket对象的映射关系
- 使用json和struct构建自定义报头，解决了粘包问题
