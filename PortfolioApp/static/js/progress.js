document.addEventListener("DOMContentLoaded", () => {
    // Select all progress bars
    const progressBars = document.querySelectorAll(".progress-bar");

    // Infinite animation for each progress bar
    progressBars.forEach((bar) => {
        const skillLevel = bar.getAttribute("data-skill-level"); // Get skill level from data attribute
        const maxValue = 10; // Maximum value
        const percentage = (skillLevel / maxValue) * 100; // Calculate percentage

        function animateProgressBar() {
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

    // Adjust grid based on screen size
    const skillList = document.querySelector(".skill-list");

    function adjustGrid() {
        const screenWidth = window.innerWidth;

        if (screenWidth < 600) {
            // Smaller screens: 1 skill per row
            skillList.style.gridTemplateColumns = "repeat(1, 1fr)";
        } else if (screenWidth < 900) {
            // Medium screens: 2 skills per row
            skillList.style.gridTemplateColumns = "repeat(2, 1fr)";
        } else {
            // Larger screens: Default layout
            skillList.style.gridTemplateColumns = "repeat(auto-fit, minmax(200px, 1fr))";
        }
    }

    // Adjust grid on page load
    adjustGrid();

    // Re-adjust grid on window resize
    window.addEventListener("resize", adjustGrid);
});
