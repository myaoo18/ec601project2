# EC601 Project 2 Twitter API

## Overview
This project aims to collect tweets from Twitter API v2 by accessing endpoints and saving tweets collected in CSV format. More specifically, 100 most recent tweets from Elon Musk was collected through the User Lookup endpoint to receive up-to-date details on a given user. Below, there are detailed steps on how the API was used and result collected.

## How to use
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
Change '<user account id you want to explore>' into a user account id that you want to explore using https://codeofaninja.com/tools/find-twitter-id/ to search for the id
4) Hit Run for each cell and your result should display

## Results
Results please see tweets.csv
