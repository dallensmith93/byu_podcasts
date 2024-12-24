document.addEventListener("DOMContentLoaded", function () {
    const podcastItems = document.querySelectorAll(".podcast-item");

    podcastItems.forEach((item) => {
        item.addEventListener("click", () => {
            alert(`You clicked on "${item.textContent.trim()}"!`);
        });
    });
});
