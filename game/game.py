from game import util


class Game:
    def __init__(self, story):
        self.story = story

    def play(self):
        self.prologue()

    def prologue(self):
        print(f'Welcome to "{self.story.title}"\n')
        util.print_text(self.story.prologue)
        print("\n\n\n")
