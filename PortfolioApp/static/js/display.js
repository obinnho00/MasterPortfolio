document.addEventListener("DOMContentLoaded", function () {
    const bugReportsGrid = document.getElementById("bugReportsGrid"); // The container for all bug report items
    const bugReportItems = Array.from(document.querySelectorAll(".bug-report-item")); // Select all bug report items
    const currentPageDisplay = document.querySelector(".current-page"); // Element to display the current page
    const itemsPerPage = 3; // Fixed number of items per page
    let currentPage = 0; // Start at the first page (0-indexed)

    // Function to render bug reports and update the current page display
    function renderBugReports(page) {
        const start = page * itemsPerPage; // Calculate start index
        const end = start + itemsPerPage; // Calculate end index

        // Show only the relevant items
        bugReportItems.forEach((item, index) => {
            item.style.display = index >= start && index < end ? "block" : "none";
        });

        // Update the current page number display
        if (currentPageDisplay) {
            currentPageDisplay.textContent = `Page: ${page + 1}`;
        }
    }

    // Handle mouse scroll to change pages
    function handleScroll(event) {
        if (event.deltaY > 0 && (currentPage + 1) * itemsPerPage < bugReportItems.length) {
            // Scroll down to next page
            currentPage++;
        } else if (event.deltaY < 0 && currentPage > 0) {
            // Scroll up to previous page
            currentPage--;
        }
        renderBugReports(currentPage);
    }

    renderBugReports(currentPage); // Render the first page
    bugReportsGrid.addEventListener("wheel", handleScroll); // Add event listener for scrolling
});
