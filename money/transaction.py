import datetime
import database

class Transaction:
    """ Transaction type
        Amount
        Category
        Note
        Date
        
    """
    def __init__(self, date, amount=0, expense=True, category=None, note=None):
        self.expense = expense
        self.date = date
        self.amount = amount
        self.category = category
        self.note = note

    def __repr__(self):
        return f"{self.__class__.__name__}({self.date}, expense=True, '{self.category}', 'extra notes here')"

    def __str__(self):
        return f"{self.__class__.__name__} - date: {self.date}, Expense: {self.expense}, Category: {self.category}, Notes: {self.note}"

    
def temp_next_transaction():
    date = str(input("Date: "))
    amount = float(input("Amount: "))
    expense = str(input("Expense? [y/n]: "))
    while expense not in ['n', 'y']:
        expense = str(input("Please try again [y/n]: "))
    category = str(input("Category: "))
    if expense is 'y':
        expense = True
    elif expense is 'n':
        expense = False
    else:
        raise TypeError("Incorrect type")
        
    return Transaction(date, amount, expense, category)

def parse_date(someDateString):
    pass
##    return date

if __name__ == '__main__':
    today = datetime.datetime.now().date()
    print(today)
    tr1 = Transaction(today, 54.21, expense=True, category='groceries')
    
    
    
    
