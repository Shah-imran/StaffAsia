from pyHook import HookManager
from win32gui import PumpMessages, PostQuitMessage

class Keystroke_Watcher(object):
    def __init__(self):
        self.hm = HookManager()
        self.hm.KeyDown = self.on_keyboard_event
        self.hm.HookKeyboard()


    def on_keyboard_event(self, event):
        try:
            key = event.KeyID
            if key == 81:
                self.shutdown()
            elif event.K
        finally:
            return True

    def your_method(self):
        print("")

    def shutdown(self):
        PostQuitMessage(0)
        self.hm.UnhookKeyboard()


watcher = Keystroke_Watcher()
PumpMessages()