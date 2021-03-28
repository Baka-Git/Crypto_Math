import math


def is_elliptic(curve):
    # curve - [y^2 y yx x^3 x^2 x^1 a]
    help_curve = curve
    if curve[0] != 1 or curve[3] != 1:
        print("Given curve is not elliptic!")
        return False
    operation = [" + ", " + ", " + ", " + ", " + ", " + ", " + "]
    for point in range(0, len(curve)):
        if curve[point] < 0:
            curve[point] = abs(curve[point])
            operation[point] = " - "
    print("Elliptic curve: y^2" + operation[1] + str(curve[1]) + " * y" + operation[2] + str(curve[2]) + " * xy = x^3"
          + operation[4] + str(curve[4]) + " * x^2" + operation[5] + str(curve[5]) + " * x" + operation[6] + str(
        curve[6]))
    return help_curve


def is_point_on_elliptic_curve(x, y, f, curve):
    if is_elliptic(curve) is False:
        return False
    elif (y ** 2 + curve[1] * y + curve[2] * x * y) % f == (x ** 3 + curve[4] * x ** 2 + curve[5] * x + curve[6]) % f:
        print("Point (" + str(x) + "," + str(y) + ") is on elliptic curve!")
        return True
    print("Point (" + str(x) + "," + str(y) + ") is not on elliptic curve!")
    return False
    # curve - [y^2 y yx x^3 x^2 x^1 a]


def order_of_ec(f, curve):
    if curve[2] != 0:
        return False
    line_points = []
    y_2_points = []
    for y in range(0, int(f / 2) + 1):
        y_2_points.append((y ** 2) % f)
    x_points = []
    x_side_points = []
    for x in range(0, f):
        x_points.append(x)
        x_side_points.append((x ** 3 + x ** 2 * curve[4] + x * curve[5] + curve[6]) % f)
    for x in range(0, f):
        x_side = x_side_points[x]
        points = find_point(x, x_side, y_2_points, f)
        if points is False:
            y_2 = "-"
            y = "-"
            points = "-"
        else:
            y_2 = points[0][1] ** 2
            y = "+-" + str(points[0][1])
        line_points.append([x, x_side, y_2, y, points])
    line_points.append(["∞", "-", "-", "∞", "[∞,∞]"])
    order = 0
    for line in line_points:
        print(line)
        if line[4] == "[∞,∞]":
            order += 1
        elif line[4] != "-":
            if line[2] == 0:
                order += 1
            else:
                order += 2
    print("Order of E[F" + str(f) + "] is: " + str(order))
    return order


def find_point(x, x_side, y_2_points, f):
    for y in range(0, len(y_2_points)):
        if x_side == y_2_points[y]:
            if y_2_points[y] == 0:
                return [[x, int(math.sqrt(y_2_points[y]))]]
            return [[x, int(math.sqrt(y_2_points[y]))], [x, int(-math.sqrt(y_2_points[y]) % f)]]
    return False


def add_point(point_p, point_q, f, curve):
    r = None
    if point_p[0] != point_q[0]:
        lambdas = (point_q[1] - point_p[1]) / (point_q[0] - point_p[0])%f
        x_r = (lambdas ** 2 - point_q[0] - point_p[0])
        r = [x_r, (lambdas * (point_p[0] - x_r) - point_p[1])]
    elif point_p[0] == point_q[0] and point_p[1] == point_q[1] and point_p[1] != 0:
        lambdas = ((3 * point_p[0] ** 2 + curve[5]) / (2 * point_p[1]))%f
        x_r = (lambdas ** 2 - 2 * point_p[0])
        r = [x_r, (lambdas * (point_p[0] - x_r) - point_p[1])]
    else:
        r = "[∞,∞]"
    print(r)
    return r


# is_elliptic([1, -1, 2, 1, -5, 3, 2])
#order_of_ec(7, [1, 0, 0, 1, 0, -1, -1])
add_point([0,1],[0,-1],7,[1,0,0,1,0,1,1])