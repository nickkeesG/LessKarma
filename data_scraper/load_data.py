from os import listdir
from os.path import isfile, join
from functools import reduce

import json

def load_file(fname):
    try:
        with open(fname, 'r') as f:
            return json.load(f)['results']
    except:
        print('Error opening file', fname)
        raise Exception

def load_data(data_dir):
    filenames = [join(data_dir, f) for f in listdir(data_dir) if isfile(join(data_dir, f))]
    return reduce(lambda a, b: a + b, [load_file(f) for f in filenames])
