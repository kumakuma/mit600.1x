def print_statement(month, payment, balance):
    print("Month: " + str(month + 1))
    print("Minimum monthly payment: " + str(round(payment, 2)))
    print("Remaining balance: " + str(round(balance, 2)))


def print_year_end(total, balance):
    print("Total paid: " + str(round(total, 2)))
    print("Remaining balance: " + str(round(balance, 2)))


def minimum_payment(monthlyPayment, balance):
    return monthlyPayment * balance


def unpaid_balance(balance, minimumPayment):
    return balance - minimumPayment


def update_balance(unpaid_balance, monthly_interest):
    return unpaid_balance + (monthly_interest * unpaid_balance)


def calculate_statements(balance, annualInterestRate, monthlyPaymentRate):
    total = 0
    monthly_interest_rate = annualInterestRate / 12.0

    for i in range(12):
        payment = minimum_payment(monthlyPaymentRate, balance)
        balance = update_balance(unpaid_balance(balance, payment), monthly_interest_rate)
        print_statement(i, payment, balance)

        total += payment
    print_year_end(total, balance)


# calculate_statements(balance, annualInterestRate, monthlyPaymentRate)


balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

calculate_statements(balance, annualInterestRate, monthlyPaymentRate)
