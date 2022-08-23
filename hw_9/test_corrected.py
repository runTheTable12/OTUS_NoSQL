import json
import redis
import datetime

with open ('reddit_jokes.json') as f:
    data = json.load(f)

r = redis.Redis ('localhost')

pipeline = r.pipeline()

print("*** запись JSON как строки")
print(datetime.datetime.now())
pipeline.set("string_test", json.dumps(data))
print(datetime.datetime.now())

print("*** чтение JSON как строки")
result = ""
print(datetime.datetime.now())
pipeline.get("string_test")
print(datetime.datetime.now())

print("-----------------------")
print("*** запись JSON как hset")
print(datetime.datetime.now())
counter = 0
for chunk in data:
    pipeline.hset('hset_test', counter, json.dumps(chunk))
    counter += 1
print(datetime.datetime.now())

print("*** чтение JSON как hset")
print(datetime.datetime.now())
s = pipeline.hgetall('hset_test')
print(datetime.datetime.now())
print("-----------------------")

print("-----------------------")
print("*** запись JSON как zset")
print(datetime.datetime.now())
counter = 0
for chunk in data:
    pipeline.zadd('zset_test', {json.dumps(chunk):counter})
    counter +=1
print(datetime.datetime.now())

print("*** чтение JSON как zset")
print(datetime.datetime.now())
s = pipeline.zrange('zset_test', 0, -1)
print(datetime.datetime.now())
print("-----------------------")

print("-----------------------")
print("*** запись JSON как list")
print(datetime.datetime.now())
for chunk in data:
    r.rpush('list_test', json.dumps(chunk))
print(datetime.datetime.now())

print("*** чтение JSON как list")
print(datetime.datetime.now())
s = pipeline.lrange('list_test', 0, -1)
print(datetime.datetime.now())
print("-----------------------")

pipeline.execute()