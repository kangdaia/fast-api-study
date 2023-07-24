# Fast API Application

## Structure

```
fast-api-study
├── app\
│   ├── auth\
│   │   ├── users_crud.py
│   │   ├── users_model.py
│   │   ├── users_router.py
|   ├── musics\
│   │   ├── musics_crud.py
│   │   ├── musics_model.py
│   │   ├── musics_router.py
│   ├── repository\
│   │   ├── mongo_handler.py
│   │   ├── main.py
├── front-ui\
├── tests\
│   ├── test_async_main.py
├── entrypoint.py
```

## To run

- pipenv shell
- python3 entrypoint.py

for test:
- pytest
