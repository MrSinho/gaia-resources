import sys
import subprocess
import os



def main():
    if (len(sys.argv) == 2):
        dir = "../"
        idx = str(sys.argv[1])
        print(f"Splitting catalogue {idx} at {dir}")
        subprocess.run(["./../bin/gaia-split", dir, idx])
    elif (len(sys.argv) == 3):
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        dir = "../"
        for i in range (start, end, 1):
            idx = str(i)
            print(f"Splitting catalogue {idx} at {dir}")
            subprocess.run(["./../bin/gaia-split", dir, idx])


if __name__ == '__main__':
    main()