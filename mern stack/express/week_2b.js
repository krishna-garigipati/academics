const express = require('express');
const app = express();

app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: false }));

app.get('/', (req, res) => {
    res.render('form', { name: 'Krishna Garigipati', email: 'srinimagi99@gmail.com' });
});


app.post('/submit', (req, res) => {
    const { name, email } = req.body;
    res.render('results', { name, email });
});

app.listen(3000, () => {
    console.log('Server running on http://localhost:3000');
});