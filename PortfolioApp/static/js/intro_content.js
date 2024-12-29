document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('intro').addEventListener('click', () => {
        console.log('Button clicked');
        window.location.href = '/intro/';
    });

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            document.body.classList.add('scrolled');
        } else {
            document.body.classList.remove('scrolled');
        }
    });
});
