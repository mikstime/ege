const express = require('express')
const app = express()
app.use(express.json())
app.use(express.urlencoded({ extended: false }))
const port = 3000
const user = {
  id: 1,
  firstName: "Михаил",
  lastName: "Балицкий",
  egeResults: {
    russian: 100,
    mathProf: 100,
    mathBase: 100,
    biology: 100,
    informatics: 100,
    socialStudies: 100,
    Physics: 100,
    Chemistry: 100,
    History: 100,
    geography: 100,
    english: 100,
    german: 100,
    french: 100,
    chinese: 100,
    Spanish: 100,
    literature: 100,
  }
}

const program =     {
  id: 1,
  code: "11.1.1",
  university: 1,
  universityName: "МГТУ им. Н.Э. Баумана",
  name: "Информационные технологии ИУ10",
  preview : {
    id: 1,
    url: "https://www.google.com/url?sa=i&url=http%3A%2F%2Fedu.bmstu.ru%2Funiversity%2Fnovosti%2Fmgtu-im-n-e-baumana-v-top-20-vuzov-pervogo-nacionalnogo-rejtinga-rossii%2F&psig=AOvVaw0x9u6ppw5peVqiGN12mKIx&ust=1605839157018000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJiGqZbHje0CFQAAAAAdAAAAABAD",
    description: "Красивое фото МГТУ"
  }
}
app.get('/', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.send('API documentation can be found at: https://github.com/mikstime/ege')
})

app.post('/api/v1/login/', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.status(201).send(JSON.stringify(user))
})

app.post('/api/v1/users/', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.send(201, JSON.stringify(user))
})

app.get('/api/v1/users/:id', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.send(200, JSON.stringify(user))
})

app.get('/api/v1/programs/:id', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.send(200, JSON.stringify(program))
})

app.get('/api/v1/programs', (req, res) => {
  res.setHeader('Content-Type', 'application/json');
  res.send(200, JSON.stringify([program, program, program]))
})

app.listen(3000, () => console.log('Сервер запущен на порту 3000'))