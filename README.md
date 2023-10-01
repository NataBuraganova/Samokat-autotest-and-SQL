## Тест на проверку, что по треку заказа можно получить данные о заказе в Яндекс самокат.
____
**- Для запуска тестов должны быть установлены пакеты pytest и requests**  
**- Запуск всех тестов выполянется командой pytest**
___
# Запросы SQL:
### Запрос 1:
SELECT  cou.login AS couriers,  
COUNT(*) AS "number orders in delivery"  
FROM "Couriers" AS cou  
RIGHT OUTER JOIN "Orders" AS ord ON ord."courierId"=cou.id  
WHERE  ord."inDelivery" = true  
GROUP BY cou.login;  

### Запрос 2:
SELECT track AS track,  
CASE   
WHEN finished = true THEN '2'  
WHEN cancelled = true THEN '-1'  
WHEN "inDelivery" = true THEN '1'  
ELSE '0'  
END AS status  
FROM "Orders";  
