from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import Context
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from markov_bot import Tweet_Generator
from twython import Twython

import random
from settings.local import API_SECRET,API_KEY
import json



def get_tweet_history(screen_name):
    twt = Twython(API_KEY,API_SECRET)
    time_line = twt.get_user_timeline(screen_name = screen_name,count = 200) # at max retrieves 200 tweets
    tweets_list = [ tweet['text'] for tweet in time_line ]
    twt_gen = Tweet_Generator(tweets_list)
    next_tweets = []
    for i in xrange(5): # generates 5 tweets at a time
        next_tweets.append(twt_gen.generate_tweet(size = random.randint(5,20)))
    return next_tweets

def index(request):
    context = Context({})
    return render_to_response('index.html',context)

def get_tweets(request):
    if request.method == "GET":
        # getting the screen_name of the user from the query parameter
        screen_name = request.GET.get('screen_name','')
        # js will do the job of checking if screen name exists on twitter or not
        response = {}
        if not screen_name:
            response['errors']  = 'No username supplied'
        else:
            try:
                next_tweets = get_tweet_history(screen_name)
                response['tweets'] = next_tweets # passing a list parameter
                response['screen_name'] = screen_name
            except Exception,e: 
                print e
                response['screen_name'] = screen_name
                response['errors'] = 'Either the user has no or protected tweets or the user does not exists.'

        response_json = json.dumps(response)
        return HttpResponse(response_json,content_type='application/json')
