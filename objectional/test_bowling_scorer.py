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
  assert(0)

def test_all_strikes():
  assert(0)

def test_all_spares():
  assert(0)

def test_all_open_frames():
  assert(0)

def test_strikes_followed_by_spares():
  assert(0)

def test_spares_followed_by_strikes():
  assert(0)

def test_two_gutters_followed_by_strike():
  assert(0)

def test_spare_with_zero_ten():
  assert(0)

def test_open_frames_followed_by_strikes_and_spares():
  assert(0)

### score game - misc end games ###

def test_tenth_frame_strike_gutter_strike():
  # 10 0 10
  assert(0)

def test_tenth_frame_strike_spare():
  # 10 5 5
  assert(0)

def test_tenth_frame_open():
  # 5 4
  assert(0)

def test_tenth_frame_zero_spare():
  # 0 10 2
  assert(0)

def test_tenth_frame_spare_strike():
  # 5 5 10
  assert(0)
