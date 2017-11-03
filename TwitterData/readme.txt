ref links: https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
reference for tweepy package: https://github.com/tweepy/tweepy
also: http://docs.tweepy.org/en/v3.5.0/getting_started.html
also: https://developer.twitter.com/en/docs/api-reference-index

1. create app after logging into twitter account: https://apps.twitter.com/
2. a consumer key and a consumer secret will be provided: these are application settings that should always be kept private
also access token and access token secret key will be provided. these are necessary to connect to the app
3. go to cmd prompt and type pip install tweepy==3.3.0

4. "twitterstream.py": gathers all the upcoming tweets ab a particular event and stores into python.json
getStreamData() in twitterData will display the tweet in readable way. the key attributes are mentioned in the ref url
for example, text, favorite_count, retweet_count, id, place, coordinates, user, entities, in_reply_to_user_id etc

5. tokenize the text using NLKT library: http://www.nltk.org/
<unable to download nltk 10/20>

6. readTwitterTimeline() method pulls the 10 most recent tweets from the timeline. It returns a json with lots of information
for example tweet.user.screen_name, tweet.user.location can be used if any applicatin needs spatial data

7. get tweet from a specific user
ref: https://www.toptal.com/python/twitter-data-mining-using-python

8. get recent tweets that contain a keyword
ref: https://www.toptal.com/python/twitter-data-mining-using-python

9.





