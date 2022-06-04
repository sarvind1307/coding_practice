const fs = require('fs');

fs.readFile('index.js', 'utf8', (err, data) => {
    console.log(err, data);
})

console.log("File reading done.")

const a = fs.readFileSync('second.js');
console.log(a.toString());
console.log("File reading done SYNC.")