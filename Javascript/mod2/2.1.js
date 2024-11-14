let numbers = [];

for (let i = 0; i < 5; i++) {
    let numero = prompt("Anna numerot " + (i + 1) + ":");
    numbers.push(Number(numero));
}
console.log("Numerot käänteisjärkässä:");
for (let i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
}