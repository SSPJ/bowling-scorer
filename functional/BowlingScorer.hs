module BowlingScorer where
--ts :: [Int]
--ts = [10,6,1,7,3,10,4,3,5,5,5,5,9,0,9,1,7,3,10]

pair :: [Int] -> [(Int,Int)]
pair [a,b]      = (a,b) : (0,0) : []
pair [a,b,c]
    | a == 10   = (10,0) : (b,c) : []
    | otherwise = (a,b) : (c,0) : []
pair (10:b:xs)  = (10,0) : pair (b:xs)
pair (a:b:xs)   = (a,b) : pair xs

score :: ((Int,Int),(Int,Int)) -> Int
score ((a,b),(c,d))
    | a == 10   = a + c + d
    | a+b == 10 = a + b + c
    | otherwise = a + b

zip_self xs = zip xs (drop 1 xs)

game xs  = sum [ score x | x <- zip_self (pair xs) ]
