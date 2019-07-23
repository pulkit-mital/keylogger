import keylogger


class KeyloggerClient(object):

    def __init__(self):
        print('Keylogger Client')

    def keyboard_event(self, event):
        print(event.key)

    def start(self):
        key_logger = keylogger.Keylogger()
        key_logger.logger = self.keyboard_event
        key_logger.start()


def main():
    key_logger_client = KeyloggerClient()
    key_logger_client.start()


if __name__ == '__main__':
    main()
