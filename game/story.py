import yaml


def load_story(filename):
    with open(filename) as file:
        content = yaml.safe_load(file)
        return Story(content)


class Story:

    @property
    def title(self):
        return self.content["game"]["title"]

    @property
    def prologue(self):
        return self.content["game"]["prologue"]

    @property
    def start(self):
        return self.content["game"]["start"]

    def __init__(self, content):
        self.content = content
