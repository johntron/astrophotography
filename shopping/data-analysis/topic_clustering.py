from os import unlink

import tensorflow as tf
from top2vec import Top2Vec

from raw_data import each_txt

top2vec_model_path = "top2vec_model"

'''
Installation of top2vec requires python headers: `sudo apt install python3-dev`
And these requirements for gpu: https://www.tensorflow.org/install/pip#software_requirements
'''
print(tf.config.list_physical_devices('GPU'))

glob_pattern = '../headless-crawler/storage/key_value_stores/default/*.txt'
docs = [doc for doc in each_txt(glob_pattern)]

top2vec_model_path = 'topic_clustering_model'
rebuild = True
try:
    if rebuild:
        unlink(top2vec_model_path)
    model = Top2Vec.load(top2vec_model_path)
    print('Loaded model')
except FileNotFoundError as e:
    print('No model found, training model')
    model = Top2Vec(
        docs,
        speed="learn",
        workers=8,
        embedding_model='universal-sentence-encoder-large'
    )
    model.save(top2vec_model_path)
    print('Saved model')

print(f'{model.get_num_topics()} topics')
words, word_scores = model.similar_words(keywords=["telescope"], keywords_neg=[], num_words=20)
for word, score in zip(words, word_scores):
    print(f"{word} {score}")
topic_words, word_scores, topic_nums = model.get_topics(1)
documents, document_scores, document_ids = model.search_documents_by_topic(topic_num=1, num_docs=5)
print(documents)

print(model)
