// Function to adjust styles dynamically
function adjustElements() {
    const screenWidth = window.innerWidth; // Get the current screen width
 

    // Adjust form-container size
    const formContainer = document.querySelector('.form-container');
    if (formContainer) {
        formContainer.style.width = screenWidth < 480 ? '90%' : '60%'; // Smaller width for mobile
        formContainer.style.padding = screenWidth < 480 ? '10px' : '20px'; // Adjust padding
    }

    // Adjust rounded-img size
    const roundedImg = document.querySelector('.rounded-img');
    if (roundedImg) {
        roundedImg.style.width = screenWidth < 480 ? '40px' : '55px'; // Adjust image size
        roundedImg.style.height = screenWidth < 480 ? '40px' : '55px';
    }

    // Adjust button styles
    const buttons = document.querySelectorAll('.btn-submit');
    buttons.forEach((button) => {
        button.style.fontSize = screenWidth < 480 ? '0.8rem' : '1rem'; // Adjust font size
        button.style.padding = screenWidth < 480 ? '6px 12px' : '10px 20px'; // Adjust padding
    });
}

// Add event listener for screen resizing
window.addEventListener('resize', adjustElements);

// Run the function initially to apply settings
adjustElements();
