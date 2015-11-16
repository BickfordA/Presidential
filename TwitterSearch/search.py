import twitter
import json
import argparse

import sys
reload(sys)
sys.setdefaultencoding("ISO-8859-1")

from urllib import unquote


# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information
# on Twitter's OAuth implementation.

CONSUMER_KEY = ''
CONSUMER_SECRET =''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''


auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable


def twitterSearch( search_term):
    count = 100

    search_results = twitter_api.search.tweets(q = search_term, count = count)

    return search_results['statuses']


def month(monthAbbrev):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return str(months.index(monthAbbrev))

def sqlDate(twitter_date):
    date_parts = twitter_date.split(' ')

    if len(date_parts) != 6:
        return ""
    outdate = []
    outdate.append( month(date_parts[1]))
    outdate.append( date_parts[2])
    outdate.append( date_parts[5])

    outstring = ""
    outstring = '-'.join(outdate)
    outstring = outstring +" "+ date_parts[3]
    return outstring


## Read the search terms from twitter and put them in a nice csv for DB import
out_file_mentions = open("outresults_mentions.csv", 'w');
out_file_tags = open("outresults_tags.csv", 'w');
out_file_searches = open("outresults_tweets.csv", 'w')
term_file = open("twitterIds.txt", 'r')

search_id = 0
for line in term_file:
    line = line.rstrip() #remove new lines etc...

    print "Searching for @" + line
    statuses = twitterSearch("@" + line)

    for status in statuses:
        #text = ""
        hashtags = []
        mentions = []

        #read the results from the status
        text =  status['text'].rstrip()
        text = text.replace('"', "'")
        text = "\"" + text +"\"";

        for user_mention in status['entities']['user_mentions']:
                mentions.append(user_mention['screen_name'])

        for hashtag in status['entities']['hashtags']:
                hashtags.append( hashtag['text'] )

        retweet_count = str(status["retweet_count"])

        date_time = sqlDate(status["created_at"])

        # write the records out to the destation files

        twitter_searches = [ str(search_id), line, date_time, text.encode('utf-8' ),retweet_count ]
        out_searches_string = ','.join(twitter_searches)
        out_file_searches.write(out_searches_string)
        out_file_searches.write("\n")

        for tag in hashtags :
            out_file_tags.write(str(search_id))
            out_file_tags.write(",")
            out_file_tags.write(tag.encode('utf-8'))
            out_file_tags.write("\n")

        for men in mentions :
            out_file_mentions.write(str(search_id))
            out_file_mentions.write(",")
            out_file_mentions.write(men.encode('utf-8'))
            out_file_mentions.write("\n")

        search_id = search_id + 1
