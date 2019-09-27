
def is_composites(n):
    # 1 is not a composite
    if (n <= 1):
        return False
    # 2 and 3 are not a composite
    if (n <= 3):
        return False
    # check if the number is divisible by 2 or 3
    # if not, will continue to next check
    if (n % 2 == 0 or n % 3 == 0):
        return True
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return True
        i = i + 6
    return False


def get_total_composites(num):

    composite_counter = 0
    # This counts the number of composites that are found
    for i in range(int(num+1)):
        if is_composites(i):
            composite_counter += 1
    return str(composite_counter)


if __name__ == "__main__":
    num = int(input("Please enter an integer to find the total number of composites: "))
    print("the total number of composites are: {}".format(get_total_composites(num)))
