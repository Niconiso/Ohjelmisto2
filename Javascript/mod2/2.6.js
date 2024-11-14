function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

let rolls = [];
let result;
do {
  result = rollDice();
  rolls.push(result);
} while (result !== 6);

console.log('<ul>');
for (let roll of rolls) {
  console.log(`<li>${roll}</li>`);
}
console.log('</ul>');