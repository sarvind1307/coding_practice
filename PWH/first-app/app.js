// Defining a function.
// function sayHello(name) {
//     console.log("Hello "+ name + "!!!");
// }

// sayHello("Arvind");


// Importing a module
// const log = require("./logger");

// console.log(log)

// log("mess");

// PATH
// const path = require('path');

// var pathObj = path.parse(__filename);
// console.log(pathObj)


// OS
// const os = require('os');

// console.log(os.totalmem())


// FILES
// const fs = require("fs");

// const files = fs.readdirSync('./')

// console.log(files)
// fs.readdir('$',function(err, files) {
//     if (err) console.log('Error', err);
//     else console.log('Result', files)
// });


// EVENTS
// const EventEmitter = require('events');
// const emitter = new EventEmitter();

// // Register a listener
// emitter.on('messageLogged', (arg) => {
//     console.log("Listener Called", arg);
// });


// EVENTS FROM OTHER FILE

// const EventEmitter = require('events');
// // const emitter = new EventEmitter();



// const Logger = require('./logger');
// const logger = new Logger();

// // Register a listener
// logger.on('messageLogged', (arg) => {
//     console.log("Listener Called", arg);
// });

// logger.log('message')


// HTTP MODULE
const http = require('http');

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        res.write('Hello');
        res.end();
    }

    if (req.url === '/api/courses') {
        res.write(JSON.stringify([1,2,3,4,5]));
        res.end();
    }
});

// server.on('connection', (socket) => {
//     console.log('New Connection');
// });

server.listen(3000);

console.log('Listening on Port 3000...');