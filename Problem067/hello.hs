module Main where

import System.IO  


main :: IO ()
main = do  
        contents <- readFile "triangle.txt"
        let linesList = lines contents
        let tree = map (map readInt . words) linesList
        print $ coalesce tree

readInt :: String -> Int
readInt = read

-- Coalesce the tree from the bottom up
-- For each row, add the maximum of the two children to the parent
-- The result is the maximum path sum
coalesce :: [[Int]] -> Int
coalesce = head . foldr1 combine
        where combine row acc = zipWith (+) row maxPairs 
                where maxPairs = zipWith max acc (tail acc)