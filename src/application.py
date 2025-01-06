from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
import os

app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Mock database - In a real application, use a proper database like SQLite or PostgreSQL.
expenses = []

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Home route
@app.route('/')
def index():
    # Create Plotly graph for expenses
    if expenses:
        descriptions = [expense['description'] for expense in expenses]
        amounts = [float(expense['amount']) for expense in expenses]
        
        # Bar chart for expenses
        fig = go.Figure([go.Bar(x=descriptions, y=amounts, marker=dict(color='blue'))])
        fig.update_layout(title='Expense Visualization', xaxis_title='Description', yaxis_title='Amount')

        # Convert plotly figure to HTML div
        graph_html = pio.to_html(fig, full_html=False)
    else:
        graph_html = ""  # No expenses, so no graph

    return render_template('index.html', expenses=expenses, graph_html=graph_html)

# Route for adding expense via form
@app.route('/add', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = request.form['amount']

    # Add expense to the list
    expenses.append({'description': description, 'amount': amount})
    return redirect(url_for('index'))

# Route for deleting expense
@app.route('/delete/<int:index>', methods=['POST'])
def delete_expense(index):
    # Delete the selected expense from the list
    if 0 <= index < len(expenses):
        expenses.pop(index)
    return redirect(url_for('index'))

# Route for uploading CSV or Excel file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']

    # Check if the file is allowed and not empty
    if file and allowed_file(file.filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)  # Save the uploaded file

        # Read file into a Pandas DataFrame
        if file.filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file.filename.endswith('.xlsx'):
            df = pd.read_excel(file_path)

        # Convert the DataFrame to expenses list and append to the current expenses
        for _, row in df.iterrows():
            expenses.append({'description': row['description'], 'amount': row['amount']})

        return redirect(url_for('index'))

if __name__ == "__main__":
    # Create the upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    
    app.run(host="0.0.0.0", port=5000, debug=True)

