from Modules.parser import parse
from Modules.group_tools import *
from Modules.elipctic_curve_tools import *


def run():
    args = parse()
    if args is False:
        print("Wrong arguments were given!")
        return False
    if args[0] is not None:
        gcd(args[0][0], args[0][1])
    if args[1] is not None:
        factorization(args[1][0])
    if args[2] is not None:
        crt(args[2])
    if args[3] is not None:
        find_inverse(args[3][0], args[3][1], True)
    if args[4] is not None:
        phi(args[4], True)
    if args[5] is not None:
        find_group_mult(args[5], True)
    if args[6] is not None:
        find_group_orders(args[6],True)
    if args[7] is not None and args[8] is None:
        is_elliptic(args[7])
    if args[7] is not None and args[8] is not None:
        is_point_on_elliptic_curve(args[8][0], args[8][1], args[8][2], args[7])


run()
