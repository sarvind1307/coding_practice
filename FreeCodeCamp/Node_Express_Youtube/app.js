const http = require('http')
const fs = require('fs');

http.createServer((req, res) => {
    // const fileStream = fs.readFileSync('./content/big.txt', 'utf8');
    // res.end(fileStream)

    const fileStream = fs.createReadStream('./content/big.txt', 'utf8');
    fileStream.on('open', () => {
        fileStream.pipe(res);
    });
    fileStream.on('error', (err) => {
        res.end(err);
    })

}).listen(3000)