from game import story
from game.game import Game

story = story.load_story('game.yaml')
game = Game(story)

game.play()
