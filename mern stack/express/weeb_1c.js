const express = require('express');
const app = express();

function loggerMiddleware(req, res, next) {
    console.log(`${req.method} request for '${req.url}'`);
    next();
}

app.use(loggerMiddleware);

app.get('/', (req, res) => {
    res.send('Welcome to the home route');
});

app.get('/about', (req, res) => {
    res.send('About this application');
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

