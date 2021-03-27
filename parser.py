import argparse


def parse():
    print(
        "  @@@   @@@@  @@@@@@@@\n @@ @@  @@ @@    @@\n@@      @@ @@    @@\n@@      @@@@     @@   Tools for Cryptography\n @@ @@  @@       @@   Mady by: Baka\n  @@@   @@       @@")
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gcd", help="'-g 5,6'")
    parser.add_argument("-f", "--factorize", help="'-f 5'")
    parser.add_argument("-c", "--crt", help="'-c '")

    args = parser.parse_args()
    print(args)
    return args


def get_ints(args):
    list_of_ints = args.split(",")
    for inter in list_of_ints:
        try:
            inter = int(inter)
        except:
            print("Arguments are not integer!")
            return False
    return list_of_ints


parse()
