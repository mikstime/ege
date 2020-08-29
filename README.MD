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
Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 201
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Bad request 400
```
{
    Error: 'Unable to create user due to invalid input'
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
Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 204
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Bad request 400
```
{
    Error: 'Unable to modify user due to invalid input'
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'User cannot be found'
}
```
#### GET /user
Получение информации о пользователе

Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'User cannot be found'
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Conflict 409
```
{
    Error: 'Not authenticated'
}
```
#### GET /user/programs
Получение списка отслеживаемых направлений

Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Unauthorized 401
```
{
    Error: 'Not authenticated'
}
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
Responses
![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 201
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Bad request 400
```
{
    Error: 'University cannot be added due to error occured in input'
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Unauthorized 401
```
{
    Error: 'User must have moderator permissions'
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Conflict 409
```
{
    Error: 'User must have moderator permissions'
}
```
#### GET /universities
Получить список существующих вузов

Responses
![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
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
Получить информацию о существующем вузе по id

Responses
![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
```
{
    id: ID,
    name: String,
    about: String,
    site: URL,
    preview : Photo,
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'University cannot be found'
}
```
#### GET /universities/<:id>/photos
Получить список фото из вуза

Responses
![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
```
[
    {
        id: ID,
        url: URL,
        description: String
    }
]
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'University cannot be found'
}
```
#### GET /universities/<:id>/programs
Получить список направлений в вузе

Responses
![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'University cannot be found'
}
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
Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 204
```
{
    id: ID,
    name: String,
    about: String,
    site: URL,
    preview : Photo,
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'University cannot be found'
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Unauthorized 401
```
{
    Error: 'Must have moderator permissions'
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Conflict 409
```
{
    Error: 'Must have moderator permissions'
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
Responses
![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 201
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Unauthorized 401
```
{
    Error: 'Only moderator can create universities'
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Conflict 409
```
{
    Error: 'Only moderator can create universities'
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Bad request 400
```
{
    Error: 'Can not create university due to incorrect input'
}
```
#### GET /programs/<:id>
Полочение подробной информации о направлении

Responses
![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'Educational program cannot be found'
}
```
#### GET /programs/<:id>/enrollees
Получить список поступающих на направление людей

Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'Educational Program cannot be found'
}
```
#### GET /programs/<:id>/similar
Получить список направлений, похожих на данное

Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'Educational Program cannot be found'
}
```
#### GET /programs
Получить список всех направлений

Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
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

Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
```
{
    id: ID,
    url: URL,
    description: String
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Not Found 404
```
{
    Error: 'Photo cannot be found'
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
Responses
![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 201
```
{
    id: ID,
    status: String,
    author: ID,
    email: EMAIL,
    message: String,
}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Bad request 400
```
{
    Error: 'Cannot create a feedback request due to incorrect input'
}
```
#### GET /feedback
Получить список обращений

Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
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
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Unauthorized 401
```
{
    Error: 'Need to authorize'
}
```
#### GET /feedback/<:id>
Получить информацию об обращении

Response

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
```
{{
    id: ID,
    status: String,
    author: ID,
    email: EMAIL,
    message: String,
}}
```
![#D32D2D](https://via.placeholder.com/15/D32D2D/000000?text=+) Unauthorized 401
```
{
    Error: 'Need to authorize'
}
```
#### GET /search
Осуществить поиск по вузам, фото и направлениям
Responses

![#60D32D](https://via.placeholder.com/15/60D32D/000000?text=+) Success 200
```
{
    photos: [Photo],
    universities: [University],
    programs: [EdPrograms],
}
```
