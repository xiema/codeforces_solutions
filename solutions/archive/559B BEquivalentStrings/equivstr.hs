module Main (main) where


solve :: String -> String -> Bool
solve a b
  | a == b = True
  | length a `mod` 2 == 1 = False
  | otherwise = let
                  l = length a `quot` 2
                  (a1, a2) = splitAt l a
                  (b1, b2) = splitAt l b
                in if (solve a1 b1) && (solve a2 b2) || (solve a1 b2) && (solve a2 b1)
                  then True
                  else False

main = do
        a <- getLine
        b <- getLine
        putStrLn $ if solve a b then "YES" else "NO"
