# Imports the Google Cloud client library
import pandas as pd
import csv
from google.cloud import language_v1


# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
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