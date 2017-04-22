#!/usr/bin/env python3

from bowling_scorer import Game
import pdb

pdb.set_trace()
game = [9,0, 8,1, 7,2, 6,3, 5,4, 4,5, 3,6, 2,7, 1,8, 5,4]
expected = 90
actual = Game(game).score()
