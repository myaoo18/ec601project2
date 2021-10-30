import ipynb.fs.full.twitter_api
import pytest
from ipynb.fs.full.twitter_api import *

def test_connect_to_api():
    # check to see api connection with valid bearer token
    header = connect_to_api()
    assert all(header)

def test_send_request():
    # check to see if api responds with valid bearer token connection to twitter api
    response = send_request(connect_to_api())
    assert all(response)

def test_make_data_frame():
    # check to see if data frame has 5 columns, 100 rows and specific headers
    headers = connect_to_api()
    response = send_request(headers)
    data_frame = make_data_frame(response)
    assert len(data_frame.columns) == 5
    assert len(data_frame) == 100
    order_data_frame_columns = sorted(data_frame.columns)
    assert (order_data_frame_columns==['conversation_id', 'created_at', 'id', 'lang', 'text'])

def test_error_call():
    # check to see api throws an error gracefully when bearer token is invalid
    BEARER_TOKEN = ''
    header = connect_to_api()
    response = send_request(header)
    AssertionError(header)
    AssertionError(response)