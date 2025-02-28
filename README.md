## Клонируйте проект

git clone (https://github.com/AlekseySuin/DjangoStripe)
cd ваш-репозиторий


## Запуск с помощью Docker

а) Убедитесь, что Docker установлен
Убедитесь, что у вас установлены Docker и Docker Compose. Если нет, установите их:

[Установка Docker](https://docs.docker.com/get-started/get-docker/)

[Установка Docker Compose](https://docs.docker.com/compose/install/)

б) Сборка и запуск контейнеров
```
docker-compose up --build
```
После завершения сборки ваш проект будет доступен по адресу:

##  Применение миграций
После запуска контейнеров примените миграции для создания базы данных:
```
docker-compose exec web python manage.py migrate
```
