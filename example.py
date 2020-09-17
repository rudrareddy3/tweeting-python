import speech_recognition as sr
import tweepy
import sys
import glob
import os

api_key = "Lor00F1mR2yYQqTFKgxuTiXed"
api_secret_key = "QK8AaRb0e1p4QfKiuXeZu7ooXpRUxFR4dDdYb4e8QlvzK3DrlB"
access_token = "1301663981157994496-vHxJ8mBaOsee6PZHMMaLzIjx7OMaUT"
access_token_secret = "LxyImrI6GMNfwsfN8KdUWkNrnGWtOAhVwLrTjCLRH2qCt"
authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
API = tweepy.API(authentication)
def make_text_tweet(text):
    #function to make a tweet using text
    API.update_status(text)

r = sr.Recognizer()
harvard = sr.AudioFile(sys.argv[1])
with harvard as source:
   audio = r.record(source)
if __name__ == "__main__":
   make_text_tweet(r.recognize_google(audio))

