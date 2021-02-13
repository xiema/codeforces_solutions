module Main (main) where

norm :: String -> String
norm s
  | length s `mod` 2 == 1 = s
  | otherwise = let
                  l = length s `quot` 2
                  s1 = norm $ take l s
                  s2 = norm $ drop l s
                in if s1 < s2 then s1++s2 else s2++s1

main = do
        a <- getLine
        b <- getLine
        putStrLn $ if norm a == norm b then "YES" else "NO"
