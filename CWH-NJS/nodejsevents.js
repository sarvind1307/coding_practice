const EventEmitter = require('events');

class MyEmitter extends EventEmitter {}

const myEmitter = new MyEmitter();
myEmitter.on('WaterFull', () => {
    console.log('Turn PUMP off.');
    setTimeout(() => {
        console.log('PLEASE Turn PUMP off.');
    }, 3000);
});
console.log("A")
myEmitter.emit('WaterFull');
console.log("B")
myEmitter.emit('WaterFull');
console.log("C")