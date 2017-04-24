### Purpose

Given a list of pins knocked down per roll, calculate a single bowler's score in a 10 pin game.

### Dependencies

* Python 3.5.2
* pytest 3.0.6
  * https://docs.pytest.org/en/latest/getting-started.html
* Glasgow Haskell Compiler 7.10.3
* Test.HUnit (comes with GHC)

Other versions of these may work but have not been tested.

### Installation
```
git clone https://github.com/SSPJ/bowling-scorer.git
```
### Usage

**Python - interactive**
```
$ cd bowling-scorer/objectional
$ ./main.py 9 1 8 2 7 3 6 4 5 5 4 6 3 7 2 8 1 9 5 5 0
```
**Python - run tests**
```
$ cd bowling-scorer/objectional
$ pytest
```
**Haskell - interactive**
```
$ cd bowling-scorer/functional
$ ghci
ghci> :l BowlingScorer
ghci> game [9,1, 8,2, 7,3, 6,4, 5,5, 4,6, 3,7, 2,8, 1,9, 5,5,0]
```
**Haskell - run tests**
```
$ cd bowling-scorer/functional
$ runghc TestBowlingScorer.hs
```
### Files

/
|--functional
|  |-- BowlingScorer.hs       - functions to score a bowling game
|  |-- TestBowlingScorer.hs   - test cases
|
|--objectional
   |-- main.py                - user interface
   |-- bowling_scorer.py      - class for bowling game object
   |-- test_bowling_scorer.py - test cases

### Tools and References

* https://www.thoughtco.com/bowling-scoring-420895
  * detailed instructions for the game of bowling
* http://bowlinggenius.com/
  * used to generate test cases
