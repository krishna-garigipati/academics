const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());
mongoose.connect('mongodb://localhost:27017/studentDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log("Connected to MongoDB");
}).catch((err) => {
    console.error("MongoDB connection error:", err);
});


const studentSchema = new mongoose.Schema({
    name: String,
    age: Number,
    grade: String
});

const Student = mongoose.model('Student', studentSchema);


// CREATE a student
app.post('/students', async (req, res) => {
    try {
        const student = new Student(req.body);
        const result = await student.save();
        res.status(201).send(result);
    } catch (err) {
        res.status(400).send(err);
    }
});

// READ all students
app.get('/students', async (req, res) => {
    try {
        const students = await Student.find();
        res.send(students);
    } catch (err) {
        res.status(500).send(err);
    }
});

// UPDATE a student by ID
app.put('/students/:id', async (req, res) => {
    try {
        const student = await Student.findByIdAndUpdate(req.params.id, req.body, { new: true });
        res.send(student);
    } catch (err) {
        res.status(400).send(err);
    }
});

// DELETE a student by ID
app.delete('/students/:id', async (req, res) => {
    try {
        const student = await Student.findByIdAndDelete(req.params.id);
        res.send({ message: "Student deleted", student });
    } catch (err) {
        res.status(500).send(err);
    }
});

// 5. Start the server
app.listen(1456, () => {
    console.log("Server is running on http://localhost:1456");
});