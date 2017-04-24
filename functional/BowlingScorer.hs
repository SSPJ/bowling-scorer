module BowlingScorer where
-- Seamus Johnston, 2017

-- pair seperates the list of rolls into tuples
-- by frame; frame 10 with 3 rolls gets two tuples
pair :: [Int] -> [(Int,Int)]
-- base cases: frame ten
pair [a,b]      = (a, b) : (0,0) : []
pair [a,b,c]
    | a == 10   = (10,0) : (b,c) : []
    | otherwise = (a, b) : (c,0) : []
-- edge case: a strike
pair (10:b:xs)  = (10,0)         : pair (b:xs)
-- general case:
pair (a:b:xs)   = (a, b)         : pair xs


-- score traverses the list of frame tuples and
-- returns a list of scores by frame
score :: [(Int,Int)] -> [Int]
-- base case: frame ten / end of list
score [(a,b)]   = (a + b)     : []
-- edge cases: end of game
score [(a,b),(c,d)]
--  strike or spare in frame ten
    | a   == 10 = (a + c + d) : []
    | a+b == 10 = (a + b + c) : []
--  frame 9 mistaken for ten
    | otherwise = (a + b)     : score [(c,d)]
-- general case:
score ((a,b):(c,d):xs)
--  edge case: two strikes in a row, eg [(10,0),(10,0),(3,4)]
    | a+c == 20 = (a + c + u) : score ((c,d):xs)
--  a strike
    | a   == 10 = (a + c + d) : score ((c,d):xs)
--  a spare
    | a+b == 10 = (a + b + c) : score ((c,d):xs)
    | otherwise = (a + b)     : score ((c,d):xs)
    where     u = fst $ head xs

-- validate takes a list of Ints and returns Nothing
-- if it is longer than 21 or contains Ints > 10 or < 0
validate :: [Int] -> Maybe [Int]
validate xs
    | length xs > 21 = Nothing
    | any (\n -> n > 10 || n <0) xs = Nothing
    | otherwise = Just xs

-- game takes an Int list of pins knocked down
-- returns Just an Int bowling score if the list is valid
game :: [Int] -> Maybe Int
game xs = if null $ validate xs
          then Nothing
          else Just . sum . score $ pair xs
