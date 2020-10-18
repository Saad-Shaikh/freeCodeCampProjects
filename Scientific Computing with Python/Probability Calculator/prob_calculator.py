import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
  
  def draw(self, ballsToDraw):
    if len(self.contents) <= ballsToDraw:
      return self.contents
    else:
      retList = []
      for i in range(ballsToDraw):
        ball = random.choice(self.contents)
        retList.append(ball)
        self.contents.remove(ball)
      return retList


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0

  for i in range(num_experiments):
    copiedHat = copy.deepcopy(hat)
    ballsDrawn = copiedHat.draw(num_balls_drawn)
    ballsDrawnDict = Counter(ballsDrawn)

    flag = True
    for key,value in expected_balls.items():
      if ballsDrawnDict[key] < value:
        flag = False

    if flag == True:
      count += 1
  
  probability = count/num_experiments
  return probability