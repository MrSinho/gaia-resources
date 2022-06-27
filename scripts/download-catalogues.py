import sys
import requests
import gzip
import shutil

def id_to_filename(i):
    filename_list = list(str(i))
    while (len(filename_list) < 4):
        filename_list.insert(0, 0)
    return "".join(str(v) for v in filename_list)

def unzip_gaia_catalogue(directory, filename, extension):
    src = gzip.open(directory+filename+extension, "rb")
    dst = open(directory+filename+".csv", "wb")
    shutil.copyfileobj(src, dst)

def download_gaia_catalogue(filename):
    extension = ".csv.gz"
    filename = filename
    link = "http://cdn.gea.esac.esa.int/Gaia/gedr3/simulation/gaia_universe_model/" + "GaiaUniverseModel_" + filename + extension
    print(f"downloading {link}\n")
    buffer = requests.get(link)
    directory = "../"
    open(directory+"gaiaUniverseModel_"+filename+extension, "wb").write(buffer.content)    
    unzip_gaia_catalogue(directory, "gaiaUniverseModel_"+filename, extension)

def download_catalogues(range_start, range_end):
    for i in range (range_start, range_end, 1):
        filename = id_to_filename(i)
        download_gaia_catalogue(filename)

def main():
    range_start = 0
    range_end = 5000
    if (len(sys.argv) > 1):
        if (sys.argv[1].isnumeric()): 
            range_start = int(sys.argv[1])
            range_end   = int(sys.argv[1])+1
    if (len(sys.argv) > 2):
        if (sys.argv[2].isnumeric()): range_end = int(sys.argv[2])+1
    download_catalogues(range_start, range_end)

if __name__ == '__main__':
    main()