def factorization(number):
    list_of_primes = []
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for pri in prime:
        fact_helper(number, pri, list_of_primes)
    print("Number " + str(number) + " can be factorize to: " + str(list_of_primes))
    return list_of_primes


def fact_helper(number, prime, list_of_primes):
    if number % prime == 0:
        number = number / prime
        list_of_primes.append(prime)
        fact_helper(number, prime, list_of_primes)


def gcd(x, y, regime):
    if y == 0:
        if regime:
            print("GCD is " + str(x))
        return x
    else:
        return gcd(y, x % y, regime)


def find_inverse(num, mod, regime):
    for i in range(1, int(mod)):
        if (i * num) % mod == 1:
            if regime:
                print("Inverse of number " + str(num) + " is " + str(i))
            return i
    if (regime):
        print("Value " + str(num) + " does NOT have inverse number in Group_" + str(mod) + "!")
        return False


def crt(list_of_x_and_mods):
    # print(list_of_x_and_mods)
    m = 1
    for mod in list_of_x_and_mods:
        m *= mod[1]
    n = []
    l = []
    for mod in list_of_x_and_mods:
        n_var = m / mod[1]
        n.append(n_var)
        l.append(find_inverse(n_var, mod[1], False))
    print("M: " + str(m))
    print("N: " + str(n))
    print("L: " + str(l))
    x = 0
    for var in range(0, len(list_of_x_and_mods)):
        x += list_of_x_and_mods[var][0] * n[var] * l[var]
    x = x % m
    print("x = " + str(x))
    return x


def phi(number, regime):
    num = 0
    for i in range(1, number):
        if gcd(number, i, False) == 1:
            num += 1
    if regime:
        print("Euler function of number " + str(number) + " is " + str(num))
    return num


def find_group_mult(number, regime):
    list_of_group = []
    for i in range(1, number):
        if gcd(number, i, False) == 1:
            list_of_group.append(i)
    if regime:
        print("Group is: " + str(list_of_group))
    return list_of_group


def order_of_num(num, mod):
    order = 1
    help_num = num
    gate = True
    if num == 1:
        return order
    while gate:
        help_num = (help_num * num) % mod
        order += 1
        if help_num == 1:
            gate = False
    return order


def find_group_orders(number, regime):
    group = find_group_mult(number, True)
    list_of_orders = []
    for i in range(0, number):
        list_of_orders.append([i])
    for inter in group:
        order = order_of_num(inter, number)
        list_of_orders[order].append(inter)
    for i in range(0, number):
        if len(list_of_orders[number - 1 - i]) == 1:
            list_of_orders.pop(number - 1 - i)
    for line in list_of_orders:
        gen = ""
        if line[0] == len(group):
            gen = " -> GENERATORS!"
        if regime:
            print(str(line[1:]) + " have order " + str(line[0]) + gen)
    return list_of_orders


def find_sub_group(generator, mod):
    help_group = find_group_mult(mod, False)
    try:
        help_group.index(generator)
    except:
        print("Wrong arguments were given.")
        return False
    sub_group = []
    for i in range(1, mod + 1):
        result = generator ** i % mod
        sub_group.append(generator ** i % mod)
        if result == 1:
            print("Subgroup of generator g = " + str(generator) + " is: " + str(sub_group))
            return sub_group
    print(sub_group)
# find_group_orders(5, True)
# find_group_mult(5,True)
#find_sub_group(5,11)
