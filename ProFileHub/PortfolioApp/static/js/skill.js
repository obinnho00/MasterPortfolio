document.addEventListener("DOMContentLoaded", () => {
    const projectButton = document.getElementById("skill"); // The dropdown toggle button

    // Check if the button exists
    if (!projectButton) {
        console.error("Button not functioning at the moment: 'skills' element not found");
        return;
    }

    // Add an event listener to handle button clicks
    projectButton.addEventListener("click", () => {
        window.location.href = "/skill/"; // Navigate to the desired URL
    });
});
