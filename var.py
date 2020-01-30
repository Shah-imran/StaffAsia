from queue import Queue
from collections import deque

runStatus = False
terminate = False
quitingStatus = False
stop = True
tableRowPos = 1
tableColPos = 0
prevR = 0
prevC = 0
preTabPos = []
csvPath = "out.csv"
data = list()
cText = Queue()
stack = deque()
GUI = object()

keymap = {
    81: {'responsibility': "Stop", 'char': "q"},
    82: {'responsibility': "Remove", 'char': "r"},
    67: {'responsibility': "Copy", 'char': "c"},
    90: {'responsibility': "Previous", 'char': "z"},
    78: {'responsibility': "NewLine", 'char': "n"},
    38: {'responsibility': "Up", 'char': "up"},
    40: {'responsibility': "Down", 'char': "down"},
    37: {'responsibility': "Left", 'char': "left"},
    39: {'responsibility': "Right", 'char': "right"},
}