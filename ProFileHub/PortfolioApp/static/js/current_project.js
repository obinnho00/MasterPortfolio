class ProjectButton {
    constructor(past_project, current_project) {
        this.current_project = current_project;
        this.past_project = past_project;
    }

    // Function to handle the buttons
    button_handler() {
        // Attach click event listener to the past project button
        document.getElementById(this.past_project).addEventListener('click', () => {
            // Navigate to the past projects page
            window.location.href = 'past/';
        });

        // Attach click event listener to the current project button
        document.getElementById(this.current_project).addEventListener('click', () => {
            // Navigate to the current projects page
            window.location.href = 'current/';
        });
    }
}

const projectButtons = new ProjectButton('past-project', 'current-project');
projectButtons.button_handler();
