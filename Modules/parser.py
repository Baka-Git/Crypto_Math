import argparse


def parse():
    print()
    parser = argparse.ArgumentParser("\n"
                                     "  @@@   @@@@  @@    @@  @@@@   @@@@@@@@  @@@@\n"
                                     " @@ @@  @@ @@  @@  @@   @@  @@    @@    @@  @@\n"
                                     "@@      @@ @@   @@@@    @@  @@    @@   @@    @@\n"
                                     "@@      @@@@     @@     @@@@      @@   @@    @@\n"
                                     " @@ @@  @@ @@    @@     @@        @@    @@  @@   Tools for Cryptography\n"
                                     "  @@@   @@  @@   @@     @@        @@     @@@@    Mady by: Baka")

    parser.add_argument(
        "-g",
        "--gcd",
        help="Function for finding GCD of two numbers. Example: '-g 5,6'"
    )

    parser.add_argument(
        "-f",
        "--factorization",
        help="Function for factorization of one number. Example:'-f 5'"
    )

    parser.add_argument(
        "-c",
        "--crt",
        help="Function for finding solution for chinese remainder theorem. Format -c 1LINE,2LINE,3LINE,... Example: '-c 5mod18,4mod7'"
    )

    parser.add_argument(
        "-i",
        "--inverse",
        help="Function for finding inverse number for given number. Format: -i NUM,MOD. Example: '-i 5,9'"
    )

    parser.add_argument(
        "-p",
        "--phi",
        help="Function for finding Euler Value of given number. Example: '-p 11'"
    )

    parser.add_argument(
        "--group",
        help="Function for finding Multiplicative Group of given number. Example: '--group 11'"
    )

    parser.add_argument(
        "--orders_of_group",
        help="Function for finding orders of all elements of multiplicative group made of given number. Example: '--orders_of_group 13'"
    )

    parser.add_argument(
        "--curve",
        help="Function for giving program your curve, if no athor function is enabled, program check if given curve is Elliptic. In case first number is negative use '/' instead of '-' (Just ounce!)! "
             "Example for EC: y^2 "
             "- 1 * y + 2 * xy = x^3 - 5 * x^2 + 3 * x + 2: '--curve "
             "1,-1,2,1,-5,3,2'"
    )

    parser.add_argument(
        "--p_point",
        help="Give program information about P, P = [x,y] -> format '--p_point x,y'"
    )

    parser.add_argument(
        "--q_point",
        help="Give program information about Q, Q = [x,y] -> format '--q_point x,y'"
    )

    parser.add_argument(
        "--field",
        help="Give program information about F, format '--field FIELD'"
    )

    parser.add_argument(
        "--order_of_ec",
        help="Function for finding order of given curve. In case first number is negative use '/' instead of '-' "
             "(Just ounce!)! Format: --order_of_ec"
             "EC + Field must be given! Example: '--curve 1,0,0,1,0,-1,-1  --field 7 --order_of_ec'",
        action="store_true"
    )

    parser.add_argument(
        "--point_on_curve",
        help="Function for finding out if given point is on given curve. In case first number is negative use '/' instead of '-' "
             "(Just ounce!)! Format: --point_on_curve"
             "EC + P_Point + Field must be given! Example: '--curve 1,0,0,1,0,2,1 --p_point 0,1 --field 7 --point_on_curve'",
        action="store_true"
    )

    parser.add_argument(
        "--add_points_ec",
        help="Function for adding two given points. In case first number is negative use '/' instead of '-' "
             "(Just ounce!)! Format: --add_points_ec"
             "EC + Points + Field must be given! Example: '--curve 1,0,0,1,0,2,1 --p_point 1,2 --q_point 0,1 --add_points_ec --field 7'",
        action="store_true"
    )

    parser.add_argument(
        "--order_of_the_one_point",
        help="Function for getting order of given point on given EC. Format: --order_of_the_one_point. EC + Point + Field must be given! "
             "Example: '--curve 1,0,0,1,0,-1,1 --p_point 4,1 --field 5 --order_of_the_one_point'",
        action="store_true"
    )

    parser.add_argument(
        "--order_of_all_points",
        help="Function for getting all orders of point on given EC. Format: --order_of_the_one_point. EC + Field must be given! Example: ' --curve 1,0,0,1,0,-1,1 --field 5 --order_of_all_point'",
        action="store_true"
    )

    parser.add_argument(
        "--possible_orders",
        help="Function for finding out possible order of points, if only order of EC (Elliptic curve) is known and also function for finding out possible orders of points, if order of EC is change to given value Formats: --possible_orders OLD_ORDER,NEW_ORDER In case we DO NOT change order of EC format is: --possible_orders ORDER. Example: '--possible_orders 5,15'"
    )

    parser.add_argument(
        "--mov_attack",
        help="Function for finding out secret by MOV Attack. Format --mov_attack SECRET,GENERATOR,ORDER. Example: '--mov_attack 5,2,10'"
    )

    parser.add_argument(
        "--get_z_x_table",
        help="Function for generating help table of Zx. Format --get_z_x_table GENERATOR,MODULUS. Example: '--get_z_x_table 2,5'"
    )

    parser.add_argument(
        "--help_bilinear",
        help="Function for printing help table for bilinear operations! Example: '--help_bilinear'",
        action="store_true"
    )

    parser.add_argument(
        "--tests",
        help="Begin practice mode. Enter a semi-interactive terminal and practice some basic elliptic curve calculations. This option is to be used on its own.",
        action="store_true",
    )

    parser.add_argument(
        "--lcg",
        help="Function for Linear Congruential Generator (LCG). Format: --lcg PRIME,A,C,SEED,COUNTER. Example: '--lcg 11,3,4,2,3'"
    )
    parser.add_argument("--r_value",
                        help="Help value for One-bit Commitment function- Format --r_value R_1,R_2,R_3,... Example: '1,0,1'")
    parser.add_argument(
        "--one_bit_com",
        help="Function for One-bit Commitment, LCG operation and assign R Value are required. Format is --lcg PRIME,"
             "A,C,SEED,COUNTER --r_value R_1,R_2,... --one_bit_com B. Example: '--lcg 11,3,4,2,3 --r_value 1,0,"
             "1 --one_bit_com 1' "
    )

    args = parser.parse_args()
    # print(args)
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

    orders_of_group = args.orders_of_group
    if orders_of_group is not None:
        orders_of_group = get_int(orders_of_group)
        if orders_of_group is False:
            return False

    curve = args.curve
    if curve is not None:
        curve = get_ints(curve)
        if curve is False or len(curve) != 7:
            return False

    p_point = args.p_point
    if p_point is not None:
        p_point = get_ints(p_point)
        if p_point is False or curve is None:
            return False

    q_point = args.q_point
    if q_point is not None:
        q_point = get_ints(q_point)
        if q_point is False or curve is None:
            return False

    field = args.field
    if field is not None:
        field = get_ints(field)
        if field is False or curve is None:
            return False

    point_on_curve = args.point_on_curve
    if point_on_curve and p_point is None:
        return False

    order_of_ec = args.order_of_ec
    if order_of_ec and field is None:
        return False

    add_points_ec = args.add_points_ec
    if add_points_ec and (p_point is None or q_point is None):
        return False

    order_of_the_one_point = args.order_of_the_one_point
    if order_of_the_one_point and (p_point is None or field is None):
        return False

    order_of_all_points = args.order_of_all_points
    if order_of_all_points and (curve is None or field is None):
        return False

    mov_attack = args.mov_attack
    if mov_attack is not None:
        mov_attack = get_ints(mov_attack)
        if mov_attack is False or len(mov_attack) != 3:
            return False

    lcg = args.lcg
    if lcg is not None:
        lcg = get_ints(lcg)
        if lcg is False or len(lcg) != 5:
            return False

    r_value = args.r_value
    if r_value is not None:
        r_value = get_ints(r_value)
        if r_value is False:
            return False

    one_bit_com = args.one_bit_com
    if one_bit_com is not None:
        one_bit_com = get_int(one_bit_com)
        if one_bit_com is False or lcg is None or r_value is None or len(r_value) != lcg[4]:
            return False

    get_z_x_table = args.get_z_x_table

    if get_z_x_table is not None:
        get_z_x_table = get_ints(get_z_x_table)
        if get_z_x_table is False or len(get_z_x_table) != 2:
            return False

    help_bilinear = args.help_bilinear
    possible_orders = args.possible_orders
    test = args.tests

    if possible_orders is not None:
        possible_orders = get_ints(possible_orders)
        if possible_orders is False:
            print("Wrong arguments!")
            return False

    return [gcd, factor, crt, inverse, phi, group, orders_of_group, curve, p_point, q_point, field, point_on_curve,
            order_of_ec, add_points_ec, order_of_the_one_point, order_of_all_points, mov_attack, get_z_x_table,
            help_bilinear, possible_orders, test, lcg, r_value, one_bit_com]


def get_ints(args):
    list_of_ints = args.split(",")
    if list_of_ints[0][0] == "/":
        list_of_ints[0] = "-" + list_of_ints[0][1:]
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
