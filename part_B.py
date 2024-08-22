from functools import reduce
from itertools import accumulate

# 1) Fibonacci generator
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])[:n]

# Test for Fibonacci generator
print("Fibonacci(5):", fibonacci(10))  # Expected output: [0, 1, 1, 2, 3]

# 2) Concatenate strings
concat_strings = lambda lst: reduce(lambda x, y: x + ' ' + y, lst)

# Test for concatenating strings
print("Concat(['Hello', 'world!']):", concat_strings(['Hello', 'world!']))  # Expected output: "Hello world!"

# 3) Cumulative sum of squares
cum_sum_squares = lambda lst: list(accumulate(
    map(lambda sublist: sum(
        map(lambda x: (lambda y: (lambda z: z ** 2)(y))(x), filter(lambda x: (lambda w: w % 2 == 0)(x), sublist))
    ), lst)
))
# Test for cumulative sum of squares
print("Cum_sum_squares([[1, 2, 3], [4, 5, 6]]):", cum_sum_squares([[1, 2, 3], [4, 5, 6]]))  # Expected output: [4, 52]
print(cum_sum_squares([[], [2, 4], []]))  # Expected output: [0, 20, 20]

# 4) Higher-order function
cumulative_apply = lambda op: lambda seq: reduce(lambda x, y: op(x, y), seq)

# Test for higher-order function (factorial)
factorial = cumulative_apply(lambda x, y: x * y)
print("Factorial of 5:", factorial([1, 2, 3, 4, 5]))  # Expected output: 120

# Test for higher-order function (exponentiation)
exponentiation = cumulative_apply(lambda x, y: x ** y)
print("Exponentiation 2^3:", exponentiation([2, 3]))  # Expected output: 8

# 5) One-line filtering & mapping
result = reduce(lambda x, y: x + y, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])))

# Test for one-line filtering and mapping
print("Sum of squares of evens:", result)  # Expected output: 56

# 6) Count palindromes
count_palindromes = lambda lst: list(map(lambda sublist: len(list(filter(lambda s: s == s[::-1], sublist))), lst))

# Test for counting palindromes
print("Count_palindromes([['madam', 'hello'], ['racecar', 'world']]):", count_palindromes([['madam', 'hello'], ['racecar', 'world']]))  # Expected output: [1, 1]

# 7) Lazy evaluation:
# Explanation: Lazy evaluation computes values only when they are needed,
# as seen in the example the values are generated and squared on demand rather than all at once
# in other words, it Generates each value only when it's needed, one at a time, which can be more efficient

# 8) Prime numbers descending order
primes_desc = lambda lst: sorted(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), lst), reverse=True)

# Test for prime numbers in descending order
print("Primes_desc([10, 7, 5, 4, 3, 2]):", primes_desc([10, 7, 5, 4, 3, 2]))  # Expected output: [7, 5, 3, 2]
