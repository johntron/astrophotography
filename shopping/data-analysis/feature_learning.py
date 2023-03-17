import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

from preprocessing import stem
from raw_data import each_spec

dataset_path = '../headless-crawler/storage/datasets/default'

raw = [raw_spec for raw_spec, _ in each_spec()]
values = [value for _, value in each_spec()]
stemmed = [stem(raw_spec) for raw_spec in raw]
data = stemmed
print(len(data))

# vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(1, 2))
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data)
print(X, X.shape)

vocab = list(vectorizer.vocabulary_.keys())
vocab.sort()
print(f'vocab ({len(vocab)}):', '\n'.join(vocab))

n_clusters = 75
kmeans = KMeans(n_clusters=n_clusters).fit(X)
clusters = pd.DataFrame(0, index=raw, columns=['stemmed', 'value'] + list(range(n_clusters)))
clusters['stemmed'] = stemmed
clusters['value'] = values

for cluster in set(kmeans.labels_):
    print('\nCluster: {}'.format(cluster))
    for i, label in enumerate(kmeans.labels_):
        if label == cluster:
            clusters[cluster][i] = True

print(clusters)
clusters.to_csv('clusters.csv')
