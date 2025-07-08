import csv  
import os 

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