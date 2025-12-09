// etitään lomake
const startForm = document.getElementById('start-form');

// lomakkeen lähetys ->
startForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Estää sivun päivitys

    // haetaan pelaajan tiedot
    const playerName = document.getElementById('player-name').value;
    const startingCountry = document.getElementById('starting-country').value;
});