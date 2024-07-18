import multiprocessing

import Web.WebMain
from BasicVoid import *


def main():
    sendInfo("欢迎使用CloudGeetest")
    sendInfo("作者By MossCG")
    Web.WebMain.startWeb()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
