document.getElementById('introdoctionpage').addEventListener('click', () => {
    // Navigate to the /intro/ page
    window.location.href = '/intro/';
});

// Add scroll event listener globally after navigation
window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        document.body.classList.add('scrolled');
    } else {
        document.body.classList.remove('scrolled');
    }
});
