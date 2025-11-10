  'use strict';
    const name = prompt('What is your name?');


    const houseNumber = Math.floor(Math.random() * 4) + 1;
    let house;

    if (houseNumber === 1) {
      house = 'Gryffindor';
    } else if (houseNumber === 2) {
      house = 'Slytherin';
    } else if (houseNumber === 3) {
      house = 'Hufflepuff';
    } else {
      house = 'Ravenclaw';
    }

    document.querySelector('#target').innerHTML = `${name}, you are ${house}.`;