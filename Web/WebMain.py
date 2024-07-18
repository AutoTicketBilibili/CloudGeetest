import json
import multiprocessing
import time
from urllib.parse import parse_qs, urlparse

import BasicVoid
import Geetest.GeetestLocal

import socket


# noinspection PyBroadException
def handleClient(client):
    try:
        request = client.recv(1024)
        url = request.decode("utf-8").splitlines()[0].split()[1]
        params = parse_qs(urlparse(url).query)
        response = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n{getResponse(params)}\r\n".encode("utf-8")
        client.send(response)
        client.shutdown(socket.SHUT_RDWR)
        client.close()
    except Exception as e:
        print(e)
        pass



# noinspection PyBroadException
def getResponse(query):
    BasicVoid.sendInfo(str(query))
    timeStart = time.time()
    try:
        data = Geetest.GeetestLocal.passGeetest(query.get('gt', [''])[0], query.get('c', [''])[0])
    except Exception as e:
        print(e)
        data = {"success": False}
    timeEnd = time.time()
    data["timeUsed"] = timeEnd - timeStart
    BasicVoid.sendInfo(str(data))
    return json.dumps(data)


def startWeb():
    BasicVoid.sendInfo("正在初始化Web")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", 8888))
    server.listen(9999)
    BasicVoid.sendInfo("服务器已在 localhost:8888 端口开始监听......")
    while True:
        client, addr = server.accept()
        process = multiprocessing.Process(target=handleClient, args=(client,))
        process.start()