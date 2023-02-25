from json import load
from os import listdir

import nltk
import pandas as pd

from preprocessing import normalize, stem

nltk.download('wordnet')

dataset_path = '../headless-crawler/storage/datasets/default'

stemmed_to_normalized = {}


def add_stemmed(stemmed: str, original: str):
    if stemmed not in stemmed_to_normalized.keys():
        stemmed_to_normalized[stemmed] = normalize(original)


dfs = []
for file in listdir(dataset_path):
    with open(f'{dataset_path}/{file}', 'r') as f:
        json = load(f)
        normalized_specs = {}
        for (raw_spec, value) in json['specs'].items():
            stemmed = stem(raw_spec)
            add_stemmed(stemmed, raw_spec)
            normalized_spec = stemmed_to_normalized[stemmed]
            normalized_specs[normalized_spec] = value
        json['specs'] = normalized_specs
        del json['html']
        dfs.append(pd.json_normalize(json))
dfs = pd.concat(dfs)

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
print(dfs.head())
