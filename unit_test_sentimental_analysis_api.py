import sentimentalAccess
import pytest
from sentimentalAccess import *
from unittest.mock import MagicMock

def test_sentimental_access():
    # check to see api connection with valid key
    google_client = connect_to_google_api()
    assert (google_client)

def test_get_text_to_analyze():
    # check to see if get_text_to_analyze can parse through tweets.csv and save all the data
    data = get_text_to_analyze()
    assert len(data) == 100

def test_write_sentiments_to_csv():
    # check to see if write_sentiments_to_csv actually wrote to sentimentAnalysis.csv
    # confirm header and header count to 2
    # confirm column count to 100
    with open ('sentimentAnalysis.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        column = len(list(reader))
    assert header==['Text', 'Sentiment']
    assert len(header)==2
    assert column==100