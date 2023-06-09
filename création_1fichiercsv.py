# -*- coding: utf-8 -*-
"""création_1fichiercsv.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16B_u1D2m96hwnM_0ywlzvY2mUaFqEmed
"""

from google.colab import drive
drive.mount('/content/drive')

!ls '/content/'

import pandas as pd
df=pd.read_csv('nr_2019-10.csv')

df

# Importing the os library
import os
import pandas as pd

# The path for listing items
path = '/content/'
 
# The list of items
files = os.listdir(path)
df = pd.DataFrame()
# Loop to print each filename separately
for filename in files:
  if filename[:2]=='nr':
     #df.concat(pd.read_csv(filename))
     df = df.append(pd.read_csv(filename), ignore_index=True)

df.describe()

min(df['day'])

dfcsv = df.to_csv('global.csv')