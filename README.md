# Расписание для тренеров в фитнес-клубах (API)
Данный проект позволяет получить API расписания тренировок.  
Тренировки отсортированы по фитнес-клубам.  
![Screenshot](https://github.com/valhallajazzy/DRF_schedule_4_coach/blob/main/picture/scheduleAPI.png)

Так же поддерживаются CRUD-операции по объектам с соответствующими атрибутами:
* Клиент (Client)
* Тренер (Coach)
* Фитнес-клуб (SportClub)
* Тренировка (Training)

## URLs для отправки API-запроса:
`/api/coaches/` - GET/POST-запросы по получению, и добавлению объекта `Тренер`.  
`/api/coaches/<coach_id>` - PUT/PATCH/DELETE-запросы по изменению, и удалению объекта `Тренер` по id тренера.  
`/api/clients/` - GET/POST-запросы по получению, и добавлению объекта `Клиент`.  
`/api/clients/<client_id>` - PUT/PATCH/DELETE-запросы по изменению, и удалению объекта `Клиент` по id клиента.  
`/api/clubs/` - GET/POST-запросы по получению, и добавлению объекта `Фитнес-клуб`.  
`/api/clubs/<club_id>` - PUT/PATCH/DELETE-запросы по изменению, и удалению объекта `Фитнес-клуб` по id фитнес-клуба.  
`/api/trainings/` - GET/POST-запросы по получению, и добавлению объекта `Тренировка`.  
`/api/trainings/<club_id>` - DELETE-запрос по удалению объекта `Тренировка` по id тренировки.  
`/api/schedule/<coach_id>` - GET-запрос получения расписания по id тренера.  

## Подготовка и запуск проекта
* Создаем файл `.env` в корневой директории проекта и указываем переменные `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASS`, `DB_PORT`  
для подключения Django к базе данных:
![Screenshot](https://github.com/valhallajazzy/DRF_schedule_4_coach/blob/main/picture/schedule_env.png)
* Запускаем приложение, с БД и PG-admin командой в docker-compose:
```console
$ docker-compose up -d
```
