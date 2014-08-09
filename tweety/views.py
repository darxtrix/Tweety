from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from markov_bot import Tweet_Generator
from twython import Twython

import random
import settings


def get_tweet_history(screen_name = 'bhogleharsha'):
    twt = Twython(settings.API_KEY,settings.API_SECRET)
    time_line = twt.get_user_timeline(screen_name = screen_name,count = 200) # at max retrieves 200 tweets
    tweets_list = [ tweet['text'] for tweet in time_line ]
    twt_gen = Tweet_Generator(tweets_list)
    next_tweet = twt_gen.generate_tweet(size = 20)
    return next_tweet
 