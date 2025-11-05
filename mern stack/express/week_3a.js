const express = require('express');
const session = require('express-session');
const cookieParser = require('cookie-parser');

const app = express();
const PORT = 3000;

app.use(cookieParser());
app.use(express.urlencoded({ extended: true }));

app.use(session({
    secret: 'mySecretKey',
    resave: false,
    saveUninitialized: true,
    cookie: {maxAge: 60000}
}));

app.get('/', (req, res) => {
    if(req.session.username){
        res.send(`
            <h2>Welcome back, ${req.session.username}!</h2>
            <p><a href="/logout">Logout</a></p>
        `);
    }

    else{
        res.send(`
            <h1>23A91A6180</h1>
            <h2>Hello, Guest!</h2>
            <form action="/login" method="POST">
            
                <input type="text" name="username" placeholder="Enter your name" required/>
                <button type="submit">Login</button>
            </form>
            `)
    }
});

app.post('/login', (req, res) => {
    const username  = req.body.username;
    req.session.username = username;
    res.cookie('username', username);
    res.redirect('/');
});

app.get('/logout', (req, res) => {{
    res.clearCookie('username');
    req.session.destroy(err => {
        res.redirect('/');
    });
}});
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});

