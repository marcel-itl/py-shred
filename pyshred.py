import argparse
import os
from glob import glob

class Shred(object):
    def __init__(self, dst: list, z: bool, r: bool, i: int, x: bool) -> None:
        self.dst = [d for d in dst if not os.path.isdir(d)] #file destination(s)
        self.z = z #null shred?
        self.r = r #random shred?
        self.i = i #iterations
        self.x = x #delete file?
        try:
            for fn in self.dst:
                if z:
                    self.zero_shred(fn, i)
                if r:
                    self.random_shred(fn, i)
        except Exception as e:
            print(f"error occurred: {e}")


    def zero_shred(self, dst: str, i: int) -> None:
        with open(dst, 'ba+') as f:
            LENGTH = f.tell()
        with open(dst, 'br+') as f:
            for t in range(1,i+1):
                print(f"shredding file {dst}... try {t} of {i}")
                f.seek(0,0)
                for n in range(0,LENGTH):
                    f.write(b'\x00')
        if self.x:
            print(f"deleting file {dst}")
            os.remove(dst)

    def random_shred(self, dst: str, i: int) -> None:
        with open(dst, 'ba+') as f:
            LENGTH = f.tell()
        with open(dst, 'br+') as f:
            for t in range(1,i+1):
                print(f"shredding file {dst}... try {t} of {i}")
                f.seek(0,0)
                f.write(os.urandom(LENGTH))
        if self.x:
            print(f"deleting file {dst}")
            os.remove(dst)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wipe data from files.')
    req = parser.add_argument_group('required')
    req.add_argument('destination', type=str, help="path to wipe")
    parser.add_argument('-z', metavar='', type=bool, action=argparse.BooleanOptionalAction, help="replace data with null-bytes")
    parser.add_argument('-r', metavar='', type=bool, action=argparse.BooleanOptionalAction, help="replace data with randomly generated output")
    parser.add_argument('-i', metavar="int", type=int, help="iterate a number of times")
    parser.add_argument('-x', metavar='', type=bool, action=argparse.BooleanOptionalAction, help='remove file after shredding')
    args = parser.parse_args()
    if args.r and args.z:
        print("error: arguments -z and -r can't be used concurrently")
        exit()
    shred = Shred(glob(args.destination), args.z, args.r, args.i, args.x)