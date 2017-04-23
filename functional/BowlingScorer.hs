module BowlingScorer where

pair :: [Int] -> [(Int,Int)]
pair [a,b]      = (a, b) : (0,0) : (0,0) : []
pair [a,b,c]
    | a == 10   = (10,0) : (b,c) : (0,0) : []
    | otherwise = (a, b) : (c,0) : (0,0) : []
pair (10:b:xs)  = (10,0) : pair (b:xs)
pair (a:b:xs)   = (a, b) : pair xs

score :: ((Int,Int),(Int,Int),(Int,Int)) -> Int
score ((10,0),(10,0),(e,f)) = 20 + e
score ((a,b),(c,d),(e,f))
    | a == 10   = a + c + d
    | a+b == 10 = a + b + c
    | otherwise = a + b

zip_self xs = zip3 xs (drop 1 xs) (drop 2 xs)

game xs  = sum [ score x | x <- zip_self (pair xs) ]
