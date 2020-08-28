# Справочник поступления
### Репозиторий бэкэнда
### API

| Method name | Path | Description |
| ----------- | ---- | ----------- |
| POST | /user | Регистрация |
| GET | /user | Получить информацию о пользователе |
| PUT | /user/ | Изменить информацию о пользователе |
| GET | /user/programs | Получить список отслеживаемых направлений |
| GET | /recommendations | Получить список рекомендованных вузов |
| POST | /universities/ | Добавить новый вуз |
| GET | /universities/ | Получить список вузов |
| GET | /universities/<:id> | Получить информацию о вузе |
| GET | /universities/<:id> | Получить информацию о вузе |
| GET | /universities/<:id>/photos | Получить фотографии из вуза |
| PUT | /universities/<:id> | Изменить информацию о вузе |
| GET | /universities/<:id>/programs | Получить информацию об образовательных программах |
| POST | /universities/<:id>/programs | Добавить образовательную программу |
| GET | /programs/<:id> | Получить информацию о направлении |
| GET | /programs/<:id>/details | Получить подробную информацию о направлении |
| PUT | /programs/<:id> | Изменить информацию о направлении |
| GET | /programs/<:id>/similar | Получить список похожих направлений |
| GET | /programs | Получить список всех направлений |
| GET | /photos/<:id> | Получить фотографию |
| POST | /feedback | Отправить отзыв |
| GET | /search | Поиск |


### Структуры данных
#### Enrollee
Enrollee служит для хранения подробной информации о пользователе, включая информацию об избранном и результатах ЕГЭ
История
Информатика и информационно-коммуникационные технологии (ИКТ) 
Биология
География
Литература 
```
Enrollee {
    id: ID,
    firstName : String,
    lastName: String,
    egeResults: {
        total: Int,
        russian: Int,
        mathProf: Int,
        mathBase: Int,
        socialStudies: Int,
        Physics: Int,
        Chemistry: Int,
        History: Int,
        geography: Int,
        english: Int,
        german: Int,
        french: Int,
        chinese: Int,
        Spanish: Int,
        literature: Int,
    }
    chosenPrograms: [EdProgram]
}
```
#### EdProgram
EdProgram - сущность, отвечающая за хранение информации об образовательном направлении
```
EdProgram {
    code: String,
    university: Id,
    name: String,
    Enrollees : [Enrollee]
}
```
#### University
University хранит в себе информацию о вузе, а также список направлений, содержащихся в вузе
```
University {
    id: Id,
    name: String,
    programs: [EdProgram],
    about: String,
    photos: [Photo],
    site: URL,
}
```
#### Photo
Photo содержит информацию о картинке
```
University {
    url: URL,
    description: String
}
```
### Описание запросов к серверу
#### /user
#### POST - Создание нового пользователя.
Тело запроса
```
{
    firstName: String,
    lastName: String,
    egeResults: {
        russian: Int,
        mathProf: Int,
        mathBase: Int,
        socialStudies: Int,
        Physics: Int,
        Chemistry: Int,
        History: Int,
        geography: Int,
        english: Int,
        german: Int,
        french: Int,
        chinese: Int,
        Spanish: Int,
        literature: Int,
    }
}
``` 
Response
```
{
    id: ID
}
```
PUT
{
    firstName: String,
    lastName: String,
    egeResults: {
        russian: Int,
        mathProf: Int,
        mathBase: Int,
        socialStudies: Int,
        Physics: Int,
        Chemistry: Int,
        History: Int,
        geography: Int,
        english: Int,
        german: Int,
        french: Int,
        chinese: Int,
        Spanish: Int,
        literature: Int,
    }
}
``` 
Response
```
{
    id: ID
    firstName: String,
    lastName: String,
    egeResults: {
        russian: Int,
        mathProf: Int,
        mathBase: Int,
        socialStudies: Int,
        Physics: Int,
        Chemistry: Int,
        History: Int,
        geography: Int,
        english: Int,
        german: Int,
        french: Int,
        chinese: Int,
        Spanish: Int,
        literature: Int,
    },
    chosenPrograms: [EdProgram]
}
```
