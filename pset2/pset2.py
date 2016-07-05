#
# -----MIT 6.00x - PSET 2 -----
#
# by Dan Smith - 27/6/2016
# dan.smith.me@gmail.com
#
#


# ----- Problem One - Paying the Minimum -----


# def print_statement(month, payment, balance):
#     """
#     :param month: int month value
#     :param payment: int or float
#     :param balance: int or float
#
#     Prints out the required format of each statement
#     """
#     print("Month: " + str(month + 1))
#     print("Minimum monthly payment: " + str(round(payment, 2)))
#     print("Remaining balance: " + str(round(balance, 2)))
#
#
# def print_year_end(total, balance):
#     """
#     Prints out the required end of year summary
#     :param total: int or float
#     :param balance: int or float
#     """
#     print("Total paid: " + str(round(total, 2)))
#     print("Remaining balance: " + str(round(balance, 2)))
#
#
# def unpaid_balance(balance, minimumPayment):
#     return balance - minimumPayment
#
#
# def update_balance(unpaid_balance, monthly_interest):
#     return unpaid_balance + (monthly_interest * unpaid_balance)
#
#
# def calculate_statements(balance, annualInterestRate, monthlyPaymentRate):
#     total = 0
#     monthly_interest_rate = annualInterestRate / 12.0
#
#     for i in range(12):
#         payment = monthlyPaymentRate * balance
#         balance = update_balance(unpaid_balance(balance, payment), monthly_interest_rate)
#         print_statement(i, payment, balance)
#
#         total += payment
#     print_year_end(total, balance)


# # calculate_statements(balance, annualInterestRate, monthlyPaymentRate)
#
#
# balance = 11000
# annualInterestRate = 0.18
# monthlyPaymentRate = 0.04
#
# calculate_statements(balance, annualInterestRate, monthlyPaymentRate)


# # ----- Problem Two - Paying Debt Off in a Year -----
#
#
# def repayment_plan(balance, annual_interest_rate, term):
#     """
#     :param balance:
#     :param annual_interest_rate:
#     "param term: the number of months
#     Calculates and prints the lowest monthly payment to clear the balance within the time
#     """
#
#     monthly_interest_rate = annual_interest_rate / 12.0
#     lowest_payment = 10
#
#     while balance_after_term(balance, monthly_interest_rate, lowest_payment, term) > 0:
#         lowest_payment += 10
#
#     print("Lowest Payment: " + str(lowest_payment))
#
#
# def balance_after_term(balance, monthly_interest, payment, term):
#     """
#     :param balance: starting balance of the account
#     :param monthly_interest: monthly interest rate
#     :param payment: amount of each payment
#     :param term: duration in months of palan
#     :return: the balance after the full term of transactions
#     """
#     for i in range(term):
#         balance = update_balance(unpaid_balance(balance, payment), monthly_interest)
#
#     return balance
#
#
# def unpaid_balance(balance, minimumPayment):
#     return balance - minimumPayment
#
#
# def update_balance(unpaid_balance, monthly_interest):
#     return unpaid_balance + (monthly_interest * unpaid_balance)
#
#
# balance = 16000
# annualInterestRate = 0.2
# months = 24
#
# repayment_plan(balance, annualInterestRate, 12)

# # ----- Problem Three - Paying Debt Off in a Year BISECTIONAL -----


def repayment_plan(balance, annual_interest_rate, term):
    """
    :param balance:
    :param annual_interest_rate:
    "param term: the number of months
    Calculates and prints the lowest monthly payment to clear the balance within the time
    """
    monthly_interest_rate = annual_interest_rate / 12.0
    epsilon = 0.01
    high = balance_after_term(balance, monthly_interest_rate, 0, term) / float(term)

    low = balance / float(term)

    guess = (high + low) / 2.0
    new_balance = high * term

    while abs(new_balance) > epsilon:
        guess = (high + low) / 2.0
        new_balance = balance_after_term(balance, monthly_interest_rate, guess, term)

        if new_balance > epsilon:
            low = guess
        elif new_balance < -epsilon:
            high = guess

    print("Lowest Payment: " + str(round(guess, 2)))


def balance_after_term(aBalance, monthly_interest, payment, term):
    """
    :param balance: starting balance of the account
    :param monthly_interest: monthly interest rate
    :param payment: amount of each payment
    :param term: duration in months of palan
    :return: the balance after the full term of transactions
    """
    for i in range(term):
        aBalance = update_balance(unpaid_balance(aBalance, payment), monthly_interest)

    return aBalance


def unpaid_balance(uBalance, minimumPayment):
    return uBalance - minimumPayment


def update_balance(unpaid_balance, monthly_interest):
    return unpaid_balance + (monthly_interest * unpaid_balance)

# - Test Case 1 -
# balance = 320000
# annualInterestRate = 0.2
# repayment_plan(balance, annualInterestRate, 12)