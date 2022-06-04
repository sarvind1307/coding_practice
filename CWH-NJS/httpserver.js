const http = require('http');

const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    console.log(req.url)
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    res.end('<h1> Arvind </h1> <p> Hi I am Arvind!</p>');
})

server.listen(port, () => {
    console.log('Server is listening on port '+ port);
});