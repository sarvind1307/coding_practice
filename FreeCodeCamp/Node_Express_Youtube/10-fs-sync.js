const fs = require('fs');

const first = fs.readFileSync('./content/first.txt', 'utf8');
console.log(first);

const second = fs.writeFileSync('./content/second.txt',"HELLL",{flag: 'a'});

const secondRead = fs.readFileSync('./content/second.txt', 'utf8');
console.log(secondRead);
