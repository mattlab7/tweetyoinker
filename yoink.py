import requests
import json
# from yoinkconsts import headers

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def getTweets(username):
    APIrequestLink = "https://api.twitter.com/2/users/by?usernames={}?media.fields=type,url&tweet.fields=id,text,attachments,conversation_id,created_at".format(username)
    response = requests.get(APIrequestLink, headers=headers) 
    debug_printResponse(response)

def debug_getSingularTweet(id):
    APIrequestLink = "https://api.twitter.com/2/tweets/{}?media.fields=type,url&tweet.fields=id,text,attachments,conversation_id,created_at".format(id)
    response = requests.get(APIrequestLink, headers=headers) 
    debug_printResponse(response)

def debug_printResponse(response):
    jprint(response.json())

# testing

# by single tweet
# content = "1346264487175675905"
# debug_getSingularTweet(content)

# by user
# content = "forsen"
# getTweets(content)
