from game import story

story = story.load_story('game.yaml')
print(f'Welcome to "{story.title}"')
print(story.prologue)
