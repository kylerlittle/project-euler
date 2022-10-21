# Solution Explanation
Solution to https://projecteuler.net/problem=30. Go to the link for a description of it.

The crux of this problem is noticing the fact that if you have a sum of digits, take for example
the number 1634 in the example, the digits that generated that sum have many permutations.
(1^4) + (6^4) + (3^4) + (4^4) =  (6^4) + (3^4) + (4^4) + (1^4)
but (6^4) + (3^4) + (4^4) + (1^4) is not equal to 6341.

So, the problem can easily be solved by looking at all the possible sums you could
generate and checking if the digits that produced that sum equal the sum itself. It's
simple to calculate every sum because the problem is recursive. The next set of sums
are equal to the sum you're currently at plus each digit to the Xth power.

The reason it's desirable to solve the problem this way is that it's computationally
very efficient. We solve the problem pretty much exclusively with sums rather than
multiplication/exponentials.

This solution has a time complexity of O(n^2) and a memory complexity of
O(n) including the stack memory of the recursion where n is the max number of
digits in possible "special values."

In practice, this runs in less than a second and its peak memory usage is ~68 KB
measured using memray.

This solution went through a lot of iterations. It started with a brute force algorithm
that took a minute to get to the right answer and 70 MB of memory.