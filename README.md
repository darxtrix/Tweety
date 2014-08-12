Tweety
------

A **Markov Bot** based on bigram probabilities to generate a random tweet based on your tweet history. A markov chain is formed by randomly seeding from your tweet history. It's fun !!

Built Using
-----------

- Django 1.6.5
- Twpython 3.1.2

Usage
-----

	
    		$ virtualenv tweety-app
    		$ cd tweety-app/
    		$ source bin/activate
    		$ pip install -r requirements.txt
    		$ foreman start


**Note**

- Get your `app_key` and `app_secret` from [Twitter Dev Center](https://dev.twitter.com/apps/new) and django app 
  `secret_key` from settings.
- Create `API_KEY`, `API_SECRET` and `SECRET_KEY` environment variables.
- Install   `heroku-toolbelt` or seperately install `foreman`.




