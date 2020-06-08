from django.db.models import Sum

def split_pn_transaction(transactions):
    positive = transactions.filter(transaction_type='received')
    negative = transactions.filter(transaction_type='transfer')

    return positive, negative

def collect_transaction(transactions):
    balance = transactions.aggregate(Sum('order__price'))
    balance = balance['order__price__sum']
    balance = balance if balance else 0

    return balance

def balance_transaction(user):
    positive, negative = split_pn_transaction(user.transactions)
    positive, negative = collect_transaction(positive), collect_transaction(negative)

    balance = positive - negative

    return balance