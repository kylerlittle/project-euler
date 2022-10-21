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
    for power in range(2,6):
        print(f"Finding numbers equal to their digits to {power} power")
        findNumbersEqualToItsDigitsToXthPowerSummed(power, power + 2)
