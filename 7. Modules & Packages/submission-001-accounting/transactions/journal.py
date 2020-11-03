print('[Module] Journal loaded.')


def receive_income(amount):
    '''prints out received amounts'''
    print('[Journal] Received R{:.2f}'.format(amount))


def pay_expense(amount):
    '''prints out paid amounts'''
    print('[Journal] Paid R{:.2f}'.format(amount))