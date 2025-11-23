const dogs = [];

for (let i = 0; i < 6; i++) {
  let name = prompt("Anna koiran " + (i + 1) + " nimi:");
  while (!name || name.trim() === "") {
    name = prompt("Nimi ei voi olla tyhjä. Anna koiran " + (i + 1) + " nimi uudestaan:");
  }
  dogs.push(name.trim());
}

dogs.sort(function(a, b) {
  return b.localeCompare(a, "fi");
});

const list = document.getElementById("dogs");

dogs.forEach(function(name) {
  const li = document.createElement("li");
  li.textContent = name;
  list.appendChild(li);
});
