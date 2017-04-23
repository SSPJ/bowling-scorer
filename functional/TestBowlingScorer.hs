module TestBowlingScorer where

import Test.HUnit
import BowlingScorer

--- create game ---

test_too_many_entries :: Test
test_too_many_entries =
  TestCase $ assertEqual "test_too_many_entries"
                         Nothing (game([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0]))

test_values_bigger_than_eleven :: Test
test_values_bigger_than_eleven =
  TestCase $ assertEqual "test_values_bigger_than_eleven" 
                         Nothing (game([10, 11, 10, 10, 10, 10, 10, 10, 9, 10, 10, 10]))

test_negative_values :: Test
test_negative_values =
  TestCase $ assertEqual "test_negative_values"
                         Nothing (game([10, 11, 10, 10, 10, 10, 10, 10, 9, 10, 10, 10]))

--- score game ---

test_all_gutter_balls :: Test
test_all_gutter_balls =
  TestCase $ assertEqual "test_all_gutter_balls"
                         (Just 0) (game([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0]))

test_all_strikes :: Test
test_all_strikes =
  TestCase $ assertEqual "test_all_strikes"
                         (Just 300) (game([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

test_all_spares :: Test
test_all_spares =
  TestCase $ assertEqual "test_all_spares"
                         (Just 141) (game([9,1, 8,2, 7,3, 6,4, 5,5, 4,6, 3,7, 2,8, 1,9, 5,5,0]))

test_open_frames :: Test
test_open_frames =
  TestCase $ assertEqual "test_open_frames"
                         (Just 90) (game([9,0, 8,1, 7,2, 6,3, 5,4, 4,5, 3,6, 2,7, 1,8, 5,4]))

test_strikes_followed_by_spares :: Test
test_strikes_followed_by_spares =
  TestCase $ assertEqual "test_strikes_followed_by_spares"
                         (Just 125) (game([10, 5,5, 5,0, 10, 0,10, 5,0, 10, 9,1, 5,0, 5,0]))

test_spares_followed_by_strikes :: Test
test_spares_followed_by_strikes =
  TestCase $ assertEqual "test_spares_followed_by_strikes"
--  also tests "zero ten" spare
                         (Just 125) (game([5,5, 10, 5,0, 0,10, 10, 5,0, 9,1, 10, 5,0, 5,0]))

test_gutters_with_strikes :: Test
test_gutters_with_strikes =
  TestCase $ assertEqual "test_gutters_with_strikes"
                         (Just 30) (game([0,0, 10, 0,0, 0,0, 10, 0,0, 10, 0,0, 0,0, 0,0]))

--- score game - misc end games ---

test_tenth_frame_strike_gutter_strike :: Test
test_tenth_frame_strike_gutter_strike =
  TestCase $ assertEqual "test_tenth_frame_strike_gutter_strike"
                         (Just 20) (game([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 10,0,10]))

test_tenth_frame_strike_spare :: Test
test_tenth_frame_strike_spare =
  TestCase $ assertEqual "test_tenth_frame_strike_spare"
                         (Just 20) (game([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 10,5,5]))

test_tenth_frame_zero_spare :: Test
test_tenth_frame_zero_spare =
  TestCase $ assertEqual "test_tenth_frame_zero_spare"
                         (Just 12) (game([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,10,2]))

test_tenth_frame_spare_strike :: Test
test_tenth_frame_spare_strike =
  TestCase $ assertEqual "test_tenth_frame_spare_strike"
                         (Just 20) (game([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 5,5,10]))

main :: IO Counts
main = runTestTT $ TestList [test_too_many_entries, test_values_bigger_than_eleven, test_negative_values, test_all_gutter_balls, test_all_strikes, test_all_spares, test_open_frames, test_strikes_followed_by_spares, test_spares_followed_by_strikes, test_gutters_with_strikes, test_tenth_frame_strike_gutter_strike, test_tenth_frame_strike_spare, test_tenth_frame_zero_spare, test_tenth_frame_spare_strike]
