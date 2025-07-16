import csv  
import os 
from datetime import datetime

FILE="expenses.csv" 
FIELDS=["id","date","category","description","amount"]

def initialize_file():
    if not os.path.exists(FILE):
        with open(FILE, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()

initialize_file()

def read_expenses():
    with open(FILE, mode='r', newline='') as f:
       reader=csv.DictReader(f)
       return list(reader) 

read_expenses()

def write_expenses(expenses):
    with open(FILE,mode='w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense():
    expenses = read_expenses()

    new_id = str(int(expenses[-1]['id']) + 1) if expenses else '1'

    date_str=input("Enter date (YYYY-MM-DD) [default today]:").strip()
    if not date_str:
        date_str = datetime.today().strftime('%Y-%m-%d')
    else:
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format!")
            return
        
    category= input("Enter category (e.g., Food, Travel): ").strip()
    description= input("Enter description: ").strip()

    try:
        amount= float(input("Enter amount: ").strip())    
    except ValueError:
        print("Inavlid amount!")
        return

    expenses.append({
        "id": new_id,
        "date": date_str,
        "category": category,
        "description": description,
        "amount": f"{amount:.2f}"
    })    

    write_expenses(expenses)
    print("Expense added successfully!")

def list_expenses():
    expenses= read_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print(f"{'ID':<4} {'Date':<12} {'Category':<15} {'Description':<25} {'Amount':>10}")
    print("-" * 70)  

    for exp in expenses: 
        print(f"{exp['id']:<4} {exp['date']:<12} {exp['category']:<15} {exp['description']:<25} ${exp['amount']:>9}")
