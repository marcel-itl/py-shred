import argparse
from glob import glob
parser = argparse.ArgumentParser(description='Wipe data from files.')
req = parser.add_argument_group('required')
req.add_argument('destination', type=str, help="path to wipe")
parser.add_argument('-z', metavar='', type=bool, action=argparse.BooleanOptionalAction, help="replace data with null-bytes")
parser.add_argument('-r', metavar='', type=bool, action=argparse.BooleanOptionalAction, help="replace data with randomly generated output")
parser.add_argument('-i', metavar="[int]", type=int, help="iterate a number of times")
parser.add_argument('-x', metavar='', type=bool, action=argparse.BooleanOptionalAction, help='remove file after shredding')
args = parser.parse_args()
if args.r and args.z:
    print("error: arguments -z and -r can't be used concurrently")
    exit()
elif args.r:
    args.z = False
elif args.z:
    args.r = False
    print(glob(args.destination))
