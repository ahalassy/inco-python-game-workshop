class Game:
    def __init__(self, story):
        self.story = story

    def play(self):
        self.prologue()

    def prologue(self):
        print(f'Welcome to "{self.story.title}"')
        print(self.story.prologue)
