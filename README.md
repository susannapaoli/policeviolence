# Police Violence and Racial Narratives in the US: The Impacts of George Floyd's Murder and the 'Black Lives Matter' Movement in Journalism
The project analyzes linguistic patterns in news articles about police violence in the US, from 2013 to 2024. More specifically, we are interested in investigating the racial bias connecting white people to mental illness and black people to criminality. We aim to identify clustered articles around stereotyped narratives by leveraging word embeddings. \
Repo structure:
1. get_data: a full functioning pipeline to create the dataset with textual data. The notebook contains a scraper that uses the 'requests' and 'newspaper' libraries to retrieve articles from the URLs in the dataset. It then joins all files and creates a unique functioning dataset. 
2. data_cleaning: process the data, remove unwanted content, select fundamental features
3. exploratory data analysis: explores the dataset, and analyzes unigrams, bigrams, and salient tokens across ethnicities and geography; extracts descriptive statistics
4. word2vec: main notebook for text preprocessing and word embedding training, with hyperparameter tuning using a stemmer
5. word2vec_lemmatized: same word2vec analysis, but employing a lemmatizer to tokenize the corpus
6. analysis: bias calculations and comparison (analysis before, after, states refer to analysis performed on the articles for incidents before George Floyd's murder, after George Floyd's murder, and across US states, respectively).
7. data folder: contains csv files
8. model folder: contains saved word2vec models used in the analysis
9. image folder: contains images generated for the report
