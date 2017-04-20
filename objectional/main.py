#!/usr/bin/env python3

class Game():

  _scores = []

  def __init__(self,raw_scores):
    for score in raw_scores:
      _scores.append(int(score))

  def score(self):
    # score code goes here
    return 1
