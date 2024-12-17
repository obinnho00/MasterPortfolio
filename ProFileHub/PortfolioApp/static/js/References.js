document.addEventListener('DOMContentLoaded', () => {

    console.log('JavaScript Loaded!');
    

    const container = document.querySelector('.container');
    const centerX = container.offsetWidth / 2;
    const centerY = container.offsetHeight / 2;
    const radius = 350;

    try {
        const references = JSON.parse('{{ reference_data|escapejs }}');
        console.log('Parsed References:', references);

    } catch (error) {
        console.error('Error parsing reference_data:', error);}

    const tooltips = []; // Store all tooltips for toggling

    // Create users, tooltips, and lines
    references.forEach((user, index) => {
        const angle = (index / references.length) * 2 * Math.PI;
        const x = centerX + radius * Math.cos(angle) - 35;
        const y = centerY + radius * Math.sin(angle) - 35;

        // User icon
        const userDiv = document.createElement('div');
        userDiv.classList.add('user');
        userDiv.style.left = `${x}px`;
        userDiv.style.top = `${y}px`;

        // Tooltip
        const tooltip = document.createElement('div');
        tooltip.classList.add('tooltip');
        tooltip.style.display = 'none'; // Initially hidden
        tooltip.innerHTML = `
        <img src="/static/images/imoji.jpg" alt="User Image">
        <div class="tooltip-content">
            <strong>${user.name}</strong>
            Email: ${user.email}<br>
            Company: ${user.company}<br>
            Role: ${user.role}
        </div>
    `;

        tooltip.style.left = `${x}px`;
        tooltip.style.top = `${y - 90}px`;

        container.appendChild(tooltip);
        tooltips.push(tooltip);

        // Show tooltip on hover
        userDiv.addEventListener('mouseenter', () => tooltip.style.display = 'flex');
        userDiv.addEventListener('mouseleave', () => tooltip.style.display = 'none');

        container.appendChild(userDiv);

        // Line from center to user
        const line = document.createElement('div');
        line.classList.add('line');
        const deltaX = x + 35 - centerX;
        const deltaY = y + 35 - centerY;
        const length = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
        const angleDeg = Math.atan2(deltaY, deltaX) * (180 / Math.PI);

        line.style.height = `${length}px`;
        line.style.left = `${centerX}px`;
        line.style.top = `${centerY}px`;
        line.style.transform = `rotate(${angleDeg}deg)`;

        container.appendChild(line);
    });

    // Middle server click toggle functionality
    const server = document.getElementById('server');
    let tooltipsVisible = false;

    server.addEventListener('click', () => {
        tooltipsVisible = !tooltipsVisible;

        // Show or hide all tooltips
        tooltips.forEach(tooltip => {
            tooltip.style.display = tooltipsVisible ? 'flex' : 'none';
        });
    });

});
