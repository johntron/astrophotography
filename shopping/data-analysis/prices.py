from json import load
from os import listdir

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

matplotlib.use('Qt5Agg')

dataset_path = '/home/johntron/Development/headless-crawler/storage/datasets/default'

dfs = []
for file in listdir(dataset_path):
    with open(f'{dataset_path}/{file}', 'r') as f:
        json = load(f)
        dfs.append(pd.json_normalize(json))

df = pd.concat(dfs)
print(df.shape)
df['rating'] = df['rating'].str.strip().str.split('/')[0].str[0].astype(int)
df.sort_values(by='rating')
sns.histplot(df['rating'], bins=10)
sns.kdeplot(df['rating'])
plt.show()
exit()
# df['price'] = df['rating'].astype(np.float32)

print('\n'.join(
    list(map(lambda val: val.replace('specs.', ''), filter(lambda val: 'specs.' in val, df.columns.sort_values())))))
print(df.dtypes)
# sns.histplot(df['price'], bins=20, binrange=(0, 5000))
sns.kdeplot(df[df['price'] < 4000]['price'], bw_adjust=0.5)
plt.show()
