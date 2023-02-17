from os import listdir
from os.path import splitext

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import load_files


dataset_path = '../headless-crawler/storage/key_value_stores'

docs = load_files(
    dataset_path,
    allowed_extensions=['.txt']
)

# docs = pd.Series()
# for file in listdir(dataset_path):
#     if splitext(file)[1] != '.txt':
#         continue
#     with open(f'{dataset_path}/{file}', 'r') as f:
#         lines = f.readlines()
#         docs.append(lines)

vectorizer_ng3 = CountVectorizer(ngram_range=(1, 3))
ng3 = vectorizer_ng3.fit_transform(docs.data)
print(vectorizer_ng3.get_feature_names_out())
print(ng3[0][0:1000])
