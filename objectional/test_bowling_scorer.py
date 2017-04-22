#!/usr/bin/env python3

import bowling_scorer

### create game ###

def test_new_game():
  #a_game = Game()
  #assert(isinstance(a_game,Game))
  assert(1)

def test_new_game_with_too_many_entries():
  assert(0)

def test_new_game_with_too_few_entries():
  assert(0)

def test_new_game_with_not_integers():
  assert(0)

### score game ###

def test_all_gutter_balls():
  game = [0,0, 0,0, 0,0, 0,0, 0,0]
  expected = 0
  assert(0)

def test_all_strikes():
  game = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
  expected = 300
  assert(0)

def test_all_spares():
  game = [9,1, 8,2, 7,3, 6,4, 5,5, 4,6, 3,7, 2,8, 1,9, 5,5,0]
  expected = 141
  assert(0)

def test_open_frames():
  game = [9,0, 8,1, 7,2, 6,3, 5,4, 4,5, 3,6, 2,7, 1,8, 5,4]
  expected = 90
  assert(0)

def test_strikes_followed_by_spares():
  game = [10, 5,5, 5,0, 10, 0,10, 5,0, 10, 9,1, 5,0, 5,0]
  expected = 125
  assert(0)

def test_spares_followed_by_strikes():
  # also tests "zero ten" spare
  game = [5,5, 10, 5,0, 0,10, 10, 5,0, 9,1, 10, 5,0, 5,0]
  expected = 125
  assert(0)

def test_gutters_with_strikes():
  game = [0,0, 10, 0,0, 0,0, 10, 0,0, 10, 0,0, 0,0, 0,0]
  expected = 30
  assert(0)

### score game - misc end games ###

def test_tenth_frame_strike_gutter_strike():
  game = [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 10,0,10]
  expected = 20
  assert(0)

def test_tenth_frame_strike_spare():
  game = [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 10,5,5]
  expected = 20
  assert(0)

def test_tenth_frame_zero_spare():
  game = [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,10,2]
  expected = 12
  assert(0)

def test_tenth_frame_spare_strike():
  game = [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 5,5,10]
  expected = 20 
  assert(0)
