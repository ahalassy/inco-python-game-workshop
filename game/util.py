import re
import textwrap


def print_text(text):
    wrapped = textwrap.wrap(text, width=80)
    for line in wrapped:
        print(line)


def print_action(action):
    print(f"{action.name}:")
    print_text(action.description)
    print()


def print_inventory(game):
    if len(game.inventory) == 0:
        print("Your backpack is empty.\n")
        return

    print("You have the following things in your backpack:")
    for item in game.inventory:
        print(f"   - {item}")
    print()


def validate_input(key):
    pattern = re.compile('^\s*([0-9]+||[qQiI])\s*$')
    return pattern.match(key)


def input_choice(game, action):
    choices = game.get_choices_for(action)
    while True:
        idx = 0
        while idx < len(choices):
            choice = choices[idx]
            idx += 1
            print(f'  {idx}) {choice.text}')

        print("  ---")
        print("  I) View inventory")
        print("  Q) Quit game")

        key = input("\n What do you do? ")
        if not validate_input(key):
            print("\n ** This is not possible!")
            continue

        if key == 'q' or key == 'Q':
            return None

        if key == 'i' or key == 'I':
            return -2

        choice = int(key) - 1
        if choice < 0 or choice >= len(choices):
            print("\n ** This is not possible!")
            continue

        return choices[choice]
