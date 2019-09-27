
def is_prime(n):
    # primes are greater than 1
    if (n <= 1):
        return False
    # 2 or 3 are prime #'s
    if (n <= 3):
        return True
    # check if the number is divisible by 2 or 3
    # if so, will continue to next check
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True


if __name__ == "__main__":
    n = int(input("Please enter a integer to find if it is a prime number: "))
    print(is_prime(n))
