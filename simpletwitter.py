# I am just hacking around with the Twitter API
# This ain't a finished product :-)

import urllib2
import simplejson
def query(str):
    request = urllib2.Request(str)
    response = urllib2.urlopen(request)
    return simplejson.load(response)

def get_recent_tweets(user_name, count):
    return query('https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&screen_name='+user_name+'&count='+str(count))

def display_recent_tweets(user_name, count = 10):
    tweets = get_recent_tweets(user_name, count)
    for tweet in tweets:
        print '%s (%s)' % (tweet['text'], tweet['created_at'])

def get_followers(user_name, cursor = -1):
    return query('https://api.twitter.com/1/followers/ids.json?cursor='+str(cursor)+'&screen_name='+user_name)

def display_follower_count(user_name):
    follower_ids = get_followers(user_name)
    print (len(follower_ids['ids']) if (follower_ids['next_cursor_str'] == '0') else '> 5000')
    
screen_name = 'aplusk'
display_recent_tweets(screen_name)
display_follower_count(screen_name)
