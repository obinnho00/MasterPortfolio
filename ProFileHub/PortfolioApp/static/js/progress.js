document.addEventListener("DOMContentLoaded", () => {
    // Select all progress bars
    const progressBars = document.querySelectorAll(".progress-bar");

    // Infinite animation for each progress bar
    progressBars.forEach((bar) => {
        const skillLevel = bar.getAttribute("data-skill-level"); // Get skill level from data attribute
        const maxValue = 10; // Maximum value
        const percentage = (skillLevel / maxValue) * 100; // Calculate percentage

        let currentPercentage = 0;

        function animateProgressBar() {
            currentPercentage = 0;
            bar.style.width = "0%"; // Reset to 0%
            bar.style.transition = "none";

            setTimeout(() => {
                bar.style.transition = "width 5s linear"; // Smooth animation
                bar.style.width = `${percentage}%`; // Move to full percentage
            }, 50); // Slight delay before restarting
        }

        bar.addEventListener("transitionend", animateProgressBar); // Reset on animation end
        animateProgressBar(); // Start animation
    });
});
