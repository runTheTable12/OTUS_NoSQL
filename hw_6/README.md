# Домашняя работа №6: ElasticSearch

* Так как нет возможности развернуть ES в AWS, то я подниму базу в доккере.

Позаимствую docker-compose файл из [этой](https://levelup.gitconnected.com/docker-compose-made-easy-with-elasticsearch-and-kibana-4cb4110a80dd) статьи.

Поднимем [контейнеры](/docker-compose.yml) с ES и Kibana командой `docker-compose up -d`
![](pics/Screen%20Shot%202022-08-18%20at%2012.03.19%20pm.png)
Теперь создадим индекс curl запросом, добавив в него паттерн.

```
curl -X PUT "localhost:9200/otus-hw?pretty" -H 'Content-Type: application/json' -d'
{
  "settings": {
    "analysis": {
      "filter": {
        "ru_stop": {
          "type": "stop",
          "stopwords": "_russian_"
        },
        "ru_stem": {
          "type": "stemmer",
          "language": "russian"
        }
      },
      "analyzer": {
        "mommy": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [ "lowercase", "ru_stop", "ru_stem" ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "mommy_field": {
        "type": "text",
        "analyzer": "mommy"
      }
    }
  }
}
'
```
![](pics/Screen%20Shot%202022-08-18%20at%2012.21.30%20pm.png)
Индекс создался. Теперь добавим в него данные.

```
curl -X POST "localhost:9200/otus-hw/_bulk?pretty" -H 'Content-Type: application/json' -d'
{ "create" : { "_id" : "1" } }
{ "mommy_field" : "моя мама мыла посуду а кот жевал сосиски" }
{ "create" : { "_id" : "2" } }
{ "mommy_field" : "рама была отмыта и вылизана котом" }
{ "create" : { "_id" : "3" } }
{ "mommy_field" : "мама мыла раму" }
'
```
![](pics/Screen%20Shot%202022-08-18%20at%201.17.48%20pm.png)
Сделаем поисковый запрос

```
curl -X POST "localhost:9200/otus-hw/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match": {
      "mommy_field": {
        "query": "мама ела сосиски",
        "fuzziness": "auto"
      }
    }
  }
}
'
```
Результат запроса доступен [здесь](response.json).
