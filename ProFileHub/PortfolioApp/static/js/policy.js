document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("policy-popup");
    const footerLink = document.querySelector("#footer-popup a[href*='website_policies']");
    const closeButton = document.querySelector(".policy-close-button");

    // Ensure modal starts hidden
    modal.style.display = "none";

    // Open modal on footer link click
    footerLink.addEventListener("click", (event) => {
        event.preventDefault(); // Prevent navigation to another page
        modal.style.display = "block";
    });

    // Close the modal
    closeButton.addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Close modal when clicking outside the modal content
    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});
