import tweepy
import uvicorn

from fastapi import FastAPI
from typing import List

from src.responses import TrendItem
from src.services import get_trends_from_mysql , save_trends


app = FastAPI()

@app.get("/trends" , response_model=List[TrendItem])
def get_trends_route():
    return get_trends_from_mysql()      #list(trends)    #[0]['trends']    #{"Hello": "World"}

if __name__ == "__main__":

    trends = get_trends_route()

    if not trends:
        save_trends()

    uvicorn.run(app, host="0.0.0.0", port=8000)
