from pyHook import HookManager
from win32gui import PumpMessages, PostQuitMessage
from threading import Thread
import var
from time import sleep
from pynput.keyboard import Key, Controller
import sys



class Keystroke_Watcher(object):
    def __init__(self):
        self.hm = HookManager()
        self.hm.KeyDown = self.on_keyboard_event
        self.hm.HookKeyboard()
        # Thread(target=self.quitingActivity, daemon=True).start()


    def on_keyboard_event(self, event):
        try:
            key = event.KeyID
            if key == 81:
                self.shutdown()
            else:
                print(key)
        finally:
            return True

    def shutdown(self):
        var.quitingStatus = True
        PostQuitMessage(0)
        self.hm.UnhookKeyboard()

    # def quitingActivity(self):
    #     while True:
    #         print(var.quitingStatus)
    #         if var.quitingStatus == True:
    #             print("here")
    #             PostQuitMessage(0)
    #             self.hm.UnhookKeyboard()
    #             sys.exit()
    #             break
    #         sleep(0.1)

def main():
    watcher = Keystroke_Watcher()
    PumpMessages()

if __name__ == '__main__':
    watcher = Keystroke_Watcher()
    PumpMessages()