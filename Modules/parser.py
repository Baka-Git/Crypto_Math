import argparse


def parse():
    print(
        "  @@@   @@@@  @@@@@@@@\n @@ @@  @@ @@    @@\n@@      @@ @@    @@\n@@      @@@@     @@   Tools for "
        "Cryptography\n @@ @@  @@       @@   Mady by: Baka\n  @@@   @@       @@")
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gcd", help="'-g 5,6'")
    parser.add_argument("-f", "--factorization", help="'-f 5'")
    parser.add_argument("-c", "--crt", help="'-c 5mod18,4mod7'")
    parser.add_argument("-i", "--inverse", help="Format: -i NUM,MOD. Example: '-i 5,9'")
    parser.add_argument("-p", "--phi", help="'-p 11'")
    parser.add_argument("--group", help="'--group 11'")
    parser.add_argument("--orders_of_group", help="--orders_of_group 13")
    parser.add_argument("--curve", help="In case first number is negative use '/' instead of '-' (Just ounce!)! "
                                        "Example for EC: y^2 "
                                        "- 1 * y + 2 * xy = x^3 - 5 * x^2 + 3 * x + 2: '--curve "
                                        "1,-1,2,1,-5,3,2'")
    parser.add_argument("--point_on_curve", help="In case first number is negative use '/' instead of '-' "
                                                 "(Just ounce!)! Format: --point_on_curve X,Y,F"
                                                 "EC must be given! Example: '--curve 1,-1,2,1,-5,3,2 --point_on_curve "
                                                 "2,3,5'")
    args = parser.parse_args()
    print(args)
    args = control(args)
    return args


def control(args):
    gcd = args.gcd
    if gcd is not None:
        gcd = get_ints(args.gcd)
        if gcd is False:
            return False
    factor = args.factorization
    if factor is not None:
        factor = get_ints(factor)
        if factor is False:
            return False
    crt = args.crt
    if crt is not None:
        crt = get_crt_info(crt)
        if crt is False:
            return False
    inverse = args.inverse
    if inverse is not None:
        inverse = get_ints(inverse)
        if inverse is False:
            return False
    phi = args.phi
    if phi is not None:
        phi = get_int(phi)
        if phi is False:
            return False
    group = args.group
    if group is not None:
        group = get_int(group)
        if group is False:
            return False
    orders_of_group= args.orders_of_group
    if orders_of_group is not None:
        orders_of_group = get_int(orders_of_group)
        if orders_of_group is False:
            return False
    curve=args.curve
    if curve is not None:
        curve = get_ints(curve)
        if curve is False:
            return False
    point_on_curve=args.point_on_curve
    if point_on_curve is not None:
        point_on_curve = get_ints(point_on_curve)
        if point_on_curve is False or curve is None:
            return False

    return [gcd, factor, crt, inverse, phi, group, orders_of_group, curve, point_on_curve]


def get_ints(args):
    list_of_ints = args.split(",")
    if list_of_ints[0][0]=="/":
        list_of_ints[0]="-"+list_of_ints[0][1:]
    for inter in range(0, len(list_of_ints)):
        list_of_ints[inter] = get_int(list_of_ints[inter])
        if list_of_ints[inter] is False:
            return False
    return list_of_ints


def get_int(inter):
    try:
        inter = int(inter)
    except:
        print("Arguments are not integer!")
        return False
    return inter


def get_crt_info(args):
    list_of_lines = args.split(",")
    list_of_x_and_mods = []
    for line in list_of_lines:
        help_list = line.split("mod")
        for i in range(0, len(help_list)):
            help_list[i] = get_int(help_list[i])
            if help_list[i] is False:
                return False
        list_of_x_and_mods.append(help_list)
    return list_of_x_and_mods
