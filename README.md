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
   Описаны в файле `items.urls` 
