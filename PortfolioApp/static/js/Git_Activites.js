document.addEventListener("DOMContentLoaded", () => {
    const projectButton = document.getElementById("project"); // The dropdown toggle button
    const dropdownMenu = document.querySelector(".project-menue"); // The dropdown menu

    if (!projectButton || !dropdownMenu) {
        console.error("Dropdown elements not found.");
        return;
    }

    console.log("Dropdown initialized successfully"); // Debugging message

    // Select all buttons within the dropdown menu
    const buttons = dropdownMenu.querySelectorAll(".drop-down-item");

    if (buttons.length === 0) {
        console.error("No dropdown items found.");
        return;
    }

    buttons.forEach((button) => {
        button.addEventListener("click", (event) => {
            const buttonId = button.id;

            console.log(`Button clicked: ${buttonId}`); // Debugging message

            // Perform actions based on button ID
            if (buttonId === "Git-Activities") {
                window.location.href = "/Git-Activities/";
            } else if (buttonId === "Git-Repo") {
                window.location.href = "/Repo/";
            } else {
                console.error("Unhandled button ID:", buttonId);
            }
        });
    });
});
