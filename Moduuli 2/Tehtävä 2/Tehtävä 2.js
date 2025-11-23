let count = parseInt(prompt("Kuinka monta osallistujaa?"), 10);

while (isNaN(count) || count <= 0) {
  count = parseInt(prompt("Anna osallistujien määrä kokonaislukuna (vähintään 1):"), 10);
}

const names = [];

for (let i = 0; i < count; i++) {
  let name = prompt("Anna osallistujan " + (i + 1) + " nimi:");
  while (!name || name.trim() === "") {
    name = prompt("Nimi ei voi olla tyhjä. Anna osallistujan " + (i + 1) + " nimi uudestaan:");
  }
  names.push(name.trim());
}

names.sort(function(a, b) {
  return a.localeCompare(b, "fi");
});

const listElement = document.getElementById("participant-list");

names.forEach(function(name) {
  const li = document.createElement("li");
  li.textContent = name;
  listElement.appendChild(li);
});
