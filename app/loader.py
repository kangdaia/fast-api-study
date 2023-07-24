import os
import requests
import json
import asyncio
import aiohttp
from dotenv import load_dotenv
from repository.mongo_handler import MongonHandler

# Last.fm top tracks api를 이용해 음악 데이터 요청 및 DB 적재


def param_handler(i):
    """Last.fm API 요청 파라메터 생성. page 값을 받아서 페이지 값을 넣은 json 반환

    Args:
        i (int): page number

    Returns:
        json object: url requests params object
    """
    return {
        "method": "chart.gettoptracks",
        "api_key": os.environ["MUSIC_API_KEY"],
        "format": "json",
        "page": i,
        "limit": 100
    }


async def music_fetch(session, i):
    """페이지별 url get request 후 응답 결과 db 적재

    Args:
        session (ClientSession Object): aiohttp.ClientSession()
        i (int): page number
    """
    BASE_URL = "http://ws.audioscrobbler.com/2.0/"
    db = MongonHandler()
    async with session.get(url=BASE_URL, params=param_handler(i)) as response:
        result = await response.json()
        tracks_data = result["tracks"]["track"]
        db.insert_item_many(
            tracks_data,
            db_name="fast-api-test-dk",
            collection_name="music_data"
        )


async def music_loader():
    """50페이지 데이터를 비동기적으로 호출
    """
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[music_fetch(session, i) for i in range(1, 50)])


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(music_loader())
