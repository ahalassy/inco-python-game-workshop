import yaml


def load_story(filename):
    with open(filename) as file:
        content = yaml.safe_load(file)
        return Story(content)


class Choice:

    @property
    def text(self):
        return self.content["choice"]

    @property
    def next(self):
        return self.content["next"]

    @property
    def response(self):
        return self.content["response"] if 'response' in self.content.keys() else None

    @property
    def items(self):
        return self.content["items"] if 'items' in self.content.keys() else []

    def __init__(self, content):
        self.content = content


class Action:

    @property
    def id(self):
        return self.content["action"]

    @property
    def name(self):
        return self.content["name"]

    @property
    def description(self):
        return self.content["desc"]

    def __init__(self, content):
        self.content = content
        self.choices = []
        for choice in self.content["choices"]:
            self.choices.append(Choice(choice))

    def find_choice_by_id(self, key):
        return self.choices[key]


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

    def find_action_by_id(self, action_id):
        actions = self.content["game"]["actions"]
        for action in actions:
            if action["action"] == action_id:
                return Action(action)

        return None
