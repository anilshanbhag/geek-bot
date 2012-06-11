from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

import os.path
import wsgiref.handlers
import urllib2
from django.utils import simplejson as json
import tweepy

class HomeHandler(webapp.RequestHandler):
    def get(self):
        ck = "AosCywbP0ZJWDQzs6fi5XA"
        cs = "U2mMHiaRI0J5OYHULiWKEuyUcdc29c0vAlMqCIxls"

        at = "337254045-bu8ZJ1eokgD6HuLoXNb1blGC8zuOUG4K8wetlsUo"
        ats = "KdYt8JNQ4hKEpNIyolDGEyEgONPwFq60w7ZkdbRfGQ"

        auth = tweepy.OAuthHandler(ck, cs)
        auth.set_access_token(at, ats)

        api = tweepy.API(auth)

        j = json.loads( urllib2.urlopen("http://apify.heroku.com/api/hacker_news.json").read() )
        api.update_status(j[0]["title"] + " " + j[0]["url"])
        self.response.out.write("Task Done");

def main():
    util.run_wsgi_app(webapp.WSGIApplication([(r"/", HomeHandler)]))

if __name__ == "__main__":
    main()
