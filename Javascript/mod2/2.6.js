let rolls = [];
while (true) {
  let roll = Math.floor(Math.random() * 6) + 1;
  rolls.push(roll);
  if (roll === 6) break;
}
rolls.forEach(roll => console.log(`<li>${roll}</li>`));
