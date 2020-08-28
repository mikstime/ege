# Справочник поступления
### Репозиторий бэкэнда
### API

| Method name | Path | Description |
| ----------- | ---- | ----------- |
| POST | /user | Регистрация |
| GET | /user | Получить информацию о пользователе |
| PUT | /user | Изменить информацию о пользователе |
| GET | /user/programs | Получить список отслеживаемых направлений |
| GET | /recommendations | Получить список рекомендованных вузов |
| POST | /universities | Добавить новый вуз |
| GET | /universities | Получить список вузов |
| GET | /universities/<:id> | Получить информацию о вузе |
| GET | /universities/<:id>/photos | Получить фотографии из вуза |
| GET | /universities/<:id>/programs | Получить информацию об образовательных программах |
| PUT | /universities/<:id> | Изменить информацию о вузе |
| POST | /universities/<:id>/programs | Добавить образовательную программу |
| GET | /programs/<:id> | Получить информацию о направлении |
| GET | /programs/<:id>/enrollees | Получить список поступающих |
| PUT | /programs/<:id> | Изменить информацию о направлении |
| GET | /programs/<:id>/similar | Получить список похожих направлений |
| GET | /programs | Получить список всех направлений |
| GET | /photos/<:id> | Получить фотографию |
| POST | /feedback | Отправить отзыв |
| GET | /feedback | Просмотреть список обращений |
| POST | /feedback/<:id> | Посмотреть информацию об обращении |
| GET | /search | Поиск |


### Структуры данных
#### Enrollee
Enrollee служит для хранения подробной информации о пользователе, включая информацию об избранном и результатах ЕГЭ
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
        biology: Int,
        informatics: Int,
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
    id: ID,
    code: String,
    university: ID,
    universityName: String,
    name: String,
    Enrollees : [Enrollee],
    preview : Photo
}
```
#### University
University хранит в себе информацию о вузе, а также список направлений, содержащихся в вузе
```
University {
    id: ID,
    name: String,
    programs: [EdProgram],
    about: String,
    photos: [Photo],
    site: URL,
    preview : Photo,
}
```
#### Photo
Photo содержит информацию о картинке
```
Photo {
    id: ID,
    url: URL,
    description: String
}
```
#### Feedback
Feedback содержит информацию об отзыве
```
Feedback {
    id: ID,
    status: String,
    author: ID,
    email: EMAIL,
    message: String,
}
```
### Описание запросов к серверу
#### POST /user
Создание нового пользователя.
Тело запроса
```
{
    firstName: String,
    lastName: String,
    egeResults: {
        russian: Int,
        mathProf: Int,
        mathBase: Int,
        biology: Int,
        informatics: Int,
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
#### PUT /user
Изменение уже существующего пользователя
```
{
    firstName: String,
    lastName: String,
    egeResults: {
        russian: Int,
        mathProf: Int,
        mathBase: Int,
        biology: Int,
        informatics: Int,
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
    id: ID,
    firstName: String,
    lastName: String,
    egeResults: {
        russian: Int,
        mathProf: Int,
        mathBase: Int,
        biology: Int,
        informatics: Int,
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
#### GET /user
Получение информации о пользователе

Response
```
{
    id: ID,
    firstName: String,
    lastName: String,
    egeResults: {
        russian: Int,
        mathProf: Int,
        mathBase: Int,
        biology: Int,
        informatics: Int,
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
#### GET /user/programs
Получение списка отслеживаемых направлений

Response
```
[
    {
        id: ID,
        code: String,
        university: ID,
        universityName: String,
        name: String,
        preview : Photo
    }
]
```
#### GET /recommendations
Получение списка рекомендованных пользователю вузов

Response
```
[
    {
        id: ID,
        name: String,
        about: String,
        photos: [Photo],
        site: URL,
        preview : Photo
    }
]
```
#### POST /universities
Создать новый университет. Доступно только модератору.
```
{
    name: String,
    about: String,
    photos: [Photo],
    site: URL,
    preview : Photo,
}
```
Response
```
{
    id: ID,
    name: String,
    about: String,
    photos: [Photo],
    site: URL,
    preview : Photo,
}
```
#### GET /universities
Получить список существующих вузов

Response
```
[
    {
        id: ID,
        name: String,
        about: String,
        site: URL,
        preview : Photo,
    }
]
```
#### GET /universities/<:id>
Получить информацию о существующем вузе по id.
```
{
    id: ID,
    name: String,
    about: String,
    site: URL,
    preview : Photo,
}
```
#### GET /universities/<:id>/photos
Получить список фото из вуза

Response
```
[
    {
        id: ID,
        url: URL,
        description: String
    }
]
```
#### GET /universities/<:id>/programs
Получить список направлений в вузе

Response
```
[
    {
        id: ID,
        code: String,
        university: ID,
        universityName: String,
        name: String,
        preview : Photo
    }
]
```
#### PUT /universities/<:id>
Изменение информации о вузе
```
{
    name: String,
    about: String,
    site: URL,
    preview : Photo,
}
```
Response
```
{
    id: ID,
    name: String,
    about: String,
    site: URL,
    preview : Photo,
}
```
#### POST /universities/<:id>/programs
```
{
    code: String,
    university: ID,
    name: String,
    preview : Photo
}
```
Response
```
{
    id: ID,
    code: String,
    university: ID,
    universityName: String,
    name: String,
    preview : Photo
}
```
#### GET /programs/<:id>
Полочение подробной информации о направлении

Response
```
{
    id: ID,
    code: String,
    university: ID,
    universityName: String,
    name: String,
    preview : Photo
}
```
#### GET /programs/<:id>/enrollees
Получить список поступающих на направление людей

Response
```
[
    {
        id: ID,
        firstName : String,
        lastName: String,
        egeResults: {
            total: Int,
        }
    }
]
```
#### GET /programs/<:id>/similar
Получить список направлений, похожих на данное

Response
```
[
    {
        id: ID,
        code: String,
        university: ID,
        universityName: String,
        name: String,
        preview : Photo
    }
]
```

#### GET /programs
Получить список всех направлений

Response
```
[
    {
        id: ID,
        code: String,
        university: ID,
        universityName: String,
        name: String,
        preview : Photo
    }
]
```
#### GET /photos/<:id>
Получить информацию о фото

Response
```
{
    id: ID,
    url: URL,
    description: String
}
```
#### POST /feedback
Отправить отзыв о работе
```
{
    author: ID,
    email: EMAIL,
    message: String,
}
```
Response
```
{
    id: ID,
    status: String,
    author: ID,
    email: EMAIL,
    message: String,
}
```
#### GET /feedback
Получить список обращений

Response
```
[
    {
        id: ID,
        status: String,
        author: ID,
        email: EMAIL,
        message: String,
    }
]
```
#### GET /feedback/<:id>
Получить информацию об обращении

Response
```
{{
    id: ID,
    status: String,
    author: ID,
    email: EMAIL,
    message: String,
}}
```
#### GET /search
Осуществить поиск по вузам, фото и направлениям
Response
```
{
    photos: [Photo],
    universities: [University],
    programs: [EdPrograms],
}
```