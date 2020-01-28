from pyHook import HookManager, HookConstants, GetKeyState
from win32gui import PumpMessages, PostQuitMessage, PumpWaitingMessages
from pynput.keyboard import Key, Controller
from threading import Thread
import calTablePos
import var
from time import sleep
import sys
import clipboard



class Keystroke_Watcher(object):
    def __init__(self):
        self.hm = HookManager()
        self.hm.KeyDown = self.on_keyboard_event
        self.hm.HookKeyboard()
        self.copy = clipboard.copy()



    def on_keyboard_event(self, event):
        try:
            if GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == 81:
                print("Removal of hookmanager")
                self.shutdown()
            elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == 67:
                sleep(0.3)
                temp = self.copy.copyClipboard()
                print("ctrl + c - copy -" + temp )
                var.cText.put([temp, (var.tableRowPos, var.tableColPos)])
                if var.tableRowPos == (var.prevR - 1) and var.tableColPos == (var.prevC - 1):
                    pass
                elif var.tableColPos == (var.prevC - 1):
                    var.tableColPos = 0
                    var.tableRowPos += 1
                else:
                    var.tableColPos += 1

            elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == 90:
                if var.tableRowPos == 0 and var.tableColPos == 0:
                    pass
                elif var.tableColPos == 0:
                    var.tableColPos = var.prevC - 1
                    var.tableRowPos -= 1
                else:
                    var.tableColPos -= 1
                var.cText.put(["", (var.tableRowPos, var.tableColPos)])
                print("ctrl + z - revert")
            elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == 82:
                var.cText.put([" ", (var.tableRowPos, var.tableColPos)])
                var.tableRowPos += 1
                sleep(0.01)
                var.tableRowPos -= 1
                print("ctrl + r - remove")
            elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == 78:
                var.tableColPos = 0
                var.tableRowPos += 1
                print("ctrl + r - new line")
            elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == 38:
                if var.tableRowPos > 0:
                    var.tableRowPos -= 1
                print("up")
                print(var.tableRowPos, var.tableColPos)
            elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == 40:
                if var.tableRowPos < (var.prevR - 1):
                    var.tableRowPos += 1
                print("down")
                print(var.tableRowPos, var.tableColPos)
            elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == 37:
                if var.tableColPos > 0:
                    var.tableColPos -= 1
                print("left")
                print(var.tableRowPos, var.tableColPos)
            elif GetKeyState(HookConstants.VKeyToID('VK_CONTROL')) and event.KeyID == 39:
                if var.tableColPos < (var.prevC - 1):
                    var.tableColPos += 1
                print("right")
                print(var.tableRowPos, var.tableColPos)
            else:
                pass
        except Exception as e:
            print(e)
        finally:
            return True

    def shutdown(self):
        # PostQuitMessage(0)
        self.hm.UnhookKeyboard()
        print("shutdown after pressing q")
        var.runStatus = False


def main():
    try:
        watcher = Keystroke_Watcher()
        # PumpMessages()
        PumpWaitingMessages()
        # Thread(target=calTablePos.main, args=(GUI, ), daemon=True).start()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # watcher = Keystroke_Watcher()
    # PumpMessages()
    main()