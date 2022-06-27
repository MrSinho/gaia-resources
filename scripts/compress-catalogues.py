import sys
import subprocess
import os

def id_to_filename(i):
    filename_list = list(str(i))
    while (len(filename_list) < 4):
        filename_list.insert(0, 0)
    return "".join(str(v) for v in filename_list)

def compress_catalogues(range_start, range_end):
    for i in range (range_start, range_end, 1):
        src_name = "../gaia-bin/gaiaUniverseModel_" + id_to_filename(i) + ".bin"
        dst_name = "../gaia-bin/gaiaUniverseModel_" + id_to_filename(i) + ".rar"
        print(f"Converting {src_name} to {dst_name}")
        #subprocess.call(f"./../bin/gaia-exp {src_name} {dst_name}", stdout=FNULL, stderr=FNULL, shell=False)
        os.system(f"rar a -r {dst_name} {src_name}")

def main():
    range_start = 0
    range_end = 5000
    if (len(sys.argv) > 1):
        if (sys.argv[1].isnumeric()): 
            range_start = int(sys.argv[1])
            range_end   = int(sys.argv[1])+1
    if (len(sys.argv) > 2):
        if (sys.argv[2].isnumeric()): range_end = int(sys.argv[2])+1
    compress_catalogues(range_start, range_end)

if __name__ == '__main__':
    main()