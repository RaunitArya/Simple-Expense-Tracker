# Simple-Expense-Tracker
A simple Flask-based expense tracker web application that allows users to add, delete, and upload expense data from CSV or Excel files. The app provides a visual representation of expenses using Plotly.

## Features

- **Add Expenses**: Users can manually add expense descriptions and amounts.
- **Delete Expenses**: Users can delete individual expenses from the tracker.
- **Upload CSV/Excel Files**: Users can upload CSV or Excel files to add multiple expenses at once.
- **Expense Visualization**: Displays a bar chart of expenses using Plotly.

## Requirements

- Python 3.x
- Flask
- Pandas
- Plotly

## Installation

1. Clone the repository:

        git clone https://github.com/yourusername/expense-tracker.gitcd expense-tracker
2. Install the required dependencies:

        pip install -r requirements.txt
3. Run the Flask application:

        python application.py
4. Visit `http://localhost:5000` in your web browser.

## File Upload

- Supported file formats: CSV, XLSX.
- Ensure the file contains the following columns:
    - `description`: Description of the expense.
    - `amount`: The amount of the expense.