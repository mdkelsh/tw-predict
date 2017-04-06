import tweepy
from tweepy import OAuthHandler
import simplejson as json

def setup():
    # Acount specific
    consumer_key = '######'
    consumer_secret = '#####'
    access_token = '#####'
    access_secret = '#####''

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    try:
            with open('corpus.json', 'a') as f:
    # store timeline to json
                for status in tweepy.Cursor(api.home_timeline).items(10):
                    f.write(json.dumps(status._json))
    except BaseException as e:
        print("Error on_data: %s" % str(e))
    return True
    
if __name__ == "__main__":
    setup()
