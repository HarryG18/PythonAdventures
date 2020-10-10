# A left-truncatable prime is a prime number that contains no 0 digits and, when the first digit is successively removed, the result is always prime.
#
# A right-truncatable prime is a prime number that contains no 0 digits and, when the last digit is successively removed, the result is always prime.
#
# Create a function that takes an integer as an argument and:
#
# If the integer is only a left-truncatable prime, return "left".
# If the integer is only a right-truncatable prime, return "right".
# If the integer is both, return "both".
# Otherwise, return False.



import sympy

def truncatable(n):
    nums = []
    lnums = []
    rnums = []
    for ch in str(n):
        nums.append(str(ch))
    if "0" not in nums:
        for i in range(len(nums)):
            lnums.append(int(''.join(nums[i:])))
            rnums.append(int(''.join(nums[:(len(nums)-i)])))
        if all(sympy.isprime(elem) == True for elem in lnums):
            if all(sympy.isprime(elem) == True for elem in rnums):
                return "both"
            else : return "left"
        elif all(sympy.isprime(elem) == True for elem in rnums):
            return "right"
    return False


def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while n >= i**2:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def truncatable2(n):
    nums = []
    lnums = []
    rnums = []
    for ch in str(n):
        nums.append(str(ch))

    if "0" not in nums:
        for i in range(len(nums)):
            lnums.append(int(''.join(nums[i:])))
            rnums.append(int(''.join(nums[:(len(nums)-i)])))

        if all(isPrime(elem) == True for elem in lnums):
            if all(isPrime(elem) == True for elem in rnums):
                return "both"
            else : return "left"

        elif all(isPrime(elem) == True for elem in rnums):
            return "right"

    return False



def prime(num):
    return num > 1 and not any(num%i == 0 for i in range(2,num))

def truncatable3(n):
    n = str(n)
    if "0" in n:
        return False
    left = all(prime(int(n[i:])) for i in range (len(n)))
    right = all(prime(int(n[:i+1])) for i in range (len(n)))

    return {(True, False): 'left', (False, True): 'right', (True, True): 'both'}.get((left, right), False)

