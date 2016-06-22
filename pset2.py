def minimum_payment(balance, annualInterestRate, monthlyPaymentRate):
    monthly_interest = annualInterestRate / 12.0
    minimum_monthly_payment = monthlyPaymentRate * balance
    