from game import util


class Game:
    def __init__(self, story):
        self.story = story

    def handle_action(self, action_id):
        action = self.story.find_action_by_id(action_id)
        util.print_action(action)
        choice = util.input_choice(action)

        return choice.next

    def play(self):
        self.prologue()
        next_action = self.story.start
        while next_action:
            next_action = self.handle_action(next_action)

    def prologue(self):
        print(f'Welcome to "{self.story.title}"\n')
        util.print_text(self.story.prologue)
        print("\n")

