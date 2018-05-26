# SENTIMENT ANALYSIS

predicting the sentiment of tweets

The repository contains a create_dataset_code.py file with which the dataset is created. 
run create_dataset.py > twitter_dataset.txt to pipeline the results of the python file to twitter_dataset.txt.

The jupyter notebook contains the code for the sentiment analysis.

## DEPENDENCIES 

1. nltk for text manipulation and machine leearning model
2. pandas for dataframes
3. matplotlib for data visualization

## DATASET

my dataset is based on indian politics

To change the topic of your dataset change this code on line 22 in create_dataset_code.py
stream.filter(track=["Narendra Modi", "Rahul Gandhi", "BJP", "INC"])

in the local_config file add the console token, console secret, application token and application secret of your twitter app
