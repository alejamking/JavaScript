document.addEventListener('DOMContentLoaded', function () {
    const target = document.getElementById("target");
    if (target) {
        target.innerHTML = `
            <li>First item</li>
            <li>Second item</li>
            <li>Third item</li>
        `;
        target.classList.add("my-list");
    }
});
