import os
from dotenv import load_dotenv

import tweepy

import time
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(consumer_key=API_KEY,
                       consumer_secret=API_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET)

sentences = [
    "That's what she said!",
    "I declare bankruptcy!",
    "I'm an idea man. I thrive on enthusiasm.",
    "I'm not a hero. I'm a high-functioning moron.",
    "I'm not just the best boss. I am the best boss.",
    "I'm not superstitious, but I am a little stitious.",
    "I talk a lot, so I've learned to just tune myself out.",
    "I'm running away from my responsibilities, and it feels good.",
    "I'm an early bird and I'm a night owl, so I'm wise and I have worms.",
    "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.",
    "Sometimes I'll start a sentence and I don't even know where it's going. I just hope I find it along the way.", 
    "Sometimes you have to take a break from being the kind of boss that's always trying to teach people things. Sometimes you just have to be the boss of dancing.",
    "Wikipedia is the best thing ever. Anyone in the world can write anything they want about any subject. So you know you are getting the best possible information.",
    "Do I need to be liked? Absolutely not. I like to be liked. I enjoy being liked. I have to be liked, but it's not like this compulsive need to be liked, like my need to be praised.",
]

def generate_tweet(sentences, days):
    tweet = f"Faltam {days} dias para a minha viagem à Alemanha!!!\n\n\"{sentences}\" - Michael Scott"
    return tweet

def one_day_tweet(sentences, days):
    tweet = f"Falta {days} dia para a minha viagem à Alemanha!!!\n\n\"{sentences}\" - Michael Scott"
    return tweet

def last_tweet(sentences):
    tweet = f"É hoje a minha viagem para a Alemanha!!!\n\n\"{sentences}\" - Michael Scott"
    return tweet

def countdown():
    travel_date = datetime(2023, 6, 26, 9, 55)
    current_date = datetime.now()

    delta = travel_date - current_date

    if delta.days < 0:
        return False

    days = delta.days

    return days

def send_tweets():
    days = countdown()

    if days < 0:
        return False

    elif days == 0:
        tweet = last_tweet(sentences[days])
        response = client.create_tweet(text=tweet)
        print(response)
    
    elif days == 1:
        tweet = one_day_tweet(sentences[days], days)
        response = client.create_tweet(text=tweet)
        print(response)

    else:
        tweet = generate_tweet(sentences[days], days)
        response = client.create_tweet(text=tweet)
        print(response)

send_tweets()