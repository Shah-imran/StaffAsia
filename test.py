from pyHook import HookManager, HookConstants
from win32gui import PumpMessages, PostQuitMessage, PumpWaitingMessages
from pynput.keyboard import Key, Controller
from threading import Thread
import var
from time import sleep
import sys


class Keystroke_Watcher:
    def __init__(self, master):
        self.hm = HookManager()
        self.hm.KeyDown = self.on_key_down
        self.hm.KeyUp = self.on_key_up
        self.hm.HookKeyboard()
        self.keys_held = set()  # set of all keys currently being pressed

    def get_key_combo_code(self):
        # find some way of encoding the presses.
        return '+'.join([HookConstants.IDToName(key) for key in self.keys_held])

    def on_key_down(self, event):
        try:
            self.keys_held.add(event.KeyID)
        finally:
            return True

    def on_key_up(self, event):
        keycombo = self.get_key_combo_code()
        print(keycombo)
        try:
            # Do whatever you want with your keycombo here
            pass
        finally:
            self.keys_held.remove(event.KeyID)
            return True


def main():
    watcher = Keystroke_Watcher
    PumpMessages()
    # PumpWaitingMessages()

if __name__ == '__main__':
    # watcher = Keystroke_Watcher()
    # PumpMessages()
    main()