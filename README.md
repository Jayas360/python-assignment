# Web Scraping Project

This Python project aims to perform web scraping by requesting data from a URL, storing it in a PostgreSQL database, and then retrieving the data from the database and storing it in a CSV file.

## Prerequisites

Before running the project, ensure you have the following prerequisites installed:

- [Python(3.11.3)](https://www.python.org/downloads/): The project is developed using Python. Make sure you have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).

- [pip](https://pip.pypa.io/en/stable/installation/): pip is the package installer for Python. It is used to install project dependencies. pip usually comes pre-installed with Python. You can check if pip is installed by running `pip --version` in your terminal or command prompt.

- [PostgreSQL(16)](https://www.postgresql.org/download/): PostgreSQL is the database management system used in the project. Make sure you have PostgreSQL installed and running on your system. You can download and install PostgreSQL from the [official website](https://www.postgresql.org/download/).


## Project Structure

1. **Project Structure**
   - `main.py`: Python script for web scraping and data manipulation.
   - `db.py`: Python script containing functions for database operations.

## How to Run

2. **How to Run**
   - **Clone the Repository:**
     ```bash
     git clone <repository_url>
     ```
   - **Install Dependencies:**
     ```bash
     pip install psycopg2 beautifulsoup4 requests
     ```
   - **Set up PostgreSQL Database:**
     - Ensure PostgreSQL is installed and running.
     - Update the PostgreSQL configurations in the `db.py` file to match your local setup (`pg_config` dictionary).
     - Create a database and use the same during configuration(`pg_config` in the `db.py` file)
   - **Run the Main Script:**
     ```bash
     python main.py
     ```

## Files Overview

3. **Files Overview**
   - **`main.py`**
     - Requests data from a specified URL using the `requests` library.
     - Parses the HTML content using `BeautifulSoup`.
     - Extracts specific elements from the HTML content.
     - Creates a table in the PostgreSQL database using functions from `db.py`.
     - Inserts scraped data into the database.
     - Retrieves data from the database and stores it in a CSV file.
   - **`db.py`**
     - `create()`: Creates a table named `testdetail` in the PostgreSQL database if it doesn't exist.
     - `insert(data)`: Inserts data into the `testdetail` table.
     - `fetch()`: Retrieves all data from the `testdetail` table.
     - `deleteAll()`: Deletes all records from the `testdetail` table.

## Note

4. **Note**
   - Make sure to update the PostgreSQL configuration (`pg_config` dictionary) in `db.py` with your own database credentials (`database`, `host`, `user`, `password`, `port`). Additionally, ensure that the URL in `main.py` points to the desired webpage for scraping.
