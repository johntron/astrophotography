from glob import glob
from json import load
from os import listdir


def each_txt(glob_pattern):
    for path in glob(glob_pattern):
        with open(path, 'r') as f:
            yield f.read()


def each_spec(dataset_path):
    for file in listdir(dataset_path):
        with open(f'{dataset_path}/{file}', 'r') as f:
            json = load(f)
            for (raw_spec, raw_value) in json['specs'].items():
                yield raw_spec, raw_value
