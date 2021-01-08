import requests
import json

headers = {"Authorization": "Bearer <token-goes-here>"}

def getTweets(username):
    # remember to remove or modify soft limit (25)
    APIrequestTweets = "https://api.twitter.com/2/tweets/search/all?query=from%3A{}&max_results=25".format(username)
    response = requests.get(APIrequestTweets, headers=headers) 
    debug_printResponse(response)

def debug_jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def debug_getSingularTweet(id):
    APIrequestTweet = "https://api.twitter.com/2/tweets/{}?media.fields=type,url&tweet.fields=id,text,attachments,conversation_id,created_at".format(id)
    response = requests.get(APIrequestTweet, headers=headers) 
    debug_printResponse(response)

def debug_printResponse(response):
    jprint(response.json())
