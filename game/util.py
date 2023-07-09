import textwrap


def print_text(text):
    wrapped = textwrap.wrap(text, width=80)
    for line in wrapped:
        print(line)


def print_action(action):
    print(f"{action.name}\n")
    print_text(action.description)
    print()


def input_choice(action):
    while True:
        idx = 0
        while idx < len(action.choices):
            choice = action.choices[idx]
            idx += 1
            print(f'  {idx}) {choice.text}')

        key = input("\n What do you do?")
        choice = int(key) - 1
        return action.find_choice_by_id(choice)
