import multiprocessing

import Web.WebMain
from BasicVoid import *


def main():
    sendInfo("欢迎使用CloudGeetest")
    sendInfo("作者By MossCG")
    sendInfo("版本V1.0.0.0.0000")
    Web.WebMain.startWeb()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
