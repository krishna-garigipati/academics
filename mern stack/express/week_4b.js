const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors');
const { name } = require('ejs');
const json = require('body-parser/lib/types/json');
const app = express();
app.use(cors());
app.use(bodyParser.json());
let students = [
  { id: 1, name: "John Doe", course: "B.Tech"},
  { id: 2, name: "Jane Smith", course: "MCA"}
];
app.get('/api/students', (req, res) => {
  res.json(students);
});
app.get('/api/students/:id', (req, res) => {
  const student = students.find(s => s.id ==req.params.id);
  student ? res.json(student) : res.status(404).json
  ({ message: "Not Found" });
});

app.post('/api/students', (req, res) => {
  const newStudent = {
    id: students.length + 1,
    name: req.body.name,
    course: req.body.course
  };
  students.push(newStudent);
  res.status(201).json(newStudent);
});

app.put('/api/students/:id', (req, res) => {
  const student = students.find(s => s.id == req.params.id);
  if(student){
    student.name =req.body.name;
    student.course = req.body.course;
    res.json(student)
  } else{
    res.status(404).json({message: "Not Found "});
  }
});

app.delete('/api/students/:id', (req, res ) => {
  students =students.filter(s => s.id != req.params.id);
  res.json({message : "Deleted"});
});

app.listen(3500, () => {
  console.log('Server running on https://localhost:3500');
})