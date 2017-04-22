#!/usr/bin/env python3

## Seamus Johnston, 2017
## Comments marked with double ## are asides to my reviewers

class Game():
  ''' Stores integer list of bowling pins knocked down per
      roll and calculates game score.

      Atributes: list _scores, int _total_score, bool _scored '''

  def __init__(self,raw_scores):
    set_raw_scores(raw_scores)

## Getters and setters are not idiomatic in python, but
## we need an isolated copy of the integer list and
## should not rely on the caller to provide it

## int() will raise a VaueError on a non-numeric score

  def set_raw_scores(raw_scores):
    ''' Parameters: list raw_score
        Throws: IndexError, ValueError '''
    # data validation
    if len(raw_scores) > 21:
      raise IndexError
    for score in raw_scores:
      # data validation
      s = int(score)
      if s < 0 or s > 10:
        raise ValueError
      # store data
      self._scores.append(s)
    # mark total outdated
    self._scored = False

  def get_raw_scores(self):
    return _scores

  def score(self):
    # don't recalc if total is up-to-date
    if self._scored == True:
      return _total_score
    # make sure that _scores is not null
    # score code goes here
    self._scored = True
    return 1
