const numbers = [];
let n = parseInt(prompt("Anna numero (0 lopettaa):"), 10);

while (n !== 0) {
  if (!isNaN(n)) numbers.push(n);
  n = parseInt(prompt("Anna numero (0 lopettaa):"), 10);
}

numbers.sort(function(a, b) {
  return b - a;
});
console.log(numbers);
