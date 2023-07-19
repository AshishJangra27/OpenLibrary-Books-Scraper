import os
import pandas as pd
from tqdm import tqdm

csvs = [csv for csv in sorted(os.listdir('OpenLibrary-Books-Scraper/data')) if '.csv' in csv]

df = pd.DataFrame()

for csv in tqdm(csvs):
    df_ = pd.read_csv('OpenLibrary-Books-Scraper/data/' + csv )
    df_['category_'] = csv.split('.csv')[0]
    df = pd.concat((df,df_))
    
df.to_csv('data.csv', index = False)
