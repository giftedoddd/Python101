import turtle


class __Menu:
    def __init__(self, screen, entries):
        self.__entries = entries
        self.__selected = 0

        self.__writer = turtle.Turtle()
        self.__writer.hideturtle()
        self.__writer.penup()

        self.screen = screen

        self.draw()


    def draw(self):
        self.__writer.clear()

        spacing = 40
        start_y = (len(self.__entries) - 1) * spacing / 2

        for i, text in enumerate(self.__entries):
            y = start_y - i * spacing
            self.__writer.goto(0, y)

            if i == self.__selected:
                self.__writer.write(
                    f"> {text} <",
                    align="center",
                    font=("Arial", 24, "bold")
                )
            else:
                self.__writer.write(
                    text,
                    align="center",
                    font=("Arial", 24, "normal")
                )

        self.screen.update()

    def up(self):
        self.__selected = (self.__selected - 1) % len(self.__entries)
        self.draw()

    def down(self):
        self.__selected = (self.__selected + 1) % len(self.__entries)
        self.draw()

    def select(self):
        choice = self.__entries[self.__selected]
        print(choice)
        self.on_select(choice)

    def on_select(self, choice):
        pass

    def get_key_set(self):
        key_set = {
            self.up: "Up",
            self.down: "Down",
            self.select: "Return"
        }
        return key_set


class MainMenu(__Menu):
    def on_select(self, choice):
        choice = choice.upper()
        if choice == "START":
            print("Start game")
            turtle.clearscreen()
            # call game start here

        elif choice == "SETTINGS":
            print("Open settings")
            # later you can open another menu

        elif choice == "EXIT":
            turtle.bye()
