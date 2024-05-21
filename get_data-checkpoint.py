%%capture
!pip install newspaper3k

import pandas as pd
import numpy as pd 
import os
from newspaper import Article

def create_dataset(dataset, csv_files, folder_path = 'data'):
    all_files_exist = all(os.path.exists(os.path.join(folder_path, file)) for file in csv_files)
    
    if os.path.exists(os.path.join(folder_path, dataset)):
        df = pd.read_csv('data/full_dataset_mpv.csv')
        print("Dataset created and saved.")
        
    
    elif all_files_exist: 
        dfs = [pd.read_csv(os.path.join(folder_path, file)) for file in csv_files]
        for df in dfs:
            df.colums = df.columns.str.strip()
        df = pd.concat(dfs, ignore_index=True)
        df.to_csv("data/full_dataset_mpv.csv")
        print("All files were successfully concatenated and saved.")
        print("Dataset created and saved.")
    else: 
        mpv = pd.read_csv("data/Mapping Police Violence.csv")
        mpv.loc[:,'text'] = None
        mpv.loc[:,'authors'] = None
        mpv.loc[:,'fu'] = None

        for i, row in mpv.iterrows():
            articles = []
            authors = []
            fu = []
            j = 0
            for url in row.news_urls.split('\n\n'):
                if url is None:
                    continue
                article = Article(url)
                article.download()
                article.html
                try:
                    article.parse()
                except Exception:
                    continue
                articles.append([article.text])
                authors.append(article.authors)
                fu.append(url)
                j += 1
            mpv.at[i, "text"] = articles
            mpv.at[i, "authors"] = authors
            mpv.at[i, "fu"] = fu
        df = mpv.copy()
    return df

csv_files = ['text_1.csv', 'text_2.csv', 'text_3.csv', 'text_4.csv']
df = create_dataset(dataset = 'full_dataset_mpv', csv_files = csv_files)