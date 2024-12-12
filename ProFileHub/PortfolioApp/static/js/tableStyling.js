document.addEventListener("DOMContentLoaded", () => {
    // Initialize DataTables
    const table = $('#projectsTable').DataTable({
        paging: true,
        searching: true,
        lengthChange: true,
        pageLength: 2, // Default entries per page
        language: {
            search: "Search Projects:", // Customize search box label
        },
    });

    console.log("Table initialized with DataTables");

    // Example: Allow dynamic changes to the number of rows
    document.getElementById('projectsTable').addEventListener('click', () => {
        console.log("Table was clicked!"); // Example dynamic behavior
    });
});
