from tkinter import Tk
import var
from time import sleep

class copy(object):
    def __init__(self):
        pass
    def copyClipboard(self):
        try:
            temp = Tk().clipboard_get()
            return temp
        except Exception as e:
            print(e)
        finally:
            pass
    def clear(self):
        Tk().clipboard_clear()

if __name__ == '__main__':
    copyAction = copy()
    print(copyAction.copyClipboard)