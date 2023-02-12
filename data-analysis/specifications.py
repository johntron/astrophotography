from json import load
from os import listdir
from pprint import pprint

from nltk import tokenize, stem

dataset_path = '../headless-crawler/storage/datasets/default'

stemmer = stem.PorterStemmer()


def normalize(s: str):
    words = tokenize.wordpunct_tokenize(s.lower().strip())
    return ' '.join([stemmer.stem(w) for w in words])


lookup = dict()


def build_lookup():
    bases = set()
    for file in listdir(dataset_path):
        with open(f'{dataset_path}/{file}', 'r') as f:
            json = load(f)
            specs = json['specs'].keys()
            mapped = dict([(spec, normalize(spec)) for spec in specs])
            for (spec, base) in mapped.items():
                if base not in bases:
                    lookup[base] = spec
                    bases.add(base)

    # pprint(bases)
    return lookup


build_lookup()
for file in listdir(dataset_path):
    with open(f'{dataset_path}/{file}', 'r') as f:
        json = load(f)
        normalized_specs = dict([(lookup[normalize(spec)], value) for (spec, value) in json['specs'].items()])
        pprint(json.keys())

