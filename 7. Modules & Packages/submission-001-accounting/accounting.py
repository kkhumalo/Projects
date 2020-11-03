import banking
import sys

from user.authentication import authenticate_user
from transactions.journal import receive_income, pay_expense
from banking.fvb.reconciliation import do_reconciliation 
from banking.online.reconciliation import do_reconciliation as online


help("modules")




if __name__ == "__main__":
    user_args = sys.argv
    for i in user_args:
        if i != 'accounting.py':
            print(i)
    
    amount = int()
    authenticate_user()
    receive_income(100.00)
    pay_expense(100.00)
    do_reconciliation()
   