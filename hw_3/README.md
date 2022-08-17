
### Создадим репликасет с тремя нодами

Для домашнего задания я буду использовать одну виртуальную машину `Yandex.Cloud`.


Будет использована MongoDB `четвёртой` версии:

```
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add - && echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list && sudo apt-get update && sudo apt-get install -y mongodb-org
```

### Создадим репликасет

```
sudo mkdir /home/mongo && sudo mkdir /home/mongo/{db1,db2,db3,db4} && sudo chmod 777 /home/mongo/{db1,db2,db3,db4}
mongod --dbpath /home/mongo/db1 --port 27001 --replSet RS --fork --logpath /home/mongo/db1/db1.log --pidfilepath /home/mongo/db1/db1.pid
mongod --dbpath /home/mongo/db2 --port 27002 --replSet RS --fork --logpath /home/mongo/db2/db2.log --pidfilepath /home/mongo/db2/db2.pid
mongod --dbpath /home/mongo/db3 --port 27003 --replSet RS --fork --logpath /home/mongo/db3/db3.log --pidfilepath /home/mongo/db3/db3.pid
```

Все инстансы успешно запущены.

### Проинициализируем кластер

```
rs.initiate({"_id" : "RS", members : [{"_id" : 0, priority : 3, host : "127.0.0.1:27001"},
{"_id" : 1, host : "127.0.0.1:27002"},
{"_id" : 2, host : "127.0.0.1:27003", arbiterOnly : true}]});
```

### Теперь поубиваем ноды

При убийстве одной ноды оказалось невозможным подключиться к ней.
Вторая и третья работают нормально.

### Теперь создадим шардированный кластер на новой виртуальной машине

```
sudo mkdir /home/mongo && sudo mkdir /home/mongo/{dbc1,dbc2,dbc3} && sudo chmod 777 /home/mongo/{dbc1,dbc2,dbc3}
mongod --configsvr --dbpath /home/mongo/dbc1 --port 27001 --replSet RScfg --fork --logpath /home/mongo/dbc1/dbc1.log --pidfilepath /home/mongo/dbc1/dbc1.pid
mongod --configsvr --dbpath /home/mongo/dbc2 --port 27002 --replSet RScfg --fork --logpath /home/mongo/dbc2/dbc2.log --pidfilepath /home/mongo/dbc2/dbc2.pid
mongod --configsvr --dbpath /home/mongo/dbc3 --port 27003 --replSet RScfg --fork --logpath /home/mongo/dbc3/dbc3.log --pidfilepath /home/mongo/dbc3/dbc3.pid

rs.initiate({"_id" : "RScfg", configsvr: true, members : [{"_id" : 0, priority : 3, host : "127.0.0.1:27001"},{"_id" : 1, host : "127.0.0.1:27002"},{"_id" : 2, host : "127.0.0.1:27003"}]});

sudo sudo mkdir /home/mongo/{db1,db2,db3,db4,db5,db6} && sudo chmod 777 /home/mongo/{db1,db2,db3,db4,db5,db6}
mongod --shardsvr --dbpath /home/mongo/db1 --port 27011 --replSet RS1 --fork --logpath /home/mongo/db1/db1.log --pidfilepath /home/mongo/db1/db1.pid
mongod --shardsvr --dbpath /home/mongo/db2 --port 27012 --replSet RS1 --fork --logpath /home/mongo/db2/db2.log --pidfilepath /home/mongo/db2/db2.pid
mongod --shardsvr --dbpath /home/mongo/db3 --port 27013 --replSet RS1 --fork --logpath /home/mongo/db3/db3.log --pidfilepath /home/mongo/db3/db3.pid
mongod --shardsvr --dbpath /home/mongo/db4 --port 27021 --replSet RS2 --fork --logpath /home/mongo/db4/db4.log --pidfilepath /home/mongo/db4/db4.pid
mongod --shardsvr --dbpath /home/mongo/db5 --port 27022 --replSet RS2 --fork --logpath /home/mongo/db5/db5.log --pidfilepath /home/mongo/db5/db5.pid
mongod --shardsvr --dbpath /home/mongo/db6 --port 27023 --replSet RS2 --fork --logpath /home/mongo/db6/db6.log --pidfilepath /home/mongo/db6/db6.pid

mongo --port 27011
rs.initiate({"_id" : "RS1", members : [{"_id" : 0, priority : 3, host : "127.0.0.1:27011"},{"_id" : 1, host : "127.0.0.1:27012"},{"_id" : 2, host : "127.0.0.1:27013", arbiterOnly : true}]});

mongo --port 27021
rs.initiate({"_id" : "RS2", members : [{"_id" : 0, priority : 3, host : "127.0.0.1:27021"},{"_id" : 1, host : "127.0.0.1:27022"},{"_id" : 2, host : "127.0.0.1:27023", arbiterOnly : true}]});
```

### Запускаем шардированный кластер в двух экземплярах для отказоустойчивости

```
mongos --configdb RScfg/127.0.0.1:27001,127.0.0.1:27002,127.0.0.1:27003 --port 27000 --fork --logpath /home/mongo/dbc1/dbs.log --pidfilepath /home/mongo/dbc1/dbs.pid 
mongos --configdb RScfg/127.0.0.1:27001,127.0.0.1:27002,127.0.0.1:27003 --port 27100 --fork --logpath /home/mongo/dbc1/dbs2.log --pidfilepath /home/mongo/dbc1/dbs2.pid 
```

### Нагенерим данные

```
use bank
sh.enableSharding("bank")
use config
db.settings.save({ _id:"chunksize", value: 1})
use bank
for (var i=0; i<100000; i++) { db.tickets.insert({name: "Max ammout of cost tickets", amount: Math.random()*100}) }
db.tickets.createIndex({amount: 1})
db.tickets.stats()
sh.shardCollection("bank.tickets",{amount: 1})
use admin
db.runCommand({shardCollection: "bank.tickets", key: {amount: 1}})
> sh.status()
```

### Создадим индекс и сделаем шардирование по нему

sh.balancerCollectionStatus("bank.tickets")
sh.splitFind( "bank.tickets", { "amount": "50" } )

### Пороняем инстансы

Вот, что удалось увидеть:

При отключении одного шарда стал давать ошибку, нельзя сделать find для коллекции.
Однако запросы со второго шарда проходят успешно. 
При выключении ноды из кластера конфигов, не являющейся мастером, то при запросе состояния rs.status() будет информация о том, что с нодой потеряна связь. Если ноду опять поднять, то эта информация пропадёт. Если отключить мастер-ноду, то мастером станет другая нода.

### Настройка аутентификации и многоролевого доступа

```
sudo mkdir /home/mongo/db15 && sudo chmod 777 /home/mongo/db15
mongod --dbpath /home/mongo/db15 --port 27005 --fork --logpath /home/mongo/db15/db5.log --pidfilepath /home/mongo/db15/db5.pid

mongo --port 27005
db = db.getSiblingDB("admin")
db.createRole(
    {      
     role: "superRoot",      
     privileges:[
        { resource: {anyResource:true}, actions: ["anyAction"]}
     ],      
     roles:[] 
    }
)

db.createUser({      
     user: "companyDBA",      
     pwd: "EWqeeFpUt9*8zq",      
     roles: ["superRoot"] 
})
```
запускаем сервер с аутентификацией

```
mongod --dbpath /home/mongo/db15 --port 27005 --auth --fork --logpath /home/mongo/db15/db5.log --pidfilepath /home/mongo/db15/db5.pid
```