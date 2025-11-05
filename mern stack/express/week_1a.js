const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello world');
})

app.get('/user/:id', (req, res) => {
    const userId = req.params.id;
    res.send(`User ID is: ${userId}`);
})

app.get('/product/:id/:name', (req, res) => {
    const productId = req.params.id;
    const productName = req.params.name;
    res.send(`Product ID is: ${productId}, Product Name is: ${productName}`);
})

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});

