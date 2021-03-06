#!/usr/bin/env python3

## Seamus Johnston, 2017
## Comments marked with double ## are asides to my reviewers

class Game():
  ''' Stores integer list of bowling pins knocked down per
      roll and calculates game score.

      Atributes: list _scores, int _total_score, bool _scored '''

  def __init__(self,raw_scores):
    self._scores = []
    self._scored = False
    self.set_raw_scores(raw_scores)

## Getters and setters are not idiomatic in python, but
## we need an isolated copy of the integer list and
## should not rely on the caller to provide it

## int() will raise a VaueError on a non-numeric score

  def set_raw_scores(self,raw_scores):
    ''' Parameters: list raw_score
        Throws: IndexError, ValueError '''
    # data validation
    if not raw_scores or len(raw_scores) > 21:
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
    return self._scores

## The logic in score() is to traverse the list once and
## for each item, determine if it is the start of a bowling
## frame. If it is, check what kind of frame it is (strike,
## spare, open) and score it accordingly.

  def score(self):
    # don't recalc if total is up-to-date
    if self._scored == True:
      return self._total_score

    # reset total
    self._total_score = 0

    # switch:
    # a strike is a single item frame; if it has an odd
    # list index, the next frame will start on even
    switch = 2
    last_index = len(self._scores) - 1
    cur_frame = 1

    for i, cur in enumerate(self._scores):
      # skip this iteration if not at start of frame:
      # logical XOR with a switch tracks whether the start
      # of the frame should be on even or odd list indices
      if i > 0 and bool(i % 2) != bool(switch % 2):
        continue
      if cur == 10:
        switch = 1 if switch == 2 else 2

      # assign by frame: [cur,nxt] [trd,lst]
      if cur == 10:
        nxt = 0
        trd = self._scores[i+1] if last_index - i >= 1 else 0
        lst = self._scores[i+2] if last_index - i >= 2 else 0
      elif cur != 10:
        nxt = self._scores[i+1] if last_index - i >= 1 else 0
        trd = self._scores[i+2] if last_index - i >= 2 else 0
        lst = self._scores[i+3] if last_index - i >= 3 else 0

      # score *this* frame according to rules
      if cur == 10:          # strike
        self._total_score += cur + nxt + trd + lst
      elif cur + nxt == 10:  # spare
        self._total_score += cur + nxt + trd
      else:                  # open frame
        self._total_score += cur + nxt

      # avoid end of game edge cases
      if cur_frame == 10: break
      cur_frame += 1

    self._scored = True
    return self._total_score
