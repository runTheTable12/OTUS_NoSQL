## Домашняя работа №14: Tarantool

К сожалению, сейчас ограничен в ресурсах, поэтому не стал экспеременитровать с vshard и запустил tarantool через доккер, следуя инструкциям на оффициальном сайте

```
docker pull tarantool/tarantool
docker run -it --rm tarantool/tarantool
```

Создам спэйс для практики - balance.

```
balance = box.schema.space.create('balance', {if_not_exists=true});
```

Теперь создадам атрибуты.

```
balance:format({
	{name = 'userID', type = 'string'},
	{name = 'amount', type = 'double'},
	{name = 'status', type = 'string'}
});
balance:create_index(
	'primary', {type = 'hash', parts = {'userID'}}
	);
```

Теперь создадам функцию добавления денег на счёт.

```
function add_money (userID, amount)
	row = box.space.balance:select{userID}
    if (row[1] == nil) then
        if (amount > 0) then
            box.space.balance:insert({userID, amount, 'active'})
        else
            box.space.balance:insert({userID, amount, 'not_active'})
        end
    else
        if (row[1][2] + amount > 0) then
            box.space.balance:update(userID, {{'+', 2, amount}, {'=', 3, 'active'}})
        else
            box.space.balance:update(userID, {{'+', 2, amount}, {'=', 3, 'not_active'}})
        end
    end    
end
```

При вставке наткнулся на ошибку с типом данных. Погуглил и нашёл решение, как кастовать.

Вставляем данные
```
ffi = require('ffi')
add_money("John", ffi.cast('double', 100))
add_money("Mark", ffi.cast('double', 599))
add_money("Vova", ffi.cast('double', 27))
```
Посмотрим, есть ли данные в таблице.
![](pics/Screen%20Shot%202022-08-26%20at%208.58.07%20pm.png)

Подключим библиотеку

```
expirationd = require('expirationd')
```
Теперь создам функцию проверки отрицательного баланса.

```
function balance_check(args, tuple)

    rows = box.space.balance:select{}

    new_sum = tuple[2] - rows[1][2]
    new_status = 'active'
    
    if (tuple[3] == 'not_active') then  
        return false
    end
    
    if (new_sum <= 0) then
        new_status = 'not_active'
    end
    
    box.space.balance:update(tuple[1], {{'-', 2, rows[1][2]}, {'=', 3, new_status}})
    
    if new_status == 'not_active' then 
		require('http.client').new():request('GET', 'http://127.0.0.1', nil, {tuple[1]}) 
	end
    
    return false

end
```

Запущу функцию

```
expirationd.run_task('balance', balance.id, balance_check)
```
![](pics/Screen%20Shot%202022-08-26%20at%209.00.22%20pm.png)