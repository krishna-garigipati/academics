const http = require('http');
const ser = http.createServer((req, res) => {
    res.end("Hello")
});

ser.listen(1346);