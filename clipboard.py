from tkinter import Tk
import var
from time import sleep

class copy(object):
    def __init__(self):
        pass
    def copyClipboard(self):
        try:
            print(Tk().clipboard_get())
        except Exception as e:
            print(e)
        finally:
            pass

if __name__ == '__main__':
    copyAction = copy()
    print(copyAction.copyClipboard)