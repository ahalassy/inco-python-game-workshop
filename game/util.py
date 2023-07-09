import textwrap


def print_text(text):
    wrapped = textwrap.wrap(text, width=80)
    for line in wrapped:
        print(line)
    print()