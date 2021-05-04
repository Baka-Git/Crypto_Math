def lcg(prime, a, c, seed, counter):
    print("LCG\nNumber of random numbers is " + str(counter) + ", prime p is " + str(prime) + ", a = " + str(
        a) + ", c = " + str(c) + " and seed X_0 = s = " + str(seed))
    values = []
    x = seed
    values.append(x)
    print("X_0 = " + str(x))
    for i in range(1, counter):
        x = (a * x + c) % prime
        print("X_" + str(i) + " = " + str(x))
        values.append(x)
    return values


def xor(x, y):
    if x == y:
        return 0
    return 1


def list_to_binar(values):
    new_list = []
    for value in values:
        new_list.append(value % 2)
    # print(new_list)
    return new_list


def one_bit_commit(random_values, r, b, seed):
    print("One-bit Commitment\nBob sends r = " + str(r) + "\nAlice choose b = " + str(b))
    # c computation
    c = []
    random_values = list_to_binar(random_values)
    if b == 1:
        for i in range(0, len(r)):
            c.append(xor(random_values[i], r[i]))
    else:
        c = random_values
    print("Alice sends c = " + str(c) + "\nAlice sends opening (b,s) = (" + str(b) + ", " + str(seed) + ")")


# a = lcg(11, 3, 4, 2, 3)
# one_bit_commit(a, [1, 0, 0], 1, 2)
