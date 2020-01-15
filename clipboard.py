from tkinter import Tk
import threading
import var
import time
import keyboard


class copy(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.threadID = threadID
        self.name = name
    def run(self):
        try:
            while var.runStatus == True:
                try:
                    if keyboard.is_pressed('ctrl+c'):
                        print(Tk().clipboard_get())
                        var.data.append(Tk().clipboard_get())
                    elif keyboard.is_pressed('shift+n'):
                        print("new line")
                    elif keyboard.is_pressed('ctrl+z'):
                        print("previous")
                    elif keyboard.is_pressed('ctrl+shift+z'):
                        print("next")
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        finally:
            print(var.runStatus)
            pass

    def terminate(self):
        if var.terminate == True:
            print("terminate")
            raise Exception("Terminate Thread")

if __name__ == '__main__':
    var.runStatus = True
    copy(0, "thread-0").start()
    while True:
        pass
        time.sleep(1)