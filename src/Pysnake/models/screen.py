from models.config import *

from turtle import Screen


class MainScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("white")
        self.screen.tracer(0)
        self.screen.title("Pysnake")

    def set_keys(self, key_set:dict):
        self.screen.listen()
        for (key, val) in key_set.items():
            self.screen.onkey(key, val)
