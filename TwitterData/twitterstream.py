# this following code will gather all the upcoming tweets ab a particular event
# once the code is executed, data will be appended in python.json
# https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
from tweepy import Stream
from tweepy.streaming import StreamListener

from tweepy import OAuthHandler

consumer_key = '7iv3cn2Dr3BfnBnZppazPR5tU'
consumer_secret = 'BQgI9TVlbZqBCVJ7vcVTPb11s57wz2dy2lc9NbVK5ZWCBN2iIP'
access_token = '917657381676367872-Nzkcp184h6jFzGIirn8SMrZg2DDqFMm'
access_secret = 'SKKc28qcS8EJUmgR601qgFpWzFeRZl0N9nTNu7F1cY4mW'


#In order to authorise our app to access Twitter on our behalf, we need to use the OAuth interface:
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])
