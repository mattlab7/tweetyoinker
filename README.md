# tweetyoinker

<img src="https://static.wikia.nocookie.net/yokaiwatch/images/7/7f/Yoink_Art.jpg" width="150px" align="right"></img>

A mini program written in Python to scrape media off of a tweet, originally planned to scrape an entire twitter profile, but due to limitations from Twitter API, this functionality is not implemented

## installation
Edit the source with your personal developer token, if you do not have one,
[apply a developer token at Twitter's Developer Portal](https://developer.twitter.com/en/portal/dashboard)

    pip3 install requests-oauthlib
    python3 yoink.py

## usage

Enter a link, the program will identify the type of media, if successful, it will display a direct download link.

[try on repl.it](https://repl.it/@mattlab/tweetyoinker)

it works on images!

![image demo](https://a.pomf.cat/bexons.png)

videos

![video demo](https://a.pomf.cat/rcfuly.png)

and last but not least, albums!

![album demo](https://a.pomf.cat/skibuw.png)
