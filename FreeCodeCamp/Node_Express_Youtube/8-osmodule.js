const os = require('os');

// Info about current user
const user = os.userInfo()

// System Uptime
console.log('System Uptime ' + os.uptime() + ' seconds');

const currentOS = {
    name: os.type(),
    release: os.release(),
    totalMem: os.totalmem(),
    freeMem: os.freemem()
}

console.log(currentOS)