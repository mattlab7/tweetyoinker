import requests, json, oauthlib
from requests_oauthlib import OAuth1Session

# headers for authentication (v1.1 and v2 respectively )
headersv1 = OAuth1Session('client_key', client_secret='client_secret', resource_owner_key='resource_owner_key', resource_owner_secret='resource_owner_secret')
headersv2 = {"Authorization": "Bearer <token>"}

def getUserID(username):
    UIDrequest = "https://api.twitter.com/2/users/by?usernames={}".format(username)
    UIDresponse = requests.get(UIDrequest, headers=headersv2)

    # why this mess? 
    # twitter api response nests an object inside of an array (which is inside of an object)
    # i had to learn json syntax to finally be able to do this (＃`Д´)	
    # worth it, i think 
    return UIDresponse.json()['data'][0]['id']

def getFleet(userID):
    # fleet: a group of ships sailing together, engaged in the same activity, or under the same ownership.
    # so, essentially, a list of tweets in this context
    fleetRequest = "https://api.twitter.com/2/users/{}/tweets?expansions=attachments.media_keys,attachments.poll_ids,geo.place_id&tweet.fields=conversation_id,created_at&max_results=5".format(userID)
    fleetResponse = requests.get(fleetRequest, headers=headersv2) 

    return fleetResponse

# it looks like twitter api v2 doesn't really look good for media fetching, rolling back to v1 just for this purpose, in progress
# def getTweet(tweetID):
    # tweetRequest = "https://api.twitter.com/2/tweets/{}?media.fields=type,url&tweet.fields=id,text,attachments,conversation_id,created_at".format(id)
    # tweetResponse = requests.get(tweetRequest, headers=headersv2)

    # tweetRequest = "https://api.twitter.com/1.1/statuses/lookup.json?id={}".format(id)
    # tweetResponse = headersv1.get(tweetRequest)

    # return tweetResponse

def fleetOwner(username):
    # line 16-17 for explaination
    userID = getUserID(username)
    tweetResponse = getFleet(userID)
    debug_jprint(tweetResponse)

def tweetQuery(tweetID):
    tweetResponse = getTweet(tweetID)
    debug_jprint(tweetResponse)

def debug_jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj.json(), sort_keys=True, indent=4)
    print(text)

def debug_printResponse(response):
    debug_jprint(response.json())