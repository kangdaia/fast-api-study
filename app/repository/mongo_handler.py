from pymongo import MongoClient
from pymongo.cursor import CursorType
import os


class MongonHandler:
    def __init__(self):
        host = os.environ['MONGO_HOST']
        port = os.environ['MONGO_PORT']
        user = os.environ['MONGO_USER']
        password = os.environ['MONGO_PW']
        mongo_str = "mongodb://" + user + ":" + password + "@" + host + ":" + port
        self.client = MongoClient(mongo_str)

    def end_client(self):
        self.client.close()

    def insert_item_one(self, data, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].insert_one(data).inserted_id
        return result

    def insert_item_many(self, datas, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].insert_many(datas).inserted_ids
        return result

    def find_item_one(self, condition=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].find_one(
            condition, {"_id": False}
        )
        return result

    def find_item(self, condition=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].find(
            condition,
            {"_id": False},
            no_cursor_timeout=True,
            cursor_type=CursorType.EXHAUST,
        )
        return result

    def delete_item_one(self, condition=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].delete_one(condition)
        return result

    def delete_item_many(self, condition=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].delete_many(condition)
        return result

    def update_item_one(
        self, condition=None, update_value=None, db_name=None, collection_name=None
    ):
        result = self.client[db_name][collection_name].update_one(
            filter=condition, update=update_value
        )
        return result

    def update_item_many(
        self, condition=None, update_value=None, db_name=None, collection_name=None
    ):
        result = self.client[db_name][collection_name].update_many(
            filter=condition, update=update_value
        )
        return result

    def text_search(self, text=None, db_name=None, collection_name=None):
        result = self.client[db_name][collection_name].find(
            {"$text": {"$search": text}}
        )
        return result