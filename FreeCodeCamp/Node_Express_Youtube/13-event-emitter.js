const EventEmitter = require('events');

const customEmitter = new EventEmitter();

customEmitter.on('response', (name, id) => {
    console.log(`Data Received, ${name} ${id}`);
});

customEmitter.on('response', () => {
    console.log(`Different Logic.`);
});

customEmitter.emit('response', 'arvind', 13);