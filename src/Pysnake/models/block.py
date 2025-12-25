class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.__kind = None
        self.__cordinate = [0, 0]
        self.__step = STEP
        self.register_shapes()

    def __repr__(self):
        return f"Shape: {self.kind}, Cordinate: [{self.__cordinate[0], self.__cordinate[1]}]"

    @classmethod
    def head(cls):
        block = cls()
        block.kind = Kinds.HEAD
        block.shape(HEAD_SHAPE_PATH)
        block.speed(SPEED)
        block.penup()
        return block

    @classmethod
    def tail(cls):
        block = cls()
        block.kind = Kinds.TAIL
        block.shape(TAIL_SHAPE_PATH)
        block.speed(SPEED)
        block.penup()
        return block

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind=Kinds.TAIL):
        if kind == Kinds.HEAD:
            kind_name = Kinds.HEAD
        else:
            kind_name = Kinds.TAIL

        self.__kind = kind_name

    @property
    def step(self):
        return self.__step

    def size(self):
        if self.kind == Kinds.HEAD:
            return HEAD_SIZE
        else:
            return TAIL_SIZE

    @staticmethod
    def register_shapes():
        turtle.register_shape(HEAD_SHAPE_PATH)
        turtle.register_shape(TAIL_SHAPE_PATH)
