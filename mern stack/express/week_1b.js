const express = require('express');
const app = express();

app.use(express.json());

let message = 'Hello';

app.get('/message', (req, res) => {
    res.send(message);
});

app.post('/message', (req, res) => {
    const newMessage = req.body.message;
    if (newMessage) {
        message = newMessage;
        res.send(`Message updated to: ${message}`);
    } else {
        res.status(400).send('Bad Request: Message is required');
    }
});

app.put('/message', (req, res) => {
    const newMessage = req.body.message;
    res.send(`Message updated to: ${newMessage}`);
});

app.delete('/message', (req, res) => {
    message = '';
    res.send('Message deleted');            
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});