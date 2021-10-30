# Imports the Google Cloud client library
import pandas as pd
import csv
from google.cloud import language_v1

def connect_to_google_api():
    # Instantiates a client
    client = language_v1.LanguageServiceClient()
    return client

google_client = connect_to_google_api()
def get_text_to_analyze(): 
    # The text to analyze
    col_list = ["conversation_id", "created_at", "lang", "text"]
    df = pd.read_csv("tweets.csv", usecols=col_list)
    data = []
    for elonText in df["text"]:
        text = elonText
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

        # Detects the sentiment of the text
        sentiment = google_client.analyze_sentiment(request={'document': document}).document_sentiment

        eachData = []
        eachData.append("{}".format(text))
        eachData.append("{}, {}".format(sentiment.score, sentiment.magnitude))
        data.append(eachData)
        # print("Text: {}".format(text))
        # print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
    return data

all_data = get_text_to_analyze()

def write_sentiments_to_csv():
    header = ['Text', 'Sentiment']
    with open('sentimentAnalysis.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(all_data)
    return f
write_sentiments_to_csv()