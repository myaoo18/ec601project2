# EC601 Project 2 Twitter API and Google NLP for Sentiment Analysis

## Overview
This project aims to collect 100 tweets from Elon Musk using Twitter User API v2 and analyze his sentiment using Google NLP API. This works by accessing endpoints, saving tweets collected in CSV format and using a sentiment analysis trained model to analyze texts. More specifically, 100 most recent tweets from Elon Musk was collected through the User Lookup API to receive up-to-date details and each tweets is ranked with a sentiment analysis value. Below, there are detailed steps on how the API was used and results collected.

## How to use Twitter API
### Prerequisites to Start
1) Go to the developer portal dashboard https://developer.twitter.com/en/portal/dashboard 
2) Sign in with your developer account or create one if you don't already have one
3) Create a new project, give it a name and a description

Using jupyter notebook to code in python

4) In your terminal, type "brew install jupyter"
5) Upon installation, type "jupyter notebook" which a new browser would pop up 

### Code Implementation in Jupyter Notebook
1) Follow the folder twitter_api.ipynb step by step 
2) Prior to step 2, type export 'BEARER_TOKEN'='<Your_bearer_token>' in your terminal. Your bearer token can be found in your developer account from creating a new project
3) In step 3, url can be changed to any users you want to analyze. 
"https://api.twitter.com/2/users/'<user account id you want to explore>'/tweets"
  
Change "user account id you want to explore" into a user account id that you want to explore using https://codeofaninja.com/tools/find-twitter-id/ to search for the id
  
4) Hit Run for each cell and your result should display

## How to use Google NLP API
### How to Start
1) Create a google cloud account if you haven't already
2) Follow all the steps from here: https://cloud.google.com/natural-language/docs/reference/libraries

### Use the Tweet csv You Saved
1) Modify your python code by adding these libraries
```
import pandas as pd
import csv
```
2) Get rid of everything starting from "Hello, world" text and add in a for loop that reads each row of the text column and save all the text and sentiment scores into another csv file
```
col_list = ["conversation_id", "created_at", "lang", "text"]
df = pd.read_csv("tweets.csv", usecols=col_list)
data = []
for elonText in df["text"]:
    text = elonText
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    eachData = []
    eachData.append("{}".format(text))
    eachData.append("{}, {}".format(sentiment.score, sentiment.magnitude))
    data.append(eachData)
    # print("Text: {}".format(text))
    # print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

header = ['Text', 'Sentiment']

with open('sentimentAnalysis.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data) 
```

  
## Results
Please see tweets.csv and sentimenAnalysis.csv
  
## Resources
1) https://www.youtube.com/watch?v=pJUN9Rsu_30
2) https://cloud.google.com/natural-language/docs/reference/libraries
