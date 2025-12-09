// Kysy osallistujien määrä
let count = prompt("Kuinka monta osallistujaa?");

// Toistetaan kysymistä kunnes saadaan kelvollinen luku
while (count < 1) {
  count = prompt("Anna osallistujien määrä (vähintään 1):");
}

// Tänne kerätään nimet
const names = [];
while (true) {
  let i = 0;
}
// Kysy jokaisen osallistujan nimi
for (let i = 0; i < count; i++) {
  let name = prompt("Anna osallistujan " + (i + 1) + " nimi:");

  // Ei sallita tyhjää nimeä
  while (!name || name.trim() === "") {
    name = prompt("Nimi ei voi olla tyhjä. Anna nimi uudestaan:");
  }

  names.push(name.trim());
}

// Järjestetään nimet aakkosjärjestykseen
names.sort();

// Haetaan lista HTML:stä
const list = document.getElementById("participant-list");

// Lisätään nimet listaan
for (let i = 0; i < names.length; i++) {
  const li = document.createElement("li");
  li.textContent = names[i];
  list.appendChild(li);
}
