let numbers = [];
while (true) {
   let num = Number(prompt("Anna numerot, jos annat 0 niin loppuu:"));
   if (num === 0) {
       break;
   }
   numbers.push(num);
}
numbers.sort((a, b) => b - a);
console.log("Numerot suurimmasta pienimpään:");
for (let number of numbers) {
   console.log(number);
}