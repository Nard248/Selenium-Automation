# Sum of List of Numbers
def list_sum(num_List):
    if len(num_List) == 1:
        return num_List[0]
    else:
        return num_List[0] + list_sum(num_List[1:])


print(list_sum([2, 4, 5, 6, 7]))


# Write a Python program to convert an integer to a string in any base.
def to_string(n, base):
    conver_tString = "0123456789ABCDEF"
    if n < base:
        return conver_tString[n]
    else:
        return to_string(n // base, base) + conver_tString[n % base]


print(to_string(2835, 16))


# Write a Python program to sum recursion lists.
def recursive_list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total = total + recursive_list_sum(element)
        else:
            total = total + element

    return total


print(recursive_list_sum([1, 2, [3, 4], [5, 6]]))


# Write a Python program to get the factorial of a non-negative integer.
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * (factorial(n - 1))


print(factorial(5))


# Write a Python program to solve the Fibonacci sequence using recursion.
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))


# Write a Python program to get the sum of a non-negative integer.
def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(int(n / 10))


print(sumDigits(345))
print(sumDigits(45))


# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
def sum_series(n):
    if n < 1:
        return 0
    else:
        return n + sum_series(n - 2)


print(sum_series(6))
print(sum_series(10))
