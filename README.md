## Степень реализации проекта:
:white_check_mark: Запуск используя Docker </br>
:white_check_mark: Использование environment variables </br>
:white_check_mark: Просмотр Django Моделей в Django Admin панели </br>
:white_check_mark: Запуск приложения на удаленном сервере, доступном для тестирования, с кредами от админки </br>
:white_check_mark: Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items </br>
:white_check_mark: Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.  </br>
:white_check_mark: Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте </br>
:white_check_mark: Реализовать не Stripe Session, а Stripe Payment Intent. </br>
> Оставил Stripe Session на покупку Item для наглядности

## Немного пояснений по endpoints:
/orders/ - список всех заказов (также реализовал преобразование валюты, если при создании заказа указаны RUB - конвертируется в рубли) </br>
/orders/{id} - конкретный заказ (также учтены налоги и скидки) </br>
/orders/{id}/checkout/ - покупка заказа  </br>
/items/ - список всех товаров </br>
/items/{id}/ - конкретный товар </br>
/buy/{id}/ - покупка товара </br>

## Проект можно посмотреть онлайн на платформе Render
```
https://djangostripe-h8yh.onrender.com/items/2/
```
Либо же оффлайн, для этого ниже написаны этапы для запуска

## 1. Клонируйте проект

git clone (https://github.com/AlekseySuin/DjangoStripe)
cd ваш-репозиторий


## 2. Запуск с помощью Docker

а) Убедитесь, что Docker установлен
Убедитесь, что у вас установлены Docker и Docker Compose. Если нет, установите их:

[Установка Docker](https://docs.docker.com/get-started/get-docker/)

[Установка Docker Compose](https://docs.docker.com/compose/install/)

б) Сборка и запуск контейнеров
```
docker-compose up --build
```
После завершения сборки ваш проект будет доступен по адресу:
```
http://localhost:8000/
```
##  3. Применение миграций
После запуска контейнеров примените миграции для создания базы данных:
```
docker-compose exec web python manage.py migrate
```
### 4. Использование проекта

1) Создание товара (Item)
  a) Перейти в админ панель
```
  http://localhost:8000/admin/
```
  б) Войдите с учетными данными суперпользователя.
2) Создание заказа (Order)
  По аналогии с товаром

3) Endpoints:
   Описаны выше во вкладке `пояснения про Endpoints`

## Для проверки работоспособности Stripe Payment Intent используйте данные из этого источника
`https://docs.stripe.com/testing?testing-method=card-numbers#visa`
