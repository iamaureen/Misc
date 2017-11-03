import tweepy
import json

from tweepy import OAuthHandler

from nltk.tokenize import word_tokenize

consumer_key = '7iv3cn2Dr3BfnBnZppazPR5tU'
consumer_secret = 'BQgI9TVlbZqBCVJ7vcVTPb11s57wz2dy2lc9NbVK5ZWCBN2iIP'
access_token = '917657381676367872-Nzkcp184h6jFzGIirn8SMrZg2DDqFMm'
access_secret = 'SKKc28qcS8EJUmgR601qgFpWzFeRZl0N9nTNu7F1cY4mW'


#In order to authorise our app to access Twitter on our behalf, we need to use the OAuth interface:
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
# The api variable is now our entry point for most of the operations we can perform with Twitter.

# If the authentication was successful, you should
# see the name of the account print out
def getUserName():
    print(api.me().name)

#print datain json format
def printAsJSON(data):
    print(json.dumps(data))

#we can read our own timeline (i.e. our Twitter homepage)
#Only iterate through the first 10 statuses
#reference: https://github.com/tweepy/tweepy/blob/master/docs/cursor_tutorial.rst
def readTwitterTimeline():
    for status in tweepy.Cursor(api.home_timeline).items(10):
        # Process a single status
        # print(status.text)
        #process result as json
        printAsJSON(status._json)

def readOurTweets():
    #a list of all our tweets
    for tweet in tweepy.Cursor(api.user_timeline).items(10):
         print(printAsJSON(tweet))

#http://docs.tweepy.org/en/v3.3.0/api.html
#get the number of following for our own profile:
#which is also known as friends
def getTwitterFriends():
    print("Number of people following :: ", len(list(tweepy.Cursor(api.friends).items())))
    for friend in tweepy.Cursor(api.friends).items():
        #print each friend name
        #print(friend.name)
        #process result as json
        printAsJSON(friend._json)

#get follower from my own profile
def getTwitterFollower():
    for follower in tweepy.Cursor(api.followers).items():
        #print(friend.name)
        printAsJSON(follower._json)

#get information ab a specific user based on their screen name as paramter
def getInfoAbSpecificUser(name):
    user = api.get_user(name)
    print(user._json)
    print (user.screen_name)
    print (user.friends_count)


#get tweet from a specific user given
def getTweetFromSpecificUser(name, noOfTweetToPull):
    #Calling the user_timeline function with our parameters
    results = api.user_timeline(id=name, count=noOfTweetToPull)
    #foreach through all tweets pulled
    for tweet in results:
   #printing the text stored inside the tweet object
        print (tweet.text)

def specific_query(query, language):
    results = api.search(q=query, lang=language)
    # foreach through all tweets pulled
    for tweet in results:
        #printing the text stored inside the tweet object
        #print (tweet.user.screen_name,"Tweeted:",tweet.text)
        #print the whole json with all info
        print(tweet._json)


#assuming twitterstream.py has been executed and data is stored in python.json
#the following function will help to understand the data
#this prints out only the first json
def getStreamData():
    with open('python.json', 'r') as f:
        line = f.readline() # read only the first tweet/line
        tweet = json.loads(line) # load it as Python dict
        print(json.dumps(tweet, indent=4)) # pretty-print

# couldnot run
# def tokenizeText():
#     tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
#     print(word_tokenize(tweet))



if __name__ == '__main__':
    #call the methods here
    #get my user name
    getUserName()

    #print("read timeline from our own profile")
    #readTwitterTimeline()

    #print("read our own tweets")
    #readOurTweets()

    #print("get friends from our own profile")
    #getTwitterFriends()

    #print("get follower count from our own profile")
    #getTwitterFollower()

    #print("get information ab a given specific user 'screen_name' as parameter")
    # getInfoAbSpecificUser("iamaureen08")

    #print("get tweet from a specific user")
    #getTweetFromSpecificUser("nytimes", 20)

    #print("query a specific topic over twitter")
    #specific_query("panda", "en")

    #get stream data from twitterstream.py
    #getStreamData()



