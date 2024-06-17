# Paleolightning Data Analysis Web App

## Overview

This web application analyzes paleolightning data to determine the correlation between lightning strike density and wildfires. The application visualizes data over longitude and latitude, providing insights into how lightning activity impacts wildfire occurrences. Built using Django, this app offers an interactive platform for researchers and enthusiasts to explore historical lightning data.

## Features

- **Data Visualization**: Interactive maps plotting lightning strikes over specified regions.
- **Correlation Analysis**: Tools to analyze the relationship between lightning strike density and wildfire occurrences.
- **User-Friendly Interface**: Easy navigation and data exploration with a responsive design.
- **Data Filtering**: Filter data by date, location, and other parameters to focus on specific areas of interest.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/paleolightning-analysis.git
    cd paleolightning-analysis
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000/`

## Usage

Once the server is running, you can access various features of the application:

- **Interactive Map**: Navigate to the map section to explore lightning strike data over different regions.
- **Data Filters**: Use the filtering options to narrow down the data by date, location, and other criteria.
- **Correlation Analysis**: View analysis results showing the correlation between lightning activity and wildfire occurrences.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or feedback, please contact [Andrew Ondara](mailto:your-email@example.com) or [Saloni Dhal](mailto:your-email@example.com).

---

Feel free to replace placeholder links and email addresses with actual ones. If you need further customization, let me know!
