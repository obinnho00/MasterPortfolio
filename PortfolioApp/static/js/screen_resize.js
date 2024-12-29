document.addEventListener("DOMContentLoaded", function () {
    const grid = document.getElementById("bugReportsGrid");

    function updateGridColumns() {
        // Clear existing column classes
        grid.classList.remove("col-cols-1", "col-cols-sm-2", "col-cols-md-3", "col-cols-lg-3");

        // Apply classes based on screen width
        const width = window.innerWidth;
        if (width < 576) {
            grid.classList.add("row-cols-1"); // 1 card per row
        } else if (width >= 576 && width < 768) {
            grid.classList.add("row-cols-1"); // 1cards per row
        } else if (width >= 768 && width < 992) {
            grid.classList.add("row-cols-1"); // 1 cards per row
        } else if (width >= 992 && width < 1200) {
            grid.classList.add("row-cols-2"); // 2 cards per row
        } else {
            grid.classList.add("row-cols-3"); // 5 cards per row
        }
    }

    // Run on initial load
    updateGridColumns();

    // Add event listener for window resize
    window.addEventListener("resize", updateGridColumns);
});
