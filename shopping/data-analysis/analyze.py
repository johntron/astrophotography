from json import load
from os import listdir

import numpy as np
import pandas as pd
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import seaborn as sns

dataset_path = '../headless-crawler/storage/datasets/default'

dfs = []
for file in listdir(dataset_path):
    with open(f'{dataset_path}/{file}', 'r') as f:
        json = load(f)
        dfs.append(pd.json_normalize(json))

df = pd.concat(dfs)
df['price'] = df['price'].astype(np.float32)

print('\n'.join(list(map(lambda val: val.replace('specs.', '') ,filter(lambda val: 'specs.' in val, df.columns.sort_values())))))
print(df.dtypes)
# sns.histplot(df['price'], bins=20, binrange=(0, 5000))
sns.kdeplot(df[df['price'] < 4000]['price'], bw_adjust=0.5)
plt.show()