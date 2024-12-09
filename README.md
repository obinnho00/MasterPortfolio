# Overview
This portfolio web application is designed to showcase my projects, repositories, and personal details. It highlights my skills, accomplishments, and experiences in an interactive and visually appealing manner. The portfolio dynamically displays project data, including repository details, commit information, and rendered README previews.



## Features

### Project Display
- Dynamically displays current GitHub repositories.
- Projects include a default fallback image for uniformity.
- Clean and professional look with circular thumbnails.

### Repository Details
- Each repository includes:
  - Name of the repository
  - Latest commit details (message, author, and date)
  - Rendered README content

### Responsive Design
- Optimized for both desktop and mobile devices.
- Provides a seamless user experience across various screen sizes.

### Interactive Elements
- Hover effects for project thumbnails.
- Links to view repository details directly on GitHub.



## Technologies Used

### Frontend
- **HTML5**: Structuring the web pages.
- **CSS3**: Styling the portfolio.
- **JavaScript**: Adding interactivity and dynamic content rendering.

### Backend
- **Django Framework**: Handling dynamic routing and rendering project data.

### Other Tools
- **Markdown2**: For converting README files into HTML.
- **GitHub API**: Fetching repository details dynamically.



## Project Details

### Repository Information
Each project dynamically pulls data from GitHub and displays it, including:
- Commit history
- Rendered README files
- Project-specific or default images

### Image Handling
- All repositories use a default fallback image for consistency.
- Circular thumbnails enhance visual presentation.



## Setup Instructions

### Prerequisites
1. Install Python 3.x
2. Install Django framework

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   `

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   

3. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   



## Future Enhancements
- Add support for fetching user profile details dynamically from GitHub.
- Include charts and visualizations of GitHub activity.
- Enable visitors to leave feedback or comments on showcased projects.



## Contact
- **Name**: Isaac Obi Arum
- **Email**: [obinnho@gmail.com](mailto:arumi21@students.ecu.ecu)
- **LinkedIn**: [Isaac Obi Arum](https://linkedin.com/in/isaac-arum)




