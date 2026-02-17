from utils import factorial, gcd

print("Factorial of 5:", factorial(5))
print("GCD of 18 and 24:", gcd(18, 24))


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_power_of_five(n):
    if n < 1:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1

