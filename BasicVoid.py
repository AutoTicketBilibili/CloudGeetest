import datetime
import sys


def sendInfo(message):
    sendMsg("37", "[Info] " + message)


def sendMsg(color, message):
    print("\033[0;" + color + "m[" + datetime.datetime.now().strftime('%H:%M:%S %f')[:-2] + "]" + message + "\033[0m")
    sys.stdout.flush()
