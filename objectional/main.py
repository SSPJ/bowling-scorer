#!/usr/bin/env python3

## Seamus Johnston, 2017

from bowling_scorer import Game
from sys import argv,exit,stderr

if __name__ == "__main__":
  try:
    our_score = Game(argv[1:]).score()
  except ValueError:
    stderr.write("All rolls must be numbers seperated by spaces, eg 10 3 5\n")
    exit(1)
  except IndexError:
    stderr.write("A valid game must have fewer than 21 rolls\n")
    exit(1)

  print(our_score)
