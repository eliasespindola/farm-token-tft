import pkg_resources

pkg_resources.require("PyAutoGUI==0.9.50")
pkg_resources.require("opencv-python==4.5.1.48")
pkg_resources.require("python-imageseach-drov0==1.0.6")

import pyautogui as auto
from python_imagesearch.imagesearch import imagesearch as search
import time
from printy import printy
from printy import inputy

auto.FAILSAFE = False


def onscreen(path, precision=0.8):
    return search(path, precision)[0] != -1


def search_to(path):
    pos = search(path)
    if onscreen(path):
        auto.moveTo(pos)
        # print(path + " found")
        return pos


def click_key(key, delay=.1):
    auto.keyDown(key)
    time.sleep(delay)
    auto.keyUp(key)


def click_left(delay=.1):
    auto.mouseDown()
    time.sleep(delay)
    auto.mouseUp()


def click_right(delay=.1):
    auto.mouseDown(button='right')
    time.sleep(delay)
    auto.mouseUp(button='right')


def click_to(path, delay=.1):
    if onscreen(path):
        auto.moveTo(search(path))
        click_left(delay)
        # print(path + " clicked")


def find_match():
    if onscreen("./captures/tft logo.png"):
        click_to("captures/find_match_ready.png")
    wait_match()


def wait_match():
    while not onscreen("./captures/loading.png"):
        time.sleep(1)
        click_to("./captures/accept.png")
        exit()


def exit():
    if onscreen("./captures/exit-now.png"):
        while onscreen("./captures/exit-now.png"):
            time.sleep(1)
            click_to("./captures/exit-now.png")
    rematch()


def rematch():
    if onscreen("./captures/play_again.png"):
        print("rematch")
        while onscreen("./captures/play_again.png"):
            time.sleep(2)
            click_to("./captures/play_again.png")
            print("chamando find match")

def main():
    while True:
        find_match()
        wait_match()
        exit()
        rematch()

auto.alert("Press OK when you're in a TFT lobby!\n")
print("Bot started, queuing up!")
main()

