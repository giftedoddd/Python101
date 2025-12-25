from models.direction import Direction
from models.config import *

import turtle


class Snake:
    def __init__(self, head):
        self.blocks = [head]
        self.direction = Direction.RIGHT

    def add_tail(self, block):
        last = self.blocks[-1]
        block.goto(last.position())
        self.blocks.append(block)

    def move(self):
        for i in range(len(self.blocks) - 1, 0, -1):
            self.blocks[i].goto(self.blocks[i - 1].position())

        head = self.blocks[0]
        head.setheading(self.direction.value)
        head.forward(head.step)

    def hit_wall(self):
        head = self.blocks[0]
        x, y = head.position()

        screen = turtle.Screen()
        half_w = screen.window_width() / 2
        half_h = screen.window_height() / 2

        margin = STEP / 2

        return (
                x > half_w - margin or
                x < -half_w + margin or
                y > half_h - margin or
                y < -half_h + margin
        )

    def hit_self(self):
        head = self.blocks[0]
        for segment in self.blocks[1:]:
            if head.distance(segment) < STEP / 2:
                return True
        return False

