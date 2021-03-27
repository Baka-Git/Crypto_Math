def factorize(number):
    list_of_primes = []
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for pri in prime:
        fact_helper(number, pri, list_of_primes)
    return list_of_primes


def fact_helper(number, prime, list_of_primes):
    if number % prime == 0:
        number = number / prime
        list_of_primes.append(prime)
        fact_helper(number, prime, list_of_primes)


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
