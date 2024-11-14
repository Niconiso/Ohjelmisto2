let dogs = [];
for (let i = 0; i < 6; i++) {
   dogs.push(prompt("Anna koiran nimi " + (i + 1) + ":"));
}
dogs.sort().reverse();
console.log("Koirat käänteisaakkosjärkässä:");
for (let dog of dogs) {
   console.log(dog);
}