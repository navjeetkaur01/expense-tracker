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


def read_expenses():
    with open(FILE, mode='r', newline='') as f:
       reader=csv.DictReader(f)
       return list(reader) 


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

def delete_expense():  
    expenses = read_expenses()
    if not expenses:
        print("No expenses to delete.")
        return

    list_expenses()  
    del_id = input("Enter the ID of the expense to delete: ").strip() 
     
    new_expenses= [e for e in expenses if e['id']!=del_id] 
    if len(new_expenses) == len(expenses):
        print("ID not found.")
        return
    
    write_expenses(new_expenses)
    print(f"Deleted expense ID {del_id}.")

def edit_expense():
    expenses = read_expenses()
    if not expenses:
        print("No expenses to edit.")
        return

    list_expenses()
    edit_id= input("Enter the ID of the expense to edit: ").strip() 

    for exp in expenses:
        if exp['id'] == edit_id:
            print("Leave blank to keep current value.")   

            new_date = input(f"Date ({exp['date']}): ").strip()
            if new_date:
                try:
                    datetime.strptime(new_date, '%Y-%m-%d')
                    exp['date'] = new_date
                except ValueError:
                    print("Invalid date format. keeping original.")

            new_cat = input(f"Category ({exp['category']}): ").strip()
            if new_cat:
                exp['category'] = new_cat

            new_desc = input(f"Description ({exp['description']}): ").strip()
            if new_desc:
                exp['description'] = new_desc

            new_amount = input(f"Amount ({exp['amount']}): ").strip()
            if new_amount:
                try:
                    float_amt = float(new_amount)
                    exp['amount'] = f"{float_amt:.2f}"
                except ValueError:
                    print("Invalid amount. Keeping original.")

            write_expenses(expenses)
            print("Expense updated.")
            return

    print("ID not found.")        

def show_menu(): 
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Exit")

def main():
    initialize_file()

    while True: 
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            list_expenses()
        elif choice == '3':
            edit_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
