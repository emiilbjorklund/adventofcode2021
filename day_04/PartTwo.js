


const transpose = matrix => matrix.reduce((prev, next) => next.map((item, i) => (prev[i] || []).concat(next[i])), []);



function calculate(data, size = 5) {
    let candidate;

    let plays = data.shift().split(',').map(function (item) {
        return parseInt(item, 10);
    });

    // Remove empty lines
    data = data.filter((a) => a);

    var boards = [];

    // Convert input to integer matrices
    for (let i = 0; i < data.length; i += size) {
        let rows = data.slice(i, i + size).map(element => {
            element = element.trim().replace(/\s+/g, " ");
            return element.split(' ').map(function (item) {
                return parseInt(item, 10);
            });
        })
        rows = rows.concat(transpose(rows))
        boards.push(rows);
    }

    let bingo = false;
    let idx = 4;
    while (!bingo) {
        let play = plays.slice(0, idx);
        for (let j = 0; j < boards.length; j += 1) {
            for (let k = 0; k < boards[j].length; k += 1) {
                if (boards[j][k].every(elem => play.includes(elem))) {
                    // console.log(boards[j])
                    if (boards.length > 1) {
                        boards.splice(j, 1)
                        break
                    } else {
                        bingo = true;
                        let sum = 0;
                        boards[j].splice(0, 5).forEach(element => {
                            sum += element.filter(item => !play.includes(item)).reduce((a, b) => a + b, 0)
                            candidate = sum * play[play.length - 1]
                        });
                    }
                }
            };
        }
        idx += 1;
    }
    console.log(candidate)
}


const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

var lines = [];

readline.prompt();

readline.on('line', (line) => {
    lines.push(line);
});

readline.on('close', function (cmd) {

    calculate(lines)
    process.exit(0);
});

