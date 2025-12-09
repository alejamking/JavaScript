'use strict';

const numerot = [];
for (let i = 0; i < 5; i++) {
  const luku = Number(prompt(`Anna luku ${i + 1}:`));
  numerot.push(luku);
}

const target = document.querySelector('#target');

for (let i = numerot.length - 1; i >= 0; i--) {
  target.textContent += numerot[i] + ' ';
}