from bson.objectid import ObjectId as BsonObjectId
from pydantic import BaseModel


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError("ObjectId required")
        return str(v)


class Artist(BaseModel):
    name: str
    mbid: str
    url: str


class Streamable(BaseModel):
    text: str
    fulltrack: str


class Music(BaseModel):
    _id: PydanticObjectId
    name: str
    duration: str
    playcount: str
    listeners: str
    mbid: str
    url: str
    streamable: Streamable
    artist: Artist
    image: list[object]

    class Config:
        orm_mode = True
