#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) the loop runs n^3 times, but that just means that the constant is large and we drop constants, so it should be O(n)


b) The outer for loop will run N times so that loops is O(n), The inner while loop will run on average half as many times as n because j is incremented by two so that would be 1/2(n). So that should simplify down to O(n^2)


c)The function only calls itself once, so the runtime is O(n)

## Exercise II
So we can say that the floors are sorted. Since the floors are sorted we could use binary search. We look at the middle and see if the result of a dropped egg is broken or not. If it is not broken, we look higher, if it is broken we look lower. We continue to use this recursive search, halfing the search space each time until we find the first floor that the egg breaks. The time complexity should be log(n) because the search space is halfed at each iteration.

