import re
import textwrap


def print_text(text):
    wrapped = textwrap.wrap(text, width=80)
    for line in wrapped:
        print(line)


def print_action(action):
    print(f"{action.name}\n")
    print_text(action.description)
    print()


def validate_input(key):
    pattern = re.compile('^\s*([0-9]+||[qQ])\s*$')
    return pattern.match(key)

def input_choice(action):
    while True:
        idx = 0
        while idx < len(action.choices):
            choice = action.choices[idx]
            idx += 1
            print(f'  {idx}) {choice.text}')

        print("  ---")
        print("  Q) Quit game")

        key = input("\n What do you do?")
        if not validate_input(key):
            print("\n ** This is not possible!")
            continue

        if key == 'q' or key == 'Q':
            return None

        choice = int(key) - 1
        if choice < 0 or choice >= len(action.choices):
            print("\n ** This is not possible!")
            continue

        return action.find_choice_by_id(choice)
