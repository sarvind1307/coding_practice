const http = require('http');
const fs = require('fs');

const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
    console.log(req.url)
    
    res.setHeader('Content-Type', 'text/html');
    if (req.url === '/') {
        res.statusCode = 200;
        res.end('<h1> Arvind </h1> <p> Hi I am Arvind!</p>');
    }
    if (req.url === '/about') {
        res.statusCode = 200;
        res.end('<h1> ABOUT Arvind </h1> <p> ABOUT Hi I am Arvind!</p>');
    }
    if (req.url === '/hello') {
        res.statusCode = 200;
        const data = fs.readFileSync('index.html');
        res.end(data.toString());
    }
    else {
        res.statusCode = 404;
        res.end('<h1> NOT FOUND</h1> <p> ABOUT Hi I am Arvind!</p>');
        
    }
    
})

server.listen(port, () => {
    console.log('Server is listening on port '+ port);
});