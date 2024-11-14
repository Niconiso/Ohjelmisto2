let numParticipants = parseInt(prompt("Enter the number of participants:"));
let names = [];
for (let i = 0; i < numParticipants; i++) {
    let name = prompt(`Enter name for participant ${i + 1}:`);
    names.push(name);
}
names.sort();
console.log("Participants in alphabetical order:");
for (let i = 0; i < names.length; i++) {
    console.log((i + 1) + ". " + names[i]);
}