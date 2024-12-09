document.addEventListener("DOMContentLoaded", function () {
    const rowsPerPage = 3;
    let currentPage = 1;
    const table = document.getElementById("projectsTable");
    const rows = table.querySelectorAll("tbody tr");
    const pagination = document.getElementById("pagination");
    const searchInput = document.getElementById("search");
    const sizeFilter = document.getElementById("sizeFilter");

    function renderTable() {
        const totalRows = Array.from(rows).filter(row => row.style.display !== "none");
        const totalPages = Math.ceil(totalRows.length / rowsPerPage);

        // Hide all rows, then show rows for the current page
        rows.forEach((row, index) => {
            row.style.display = "none";
        });

        totalRows.slice((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage).forEach(row => {
            row.style.display = "table-row";
        });

        // Update pagination
        pagination.innerHTML = "";
        if (totalPages > 1) {
            for (let i = 1; i <= totalPages; i++) {
                const pageButton = document.createElement("span");
                pageButton.textContent = i;
                pageButton.className = `page-number ${i === currentPage ? "active" : ""}`;
                pageButton.addEventListener("click", function () {
                    currentPage = i;
                    renderTable();
                });
                pagination.appendChild(pageButton);
            }
        }
    }

    function searchAndFilter() {
        const searchValue = searchInput.value.toLowerCase();
        const sizeValue = sizeFilter.value;

        rows.forEach(row => {
            const rowText = row.textContent.toLowerCase();
            const rowSize = row.cells[7].textContent.trim();

            if (
                (rowText.includes(searchValue) || searchValue === "") &&
                (rowSize === sizeValue || sizeValue === "")
            ) {
                row.style.display = "table-row";
            } else {
                row.style.display = "none";
            }
        });

        currentPage = 1; // Reset to the first page
        renderTable();
    }

    searchInput.addEventListener("input", searchAndFilter);
    sizeFilter.addEventListener("change", searchAndFilter);

    renderTable(); 
});
