#LoanPayment.py

"""This program will take a loan amount, an interest rate, and the number of years in order to run them
through a custom function and find monthly payment, total payment, and total interest payed over the years in the loan.
A loan amorization table will then be created"""


def loan_payment (P,i,t):
    R = (P * (i / 12)) / (1 - (1 + (i / 12)) ** (-12 * t))
    return R


amount = float(input("Enter the loan amount: "))

rate = float(input("Enter annual rate as a decimal: "))

time = int(input("Enter the number of years of the loan: "))

monthly = loan_payment(amount, rate, time)

print(f"\nThe monthly payment will be ${monthly:.2f}")
print(f"The total payments over {time} years will be ${monthly * 12 * time:.2f}")
print(f"The total interest paid over {time} years will be ${(monthly * 12 * time) - amount:.2f}")




print("\nLoan Amorization Table:")

print("\nMonth \t\tInterest Payment \t\tPrincipal Payment \t\tRemaining Balance")

for month in range(time * 12):
    
    i_pay = (rate * (1 / 12) * amount)
    
    princ_pay = monthly - i_pay
    
    amount = amount - princ_pay
    
    
    print(f"{month + 1:<13} ${i_pay:<22.2f} ${princ_pay:<25.2f} ${amount:.2f}")