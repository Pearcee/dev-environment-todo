from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection
import redis

r = redis.Redis(host="redis", port=6379)

redis = get_redis_connection(
    host="localhost",
    port=6379,
    decode_responses=True
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get("/")
def read_root():
    return {"Hello": "World!"}

@app.get("/hits")
def read_root():
    r.set("foo", "bar")
    r.incr("hits")
    return {"Number of hits:": r.get("hits"), "foo": r.get("foo")}

