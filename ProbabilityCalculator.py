import copy
import random

class Hat:

  def __init__(self, **list):
    self.list = list
    self.contents = [key for key, value in self.list.items() for i in range(value)]
    
  def get_contents(self):
    return self.contents

  #Old logic passed to list comprehension
  #def get_contents(self):
  #  for key, value in self.list.items():
  #    for _ in range(value):
  #      self.contents.append(key)
  #  return self.contents

  def draw(self, num_balls):
    if num_balls > len(self.contents):
      drawn_balls = self.contents
      self.contents = []
    else:
      drawn_balls = random.sample(self.contents, num_balls)
      for ball in drawn_balls:
        self.contents.remove(ball)
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn=1, num_experiments=0):
  match = 0
  #generating experimento
  for _ in range(num_experiments):
    find = 0
    #for secured that every experiment is independent
    copy_hat = copy.deepcopy(hat)
    #draw balls
    draw_experiments = copy_hat.draw(num_balls_drawn)
    draw_experiments_dict = {key: draw_experiments.count(key) for key in draw_experiments}          
    
    #draws
    for key, value in draw_experiments_dict.items():
      if key in expected_balls and value >= expected_balls[key]:
        find += 1
    if find == len(expected_balls):
      match += 1

  return match / num_experiments