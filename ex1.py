import argparse

parser = argparse.ArgumentParser()
parser.add_argument("add", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--awa", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.add**2
if args.awa:
    print(f"the square of {args.add} equals {answer}")
else:
    print(answer)
