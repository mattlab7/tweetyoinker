import json
from requests_oauthlib import OAuth1Session

# authentication (v1.1 // oauth 1.0)
oauthv1 = OAuth1Session('<api token>', client_secret='<api secret>', resource_owner_key='<account token>', resource_owner_secret='<account secret>')

# twitter api v2 doesn't really look good for media fetching, using v1.1
def getTweet(tweetID):
    tweetRequest = "https://api.twitter.com/1.1/statuses/show.json?id={}&tweet_mode=extended".format(tweetID)
    tweetResponse = oauthv1.get(tweetRequest)

    return tweetResponse

def processing(tweetResponse):
    tweetResponse = tweetResponse.json()

    # this will attempt to catch tweets without media, program will exit when it isn't
    try:
        mediatype = tweetResponse['extended_entities']['media'][0]['type']
    except KeyError:
        print("No media detected")
        return

    print("\n\n========== yoink results ==========")
    print("Creation: " + tweetResponse['created_at'])

    # twitter api will truncate certain tweets based on length, so, if the text field is not detected, there will be certain a full_text field
    try:
        print("Tweet Contents: " + tweetResponse['text'])
    except:
        print("Tweet Contents: " + tweetResponse['full_text'])

    print("User: " + tweetResponse['user']['name'] + " (@" + tweetResponse['user']['screen_name'] + ")")
    print("Media Type: " + mediatype)
    
    if (mediatype == 'photo'):
        print("Media Direct Link(s);")
        
        for photo in tweetResponse['extended_entities']['media']:
            print("• " + photo['media_url_https'])
            print("Source Media Resolution: " + str(photo['sizes']['large']['h']) + " height - " + str(photo['sizes']['large']['w']) + " width")
    elif (mediatype == 'video'):
        print("Duration: " + str(tweetResponse['extended_entities']['media'][0]['video_info']['duration_millis'] / 1000) + " second(s)")
        
        print("Media Direct Link(s);")
        for variant in tweetResponse['extended_entities']['media'][0]['video_info']['variants']:
            if (variant['content_type'] == "application/x-mpegURL"):
                break
            print("• Bitrate [" + str(variant['bitrate']) + "] --- URL: " + variant['url'])
        
        print("Source Media Resolution: " + str(tweetResponse['extended_entities']['media'][0]['sizes']['large']['h']) + " height - " + str(tweetResponse['extended_entities']['media'][0]['sizes']['large']['w']) + " width")    

    return

def inputFormatting(userInput):
    userInput = userInput.split("/")

    if (len(userInput) == 1):
        tweetID = userInput[0]
    else:
        if (userInput[2] == "twitter.com"):
            tweetID = userInput[5]
        elif (userInput[0] == "twitter.com"):
            tweetID = userInput[3]

    return tweetID

# debug method to show what is in the response
def debug_jprint(obj):
    text = json.dumps(obj.json(), sort_keys=True, indent=4)
    print(text)

userInput = input("tweetyoinker!\n==================\nEnter your twitter link here (or tweet ID)\n\n")
processing(getTweet(inputFormatting(userInput)))

