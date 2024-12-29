// Function to adjust header, navbar, footer, and buttons dynamically
function adjustLayout() {
    const screenWidth = window.innerWidth; // Get current screen width
    const screenHeight = window.innerHeight; // Get current screen height

    // Adjust body overflow to prevent horizontal scrolling
    document.body.style.overflowX = 'hidden';

    // Adjust header
    const header = document.getElementById('main-header');
    if (header) {
        header.style.height = screenWidth < 768 ? '50px' : '80px'; // Adjust height
        header.style.fontSize = screenWidth < 768 ? '0.9rem' : '1.2rem'; // Adjust font size
        header.style.width = '100%'; // Ensure header spans full width
        header.style.overflow = 'hidden'; // Prevent any overflow
    }

    // Adjust navbar items
    const navbarItems = document.querySelectorAll('#custom-nav .navbar-brand, #custom-nav .chart-button, #custom-nav .intro-button, #custom-nav .project-button, #custom-nav .cv-button, #custom-nav .skill-button');
    navbarItems.forEach((item) => {
        item.style.fontSize = screenWidth < 768 ? '0.8rem' : '1rem'; // Adjust font size
        item.style.padding = screenWidth < 768 ? '4px 6px' : '8px 12px'; // Adjust padding
        item.style.overflow = 'hidden'; // Prevent overflow
    });

    // Adjust buttons
    const buttons = document.querySelectorAll('.btn-submit, #custom-nav .chart-button, #custom-nav .intro-button, #custom-nav .project-button, #custom-nav .cv-button, #custom-nav .skill-button');
    buttons.forEach((button) => {
        button.style.fontSize = screenWidth < 768 ? '0.8rem' : '1rem'; // Adjust font size
        button.style.padding = screenWidth < 768 ? '5px 10px' : '10px 20px'; // Adjust padding
        button.style.height = screenWidth < 768 ? '35px' : '50px'; // Adjust height
        button.style.width = screenWidth < 768 ? '90%' : 'auto'; // Adjust width dynamically
        button.style.overflow = 'hidden'; // Prevent overflow
    });

    // Adjust footer
    const footer = document.querySelector('.fixed-footer');
    if (footer) {
        footer.style.height = screenWidth < 768 ? '40px' : '60px'; // Adjust height
        footer.style.fontSize = screenWidth < 768 ? '0.8rem' : '1rem'; // Adjust font size
        footer.style.padding = screenWidth < 768 ? '5px 10px' : '10px 20px'; // Adjust padding
        footer.style.width = '100%'; // Ensure footer spans full width
        footer.style.overflow = 'hidden'; // Prevent overflow
    }

    // Adjust footer links
    const footerLinks = document.querySelectorAll('.fixed-footer .footer-links a');
    footerLinks.forEach((link) => {
        link.style.fontSize = screenWidth < 768 ? '0.7rem' : '0.9rem'; // Adjust font size
        link.style.margin = screenWidth < 768 ? '3px 5px' : '5px 10px'; // Adjust spacing
        link.style.overflow = 'hidden'; // Prevent overflow
    });
}

// Add event listener for screen resizing
window.addEventListener('resize', adjustLayout);

// Run the function initially to apply settings
adjustLayout();
