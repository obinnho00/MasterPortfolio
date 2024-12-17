document.addEventListener("DOMContentLoaded", function () {
    const downloadButton = document.getElementById("download-btn");
    if (downloadButton) {
        downloadButton.addEventListener("click", function () {
            // Redirect to the download URL
            window.location.href = "/download-cv/";
        });
    }
});
