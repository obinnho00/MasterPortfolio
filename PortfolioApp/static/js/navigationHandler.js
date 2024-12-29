class NavigationHandler {
    constructor() {
        this.initEventListeners();
    }

    // Initialize event listeners for all buttons
    initEventListeners() {
        document.addEventListener('DOMContentLoaded', () => {
            const buttonActions = {
                report: "/report-bug/",
                comment: "/viewe-comment/",
                skill: "/skill/",
                "download-btn": "/download-cv/",
                "References-button": "/reference/",
            };

            // Attach click event listeners to all buttons with specific IDs
            Object.keys(buttonActions).forEach(buttonId => {
                const button = document.getElementById(buttonId);
                if (button) {
                    button.addEventListener('click', () => {
                        this.redirectTo(buttonActions[buttonId]);
                    });
                } else {
                    console.warn(`Button with ID "${buttonId}" not found.`);
                }
            });
        });
    }

    // Redirect to a given URL
    redirectTo(url) {
        window.location.href = url;
    }
}

// Instantiate the NavigationHandler
new NavigationHandler();
