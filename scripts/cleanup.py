import sys
import subprocess
import os



def main():
    subprocess.run(["rm -r *.csv"])
    subprocess.run(["rm -r *.csv.gz"])


if __name__ == '__main__':
    main()