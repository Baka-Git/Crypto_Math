import argparse

def parse():
    print("  @@@   @@@@  @@@@@@@@\n @@ @@  @@ @@    @@\n@@      @@ @@    @@\n@@      @@@@     @@   Tools for Cryptography\n @@ @@  @@       @@   Mady by: Baka\n  @@@   @@       @@")
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--detection",
                        help="Enables Detection Module. Detection to enable: syn - Syn Flood detection, udp - UDP "
                             "Flood detection, icmp - ICMP Flood detection, complex - Complex detection. Example '-d "
                             "syn', '-d syn,udp' In case of enabling all detetion modes use: '-d all'")

    args = parser.parse_args()
    print(args)
    return args
parse()