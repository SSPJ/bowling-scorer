#!/usr/bin/env python3

## Seamus Johnston, 2017
## Comments marked with double ## are asides to my reviewers

class Game():

  _scores = []
  _total_score

  def __init__(self,raw_scores):
    set_score(raw_scores)

## getters and setters are not idiomatic in python, but arrays
## are passed by referrence so this avoids confusion

  def set_score(raw_scores):
    for score in raw_scores:
      _scores.append(int(score))

  def get_scores(self):
    return _scores

  def score(self):
    # score code goes here
    return 1
