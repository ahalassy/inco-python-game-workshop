import random

from game import util


class Game:
    def __init__(self, story):
        self.story = story
        self.inventory = []
        self.reputation = 0
        self.strength = 0

    def handle_fight(self, choice):
        fight = choice.fight_results
        if not fight:
            return None

        (win, loss) = fight
        outcome = random.randint(1, 6)
        if outcome > 3:
            print("You won the fight, you lucky man!")
            return win
        else:
            print("You lost the fight, and barely escaped.")
            return loss

    def handle_action(self, action_id):
        action = self.story.find_action_by_id(action_id)
        util.print_action(action)
        if action.is_end():
            return -1

        choice = util.input_choice(action)

        if not choice:
            return None

        if choice == -2:
            util.print_inventory(self)
            return action_id

        self.handle_choice(choice)

        fight_outcome = self.handle_fight(choice)
        return fight_outcome if fight_outcome else choice.next

    def handle_choice(self, choice):
        # Handle response if any:
        if choice.response:
            util.print_text(choice.response)

        # Add items if any:
        for item in choice.items:
            self.inventory.append(item)
            print(f"A(n) {item} added to your backpack.")

        # Handle hooks:
        for hook in choice.hooks:
            method = getattr(self, hook)
            method()

    def play(self):
        self.prologue()
        next_action = self.story.start
        while next_action:
            next_action = self.handle_action(next_action)
            if next_action == -1:
                print("The end")
                break

        print("Thank you for playing with me, bye!")

    def prologue(self):
        print(f'Welcome to "{self.story.title}"\n')
        util.print_text(self.story.prologue)
        print("\n")

    # Hooks:
    def increase_reputation(self):
        self.reputation += 1

    def decrease_reputation(self):
        self.reputation += 1

    def increase_strength(self):
        self.strength += 1
        print(f"Your strength increased to {self.strength}.")

