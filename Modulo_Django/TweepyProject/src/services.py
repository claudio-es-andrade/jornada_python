import tweepy
from typing import List, Dict, Any

from src.connection import trends_collection
from src.constants import BRAZIL_WOE_ID
from src.secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
"""
    Get Treding Topics
    :param woe_id: Identifier of Location
    :return: List[Dict[str, Any]]: Trends list
"""
def _get_trends(woe_id: int, api: tweepy.API) -> List[Dict[str, Any]]:

    breakpoint()
    trends = api.get_place_trends(woe_id)    # for tweet in trends:  #     print(tweet)
    return trends[0]['trends']   #[trend for trend in trends]

def get_trends_from_mongo()-> List[Dict[str, Any]]:
    trends = trends_collection.find({})
    return list(trends)

def save_trends() -> None:
    auth = tweepy.OAuthHandler(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    trends = _get_trends(woe_id=BRAZIL_WOE_ID, api=api)
    trends_collection.insert_many(trends)
