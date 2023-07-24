from app.repository.mongo_handler import MongonHandler


def get_musics(page: int = 1, limit: int = 30, query: str = None):
    db = MongonHandler()
    cursor = db.find_item(
        query, db_name="fast-api-test-dk", collection_name="music_data"
    ).sort("playcount", -1)
    data = list(cursor.skip((page - 1) * limit))[: page * limit]
    db.end_client()
    return data


def get_music_search(name: str, artist: str):
    db = MongonHandler()
    cursor = db.find_item(
        condition={
            "$or": [
                {"name": name if name else artist},
                {"artist.name": artist if artist else name},
            ]
        },
        db_name="fast-api-test-dk",
        collection_name="music_data",
    )
    data = list(cursor)
    db.end_client()
    return data
