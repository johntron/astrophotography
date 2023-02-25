from json import load
from os import listdir

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer

from preprocessing import stem

dataset_path = '../headless-crawler/storage/datasets/default'


def each_spec():
    for file in listdir(dataset_path):
        with open(f'{dataset_path}/{file}', 'r') as f:
            json = load(f)
            for (raw_spec, value) in json['specs'].items():
                yield stem(raw_spec), stem(value)


specs = [f'{spec}: {value}' for spec, value in each_spec()]

ngram_vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(2, 2))
X = ngram_vectorizer.fit_transform(specs)

kmeans = KMeans(n_clusters=50).fit(X)

for cluster in set(kmeans.labels_):
    print('\nCluster: {}'.format(cluster))
    for i, label in enumerate(kmeans.labels_):
        if label == cluster:
            print(specs[i])
