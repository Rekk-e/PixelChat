import socket, json
import os
import time
from _thread import start_new_thread
from pyngrok import ngrok
global sockets

def disconnect(addr):
    print('Соединение с ' + str(addr) + ' разорвано')

    data = sockets[str(addr)][1]
    send_data = {'nick': 'server',
                 'color': 'yellow',
                 'message': data["nick"] + ' disconnected'}
    send_data = json.dumps(send_data)
    sockets.pop(str(addr))

    for soc in sockets:
        sockets[soc][0].send(bytes(send_data, 'utf-8'))


def sendSmile(data, addr, mess):
    for soc in sockets:
        send_data = {'nick': data['nick'],
                    'color': data['color'],
                    'message': mess}
        send_data = json.dumps(send_data)
        sockets[soc][0].send(bytes(send_data, 'utf-8'))

def sendHelp(addr):
    for soc in sockets:
        if soc == str(addr):
            send_data = {'nick': 'server',
                         'color': 'yellow',
                         'message': '/clear, /smile, /angry, /shock'}
            send_data = json.dumps(send_data)
            sockets[soc][0].send(bytes(send_data, 'utf-8'))

def sendToClient(data, addr):
    for soc in sockets:
        if soc != str(addr):
            sockets[soc][0].send(data)

def threaded(c, addr):
    while True:
        try:
            data = c.recv(1024)
            print(data)
        except ConnectionResetError:
            disconnect(addr)
            break

        if data:
            jData = data.decode('utf-8')
            jData = json.loads(jData)
            if jData["message"] == '/smile':
                mess = '😆😆😆'
                sendSmile(jData, addr, mess)
            elif jData["message"] == '/angry':
                mess = '😡😡😡'
                sendSmile(jData, addr, mess)
            elif jData["message"] == '/shock':
                mess = '😱😱😱'
                sendSmile(jData, addr, mess)
            elif jData["message"] == '/help':
                sendHelp(addr)
            else:
                sendToClient(data, addr)
        else:
            print('Пришла пустая строка')
            time.sleep(5)
    c.close()

host = ''
port = 22

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1000)



sockets = {}
while True:
    sock, addr = s.accept()
    sockets[str(addr[1])] = [sock]
    print('Connected to :', addr[0], ':', addr[1])
    data = sock.recv(1024).decode('utf-8')
    data = json.loads(data)
    sockets[str(addr[1])].append(data)
    send_data = {'nick':'server',
                 'color':data["color"],
                 'message':data["message"]}
    send_data = json.dumps(send_data)

    for soc in sockets:
        sockets[soc][0].send(bytes(send_data, 'utf-8'))

    start_new_thread(threaded, (sock, addr[1], ))



