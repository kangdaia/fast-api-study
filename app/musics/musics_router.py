from fastapi import APIRouter
from app.musics import musics_crud

"""
/music -> get all music by pagenation
param:
    page: pagenationx
    query: find
    limit: page data limit set=30
-> return the musics fit to cond
"""

router = APIRouter()


# 페이지 쿼리 가능한 track list. playcount 내림차순으로 정렬
@router.get("/list", tags=["music"], description="show all musics data")
def get_musics_all(page: int = 1, limit: int = 30, query: str = None):
    data = musics_crud.get_musics(page=page, limit=limit, query=query)
    return {"tracks": data, "page": page, "limit": limit}


# 음악 제목과 가수이름으로 음악 트랙 조회
@router.get(
    "/search", tags=["music"], description="get musics by music title and artist name"
)
def get_music_by_id(name: str = None, artist: str = None):
    if not name and not artist:
        return {"track": []}
    data = musics_crud.get_music_search(name, artist)
    return {"track": data}
