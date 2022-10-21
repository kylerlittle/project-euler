from typing import List

def getDigits(n: int) -> List[int]:
    if n < 0:
        raise RuntimeError("getDigits is not implemented for negative numbers")
    
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits

def findNumbersEqualToItsDigitsToXthPowerSummed(x: int, n: int):
    """
    Call a sum Y the sum generated from the digits of a number M
    If M is composed of digits m_1-m_2-m_3-...-m_n (n being the number of digits),
    then sum Y is equal to (m_1)^x  +  (m_2)^x  +  ...  +  (m_n)^x.
    Denote the digits of sum Y as x_1 x_2 ... x_k.
    This function finds all possible numbers such that
    x_1 x_2 ... x_k = m_1 m_2 ... m_n = (m_1)^x  +  (m_2)^x  +  ...  +  (m_n)^x.
    """
    powers = {i: i**x for i in range(0,10)}
    correct_vals = set()
    def recurse(iteration, currSum, digitsToProduceCurrSum):
        if iteration == num_digits:
            currSumDigits = getDigits(currSum)
            if currSumDigits == digitsToProduceCurrSum:
                if currSum not in correct_vals:
                    correct_vals.add(currSum)
                    sumString = " + ".join([f"{str(digit)}^{x}" for digit in currSumDigits])
                    print(f"{currSum} == {sumString}")
            return
        for digit, digit_to_power in powers.items():
            nextSum = currSum + digit_to_power
            recurse(iteration + 1, nextSum, [digit, *digitsToProduceCurrSum])
    for num_digits in range(1,n):
        recurse(0, 0, [])
    print(f"Sum: {sum(correct_vals)}")

if __name__ == '__main__':
    """
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
    """
    findNumbersEqualToItsDigitsToXthPowerSummed(5, 7)
