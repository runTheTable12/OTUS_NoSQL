## Домашняя работа №10: DCS

Для того, чтобы развернуть БД, буду [docker-compose](docker-compose.yaml) с образами bitnami.

Несколько раз потестил БД с разным количеством ключей.

Полные вывод трёх тестов находятся в репозитории. 

Каждый раз тест завершался с одной из двух ошибок.

```
Error querying Consul agent: Unexpected response code: 500 (rpc error getting client: failed to get conn: dial tcp <nil>->172.31.0.2:8300: i/o timeout)
```

```
Error querying Consul agent: Unexpected response code: 500 (No cluster leader)
```

Особенно интересна ошибка `no cluster leader` - ради интереса поресёрчил её, и чётное количество нод, несмотря на количество, действительно может привести к ней. В теории, одна упавшая нода может уронить весь кластер. 

