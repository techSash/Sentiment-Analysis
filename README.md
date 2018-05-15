# Sentiment-Analysis
predicting the sentiment of tweets

The repository contains a create_dataset.py file with whoch the dataset is created. 
run create_dataset.py > twitter_dataset.txt to pipeline the results of the python file to twitter_dataset.txt.

The jupyter notebook contains the code for the sentiment analysis.

The libraries used were 

nltk for text manipulation and machine leearning model
pandas for dataframes
matplotlib for data visualization

my dataset is based on indian politics

To change the topic of your dataset change this code on line 22 in create_dataset_code.py
stream.filter(track=["Narendra Modi", "Rahul Gandhi", "BJP", "INC"])
