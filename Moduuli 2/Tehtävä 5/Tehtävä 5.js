const numbers = [];
let n = parseInt(prompt("Anna numero:"), 10);

while (true) {
  if (numbers.includes(n)) {
    alert("Numero on jo annettu!");
    break;
  }
  if (!isNaN(n)) numbers.push(n);
  n = parseInt(prompt("Anna numero:"), 10);
}

numbers.sort(function(a, b) {
  return a - b;
});

console.log(numbers);
