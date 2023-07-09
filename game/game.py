from game import util


class Game:
    def __init__(self, story):
        self.story = story
        self.inventory = []

    def handle_action(self, action_id):
        action = self.story.find_action_by_id(action_id)
        util.print_action(action)
        choice = util.input_choice(action)

        if not choice:
            return None

        if choice == -2:
            util.print_inventory(self)
            return action_id

        self.handle_choice(choice)

        return choice.next

    def handle_choice(self, choice):
        # Add items if any:
        for item in choice.items:
            self.inventory.append(item)
            print(f"A(n) {item} added to your backpack.")

    def play(self):
        self.prologue()
        next_action = self.story.start
        while next_action:
            next_action = self.handle_action(next_action)

        print("Thank you for playing with me, bye!")

    def prologue(self):
        print(f'Welcome to "{self.story.title}"\n')
        util.print_text(self.story.prologue)
        print("\n")


