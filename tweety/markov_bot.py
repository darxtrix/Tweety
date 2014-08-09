import random,re
from collections import defaultdict # using a defultdict will not throw KeyError

class Tweet_Generator:
    def __init__(self,tweets_list):
        '''
            Markov bot based on bigram probabilities.
            Generates a tweet on user's tweet history.
        '''
        self.chain_length = 2 # markov chain length
        self.words_list = self.clean_data(tweets_list) # clean the data using regex
        self.words_length = len(self.words_list) # by this way we call length only once
        self.tokens = defaultdict(list) # using list constructor  ( w1, w2 ) --> [..]
        self.structurise() # flood the self.tokens field

    def clean_data(self,tweets_list):
        ''' 
            Cleans the list of user 
            statuses by using regex
        '''
        ignorables = re.compile(r'http|[@#][a-zA-Z0-9_]+|RT|MT') # making a compiles regex object
        #ankush,@bower123,http://mysite.com --> ignore these set of words
        words = [] # a list of w1,w2,w3,w4 ...
        for tweet in tweets_list:
            for word in tweet.split(): # for every word in a tweet
                if not ignorables.search(word):
                    words.append(word.lower()) # making a list of words in user's tweets
        return words

    def structurise(self):
        '''
            Converts the list of words to the following format
            [ ( w1,w2 ) --> [ w3,w4, ..] ] and store them in tokens
        '''
        # if the message is any shorter, it won't lead anywhere
        if self.words_length > self.chain_length:
            for ctr in range(self.words_length-self.chain_length):
                key = self.words_list[ctr],self.words_list[ctr+1]
                self.tokens[key].append(self.words_list[ctr+2]) # appends the next word to current dict
                # if there exist no dict,it would create one

    def generate_tweet(self,size = 5):
        '''
            Generates a tweet of a given size
        '''
        # we should give an initial seed for preicting w1
        #print self.tokens
        seed = random.randint(0,self.words_length - self.chain_length - 1)
        tweet = []
        w1,w2 = self.words_list[seed],self.words_list[seed+1]
        for ctr in xrange(size):
            tweet.append(w1)
            key = (w1,w2)
            if self.tokens[key] == []: # w3 not found
                break
            else:
                w1,w2 = w2,random.choice(self.tokens[key]) # uses a random element from the list
        tweet.append(w2) # when break occurs do append w2
        return " ".join(tweet) # concat the list items



