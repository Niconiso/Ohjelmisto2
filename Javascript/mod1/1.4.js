    var name = prompt("Enter your name:");
    var randomNum = Math.floor(Math.random() * 4) + 1;
    var house;
    if (randomNum === 1)
      { house = "Gryffindor"; }
      else if (randomNum === 2)
      { house = "Slytherin"; }
      else if (randomNum === 3)
      { house = "Hufflepuff"; }
      else
      { house = "Ravenclaw"; }

document.write(name + ", you are in " + house + ".");