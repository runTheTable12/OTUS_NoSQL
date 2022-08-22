import json
import redis
import datetime

with open ('reddit_jokes.json') as f:
    data = json.load(f)

r = redis.Redis ('localhost')


print("*** запись JSON как строки")
print(datetime.datetime.now())
r.set("string_test", json.dumps(data))
print(datetime.datetime.now())

print("*** чтение JSON как строки")
result = ""
print(datetime.datetime.now())
for key in r.scan_iter():
    result += str(key)
print(datetime.datetime.now())

print("-----------------------")
print("*** запись JSON как hset")
print(datetime.datetime.now())
counter = 0
for chunk in data:
    r.hset('hset_test', counter, json.dumps(chunk))
    counter += 1
print(datetime.datetime.now())

print("*** чтение JSON как hset")
print(datetime.datetime.now())
s = r.hgetall('hset_test')
print(datetime.datetime.now())
print("-----------------------")

print("-----------------------")
print("*** запись JSON как zset")
print(datetime.datetime.now())
counter = 0
for chunk in data:
    r.zadd('zset_test', {json.dumps(chunk):counter})
    counter +=1
print(datetime.datetime.now())

print("*** чтение JSON как zset")
print(datetime.datetime.now())
s = r.zrange('zset_test', 0, -1)
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
s = r.lrange('list_test', 0, -1)
print(datetime.datetime.now())
print("-----------------------")