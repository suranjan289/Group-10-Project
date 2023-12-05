from flask import Flask, render_template
import sqlite3
import pathlib

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('coffee_shop_sales.db')
cursor = conn.cursor()

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    # Add logic to fetch information about the data
    return render_template('about.html')

@app.route("/data")
def data():
    # Add logic to fetch and display data
    con = sqlite3.connect('coffee_shop_sales.db')
    cursor =con.cursor()
    coffee_sales = cursor.execute("SELECT * FROM coffee_sales").fetchall()
    con.close
    
    return render_template("data_table.html", coffee_sales=coffee_sales)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)