from Modules.parser import parse
from Modules.group_tools import *
from Modules.elliptic_curve_tools import *
from Modules.train import interactive
from Modules.commitments_tools import *
from Modules.graph_tools import *

def run():
    args = parse()

    if args is False:
        print("Wrong arguments were given!")
        return False
    if args[0] is not None:
        gcd(args[0][0], args[0][1],True)
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
        find_group_orders(args[6], True)
    # [0-gcd, 1-factor, 2-crt, 3-inverse, 4-phi, 5-group, 6-orders_of_group, 7-curve, 8-p_point, 9-q_point, 10-field,
    # 11-point_on_curve, 12-order_of_ec, 13-add_points_ec, 14-order_of_the_one_point, 15-order_of_all_points,
    # 16-mov_attack, 17-get_z_x_table, 18-help_bilinear, 19-possible_orders ]
    # only control if curve is elliptic, ban 11-point_on_curve, 12-order_of_ec, 13-add_points_ec
    if args[7] is not None and (args[11] is False and args[12] is False and args[13] is False):
        is_elliptic(args[7], True, False)
    # only control if point is on EC curve, need Curve, Point, Field,
    if args[11]:
        is_point_on_elliptic_curve(args[8][0], args[8][1], args[10][0], args[7], True, False)
    # get order of EC
    if args[12]:
        order_of_ec(args[10][0], args[7], True, False)
    # adds points
    if args[13]:
        add_point([args[8][0], args[8][1]], [args[9][0], args[9][1]], args[10][0], args[7], True)
    if args[14]:
        order_of_point(args[8], args[10][0], args[7], True)
    if args[15]:
        order_of_points(args[10][0], args[7], False)
    if args[16] is not None:
        mov_attack(args[16][0], args[16][1], args[16][2])
    if args[17] is not None:
        get_z_x_table(args[17][0], args[17][1])
    if args[18]:
        get_bilininear_help()
    if args[19] is not None:
        possible_orders(args[19], False)
    if args[20]:
        interactive()
    if args[21] is not None:
        lcg(args[21][0],args[21][1],args[21][2],args[21][3],args[21][4])
    if args[23] is not None:
        one_bit_commit(lcg(args[21][0],args[21][1],args[21][2],args[21][3],args[21][4]),args[22],args[23],args[21][3])
    if args[26]:
        is_two_graphs_isomorphic(args[24],args[25])


run()
