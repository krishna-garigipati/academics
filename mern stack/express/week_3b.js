const express = require('express');
const session = require('express-session');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

const users = [
    {username: 'john', password: '1234'},
    {username: 'alice', password: 'abcd'}
];

app.use(bodyParser.urlencoded({ extended: true }));
app.use(session({
    secret: 'mySecret',
    resave: false,
    saveUninitialized: true,
}));

app.get('/', (req, res) => {
    if(req.session.user){
        res.send(`
            <h2>Welcome, ${req.session.user.username}!</h2>
            <p><a href="/logout">Logout</a></p>
            `);
    }

    else{
        res.send(`
            <h1>23A91A6180</h1>
            <h2>Please Login</h2>
            <form action="/login" method="POST">
                <input type="text" name="username" placeholder="Username" required/>
                <input type="password" name="password" placeholder="Password" required/>
                <button type="submit">Login</button>
            </form>
        `);
    }
});

app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username && u.password === password);

    if(user){
        req.session.user = user;
        res.redirect('/');
    } else {
        res.send('<h2>Invalid credentials. Please try again.</h2><a href="/">Try Again</a>');
    }
});

app.get('/logout', (req, res) => {
    req.session.destroy(()=>{
        res.redirect('/');
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});