

document.getElementById("comment").addEventListener('click', () => {
    window.location('/viewe-comment/')
});

function toggleComments(id) {
    const commentsSection = document.getElementById(id);
    commentsSection.classList.toggle('show-comments');
}
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.user-name').forEach(function (element) {
        if (!element.textContent.trim() || element.textContent.trim().toLowerCase() === 'none') {
            element.style.display = 'none';
        }
    });
});



