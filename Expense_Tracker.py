import csv
import os
import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def load_expenses(filename="expenses.csv"):
    expenses = []
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            expenses = [row for row in reader]
    return expenses

def save_expenses(expenses, filename="expenses.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
        writer.writerows(expenses)

def add_expense(date, category, amount, description):
    expenses = load_expenses()
    expenses.append([date, category, amount, description])
    save_expenses(expenses)

def filter_by_category(category):
    expenses = load_expenses()
    return [exp for exp in expenses if exp[1].lower() == category.lower()]

def get_monthly_summary():
    expenses = load_expenses()
    summary = {}
    for exp in expenses:
        date_obj = datetime.datetime.strptime(exp[0], "%Y-%m-%d")
        month = date_obj.strftime("%Y-%m")
        summary[month] = summary.get(month, 0) + float(exp[2])
    return summary

@app.route('/')
def home():
    return render_template("Expense.html")

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    add_expense(data['date'], data['category'], data['amount'], data['description'])
    return jsonify({"message": "Expense added successfully"})

@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(load_expenses())

@app.route('/filter', methods=['GET'])
def filter_expenses():
    category = request.args.get('category', '')
    return jsonify(filter_by_category(category))

@app.route('/summary', methods=['GET'])
def summary():
    return jsonify(get_monthly_summary())

if __name__ == "__main__":
    app.run(debug=True)
